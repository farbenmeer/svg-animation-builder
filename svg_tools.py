# svg-animation-builder - create stop-motion animated svg from images
# Copyright (C) 2016 Josa Wode
#
# This file is part of svg-animation-builder.
#
# svg-animation-builder is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# svg-animation-builder is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

import xml.etree.ElementTree

def extract_path(filepath):
    e = xml.etree.ElementTree.parse(filepath).getroot()
    e = e.find('{http://www.w3.org/2000/svg}g')
    e = e.find('{http://www.w3.org/2000/svg}path')
    path = e.get('d')
    return path

def extract_image_info(filepath):
    e = xml.etree.ElementTree.parse(filepath).getroot()
    return (e.get('width'), e.get('height'))
