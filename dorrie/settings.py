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

# Django settings for dorrie project.

import os.path
import glob

try:
    DORRIE_ROOT
except NameError:
    DORRIE_ROOT = os.path.dirname(__file__)

conf_files_path = os.path.join(DORRIE_ROOT, 'settings', '*.conf')
conffiles = glob.glob(conf_files_path)
conffiles.sort()

for f in conffiles:
    execfile(os.path.abspath(f))
