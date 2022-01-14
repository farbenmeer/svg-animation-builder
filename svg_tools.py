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

def extract_image_info(filepath, required_width, required_height):
    e = xml.etree.ElementTree.parse(filepath).getroot()
    width = e.get('width')
    height = e.get('height')

    #convert attribute to float
    if width.endswith('px'):
        width = width[:-2]
    width = float(width)
    if height.endswith('px'):
        height = height[:-2]
    height = float(height)

    if required_width == required_height == None:
        return (int(width), int(height), 1.0, 1.0)

    if required_width != None and required_height != None:
        wratio = float(required_width)/float(width)
        hratio = float(required_height)/float(height)
        return (required_width, required_height, wratio, hratio)

    if required_width == None:
        ratio = float(required_height)/height
    else: #if required_height == None:
        ratio = float(required_width)/width
    width = width*ratio
    height = height*ratio

    width = int(round(width))
    height = int(round(height))

    return (width, height, ratio, ratio)
