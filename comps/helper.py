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

from models import Spin, Group, Package

def get_spin(id):
    """
    return Spin object from id
    """
    return Spin.objects.get(id=id)


def new_spin(name, base_ks):
    """
    Return new spin
    """
    spin = Spin(name=name, baseks=base_ks)
    spin.save()
    return spin


def add_lang_tz(spin_id, lang, tz):
    """
    Add language and timezone
    """
    spin = get_spin(spin_id)
    spin.language = lang
    spin.timezone = tz
    spin.save()
    return spin


def package(name):
    """
    New or existing package
    """
    try:
        package = Package.objects.get(name__exact=name)
    except:
        package = Package(name=name)
        package.save()
    return package


def group(name):
    """
    New or existing group
    """
    try:
        group = Group.objects.get(name__exact=name)
    except:
        group = Group(name=name)
        group.save()
    return group


def add_rem_groups(spin, type, string):
    """
    $function_name
    """
    if string:
        g = group(string)
    else:
        return None
    if type == '+':
        if g in spin.gminus.all():
            spin.gminus.remove(g)
        elif g not in spin.gplus.all():
            spin.gplus.add(g)
        else:
            return None
        return 'Added group %s' % string
    elif type == '-':
        if g in spin.pplus.all():
            spin.gplus.remove(g)
        elif g not in spin.gminus.all():
            spin.gminus.add(g)
        else:
            return None
        return 'Removed group %s' % string
    else:
        return None
    

def add_rem_packages(spin, type, string):
    """
    $function_name
    """
    if string:
        p = package(string)
    else:
        return None
    if type == '+':
        if p in spin.pminus.all():
            spin.pminus.remove(p)
        elif p not in spin.pplus.all():
            spin.pplus.add(p)
        else:
            return None
        return 'Added package %s' % string
    elif type == '-':
        if p in spin.pplus.all():
            spin.pplus.remove(p)
        elif p not in spin.pminus.all():
            spin.pminus.add(p)
        else:
            return None
        return 'Removed package %s' % string
    else:
        return None
    

def select_helper(spin_id, type, action, string):
    """
    helper to select/deselect package/groups
    """
    spin = get_spin(spin_id)
    if type == 'p':
        return add_rem_packages(spin, action, string)
    elif type == 'g':
        return add_rem_groups(spin, action, string)
    else:
        return None
