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

from django.db import models

# Create your models here.

class Spin(models.Model):
    """Class for the releases

    Table details:
    name: Name of the spin.
    language:
    timezone:
    rootpwd:
    baseks: base kickstart file
    groups_plus: added groups
    groups_minus: removed groups
    packages_plus: added packages
    packages_minus: removed packages
    """
    name = models.TextField()
    language = models.TextField()
    timezone = models.TextField()
    rootpwd = models.TextField()
    baseks = models.TextField()
    gplus = models.ManyToManyField('Group', related_name='gplus_set')
    gminus = models.ManyToManyField('Group', related_name='gminus_set')
    pplus = models.ManyToManyField('Package', related_name='pplus_set')
    pminus = models.ManyToManyField('Package', related_name='pminus_set')


class Group(models.Model):
    """Package Groups

    Table details:
    name: 
    """
    name = models.TextField()


class Package(models.Model):
    """Package

    Table details:
    name: 
    """
    name = models.TextField()
