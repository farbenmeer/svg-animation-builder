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

import struct

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

#if __name__ == '__main__':
#    with open('foo.png', 'rb') as f:
#        data = f.read()
#
#    print is_png(data)
#    print get_image_info(data)
