# Dorrie - Web interface for building Fedora Spins/Remixes. 
# Copyright (C) 2009 Red Hat Inc.
# Author: Shreyank Gupta <sgupta@redhat.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib
import os
from comps import Comps
from helper import get_spin
from hardwareLists import langDict
import pytz
#import rhpl.keyboard as keyboard

from settings import COMPS_URL, KS_DIR, CACHE, MEDIA_ROOT

from pykickstart.parser import *
from pykickstart.version import makeVersion


def get_comps():
    """
    parse and return comps object
    """
    fd = urllib.urlopen(COMPS_URL)
    c = Comps()
    c.add(fd)
    return c
    

def ls_ks():
    """
    List files in KS_DIR
    """
    ksts = os.listdir(KS_DIR)
    choicelist = []
    for kst in ksts:
        #if kst.find('_') == -1:
        ks_tuple = (kst, kst.split('.')[0])
        choicelist.append(ks_tuple)
    return tuple(choicelist)


def languages():
    """
    Return list of languages
    """
    choicelist = []
    for text, code in langDict.iteritems():
        choicelist.append((code, text))
    return tuple(choicelist)
    

def timezones():
    """
    Return list of timezones
    """
    choicelist = []
    for each in pytz.common_timezones:
        choicelist.append((each, each))
    return tuple(choicelist)


def kickstart(ks, path=KS_DIR):
    """
    return parsed pykickstart object
    """
    ks = "%s%s" % (path, ks)
    ksparser = KickstartParser(makeVersion())
    ksparser.readKickstart(ks)
    return ksparser


def get_lang_tz(ks):
    """
    return default language and timezole from base kickstart
    """
    ksparser = kickstart(ks)
    dict = {}
    dict['select_language'] = ksparser.handler.lang.lang.split('.')[0]
    dict['select_timezone'] = ksparser.handler.timezone.timezone
    return dict


def default_selected(ks):
    """
    Return default groups from baseks
    """
    ksparser = kickstart(ks)
    groups = [group.name for group in ksparser.handler.packages.groupList]
    plus = ksparser.handler.packages.packageList
    minus = ksparser.handler.packages.excludedList
    return groups, plus, minus


def package_listing(c):
    """
    Return a nicely parsed package-group listing 
    """
    result = {}
    for group, object in c._groups.iteritems():
        mandatory = object.mandatory_packages.keys()
        default = object.default_packages.keys()
        optional = object.optional_packages.keys()
        result[group] = [mandatory, default, optional]
    return result


def kpgrp_list(object):
    """
    return ksparser.group list from db object
    """
    list = []
    for each in object.all():
        list.append(Group(name=each.name))
    return list


def build_ks(id):
    """
    Build Modified KS file
    """
    spin = get_spin(id)
    folder = "%s%s_%s/" % (CACHE, spin.id, spin.name)
    
    link = "%s/cache" % MEDIA_ROOT
   
    #build paths
    if not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(link):
        os.symlink(CACHE, link)

    ksparser = kickstart(spin.baseks)
   
    #change lang, tz

    ksparser.handler.lang.lang = spin.language
    ksparser.handler.timezone.timezone = spin.timezone

    #Packages and Groups

    gplus = kpgrp_list(spin.gplus)
    gminus = kpgrp_list(spin.gminus)
    pplus = [p.name for p in spin.pplus.all()]
    pminus = [p.name for p in spin.pminus.all()]

    for each in gminus:
        try:
            ksparser.handler.packages.groupList.remove(each)
        except:
            pass
    for each in gplus:
        ksparser.handler.packages.groupList.append(each)

    ksparser.handler.packages.packageList.extend(pplus)
    ksparser.handler.packages.excludedList.extend(pminus)
    
    #write new ks file
    filename = "%s%s.ks" % (folder, spin.name)
    fd = open(filename, 'w')
    fd.write(ksparser.handler.__str__())
    fd.close()

    linkname = "/static/cache/%s_%s/%s.ks" % \
        (spin.id, spin.name, spin.name)

    return linkname
    
    


