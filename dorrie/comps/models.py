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


class Spin(models.Model):
    """Class for the releases"""
    name = models.TextField(
        help_text="The name of the spin.")
    language = models.TextField()
    timezone = models.TextField()
    rootpwd = models.TextField()
    baseks = models.TextField()
    gplus = models.ManyToManyField('Group', related_name='gplus_set')
    gminus = models.ManyToManyField('Group', related_name='gminus_set')
    pplus = models.ManyToManyField('Package', related_name='pplus_set')
    pminus = models.ManyToManyField('Package', related_name='pminus_set')
    pid = models.IntegerField(default=0)


class Group(models.Model):
    """Package Groups"""
    name = models.TextField(help_text="The name of the package group.")


class Package(models.Model):
    """A Package."""
    name = models.TextField(help_text="The name of the package.")
