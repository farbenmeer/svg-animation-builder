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

import struct, os, shutil
import Image

def get_image_info_data(data):
    if is_png(data):
        w, h = struct.unpack('>LL', data[16:24])
        width = int(w)
        height = int(h)
    else:
        raise Exception('not a png image')
    return width, height

def is_png(data):
    return (data[:8] == '\211PNG\r\n\032\n'and (data[12:16] == 'IHDR'))

def get_image_info(filename):
    result = None
    with open(filename, 'rb') as f:
        data = f.read()
        result = get_image_info_data(data)
        f.close()
    return result

def get_base64(filepath):
    png = open(filepath, 'rb')
    base64 = png.read().encode("base64").replace('\n', '')
    png.close()
    return base64

def scale_folder(input, output, width=None, height=None):
    if os.path.exists(output):
        shutil.rmtree(output)
    shutil.copytree(input, output)
    if width == height == None:
        return #save some time
    for img in os.listdir(input):
        scale(output + img, width, height)

def scale(image, width=None, height=None):
    if width == height == None:
        print("width or height required, both were 'None'")
        return
    try:
        img = Image.open(image)
        size = img.size
        
        if width == None or height == None:
            #calculate scale
            if width == None:
                ratio = float(height)/float(size[1])
            if height == None:
                ratio = float(width)/float(size[0])
            width = size[0]*ratio
            height = size[1]*ratio
            width = int(round(width))
            height = int(round(height))
        
        print("scaling image '" + image + "' to " + str(width) + "x" + str(height))
        img = img.resize((width, height), Image.ANTIALIAS)
        img.save(image)
    except IOError:
        print("failed scaling image '" + image + "'")


