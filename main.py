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

import sys, os, re
from optparse import OptionParser
import svg_structure
import svg_tools

copyright_info = '''
svg-animation-builder - create stop-motion animated svg from images
Copyright (C) 2016 Josa Wode

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.
'''

def setup_command_line_parser():
    cl_parser = OptionParser()
    cl_parser.add_option("-f", "--file", dest="output_filename", help="define output file (default: animation.svg)", default='animation.svg')
    cl_parser.add_option("-i", "--input", dest="input_folder", help="input folder (default: input/)", default='input/')
    cl_parser.add_option("-s", "--step", dest="frame_rate", help="frame rate in milliseconds (default: 100)", type="int", default=100)
    cl_parser.add_option("", "--width", dest="width", help="scale images to the given width (ommit --height for aspect ratio)", type="int", default=None)
    cl_parser.add_option("", "--height", dest="height", help="scale images to the given height (ommit --width for aspect ratio)", type="int", default=None)
    cl_parser.add_option("-c", "--copyright", action="store_true", dest="copyright_info", help="show legal information and exit", default=False)
    return cl_parser

def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def animate_svg():
    global result
    svgs = os.listdir(options.input_folder)
    svgs.sort(key=alphanum_key)

    (width, height, wratio, hratio) = svg_tools.extract_image_info(options.input_folder + svgs[0], options.width, options.height)
    result = svg_structure.get_document_begin(width, height)

    path = svg_tools.extract_path(options.input_folder + svgs[0])
    result += svg_structure.get_path(path, wratio, hratio)
    offset = None
    for svg in svgs[1:]:
        svg_name = os.path.splitext(svg)[0]
        path = svg_tools.extract_path(options.input_folder + svg)
        result += svg_structure.get_animation(name=svg_name, duration=str(options.frame_rate) + 'ms', path=path, offset=offset)
        offset = 'img_' + svg_name + '.begin + ' + str(options.frame_rate) + 'ms'

    result += svg_structure.get_document_end()
    return result

def main():
    if options.copyright_info:
        print(copyright_info)
        exit()

    if options.input_folder[-1] != '/':
        options.input_folder += '/'

    result = animate_svg()
    text_file = open(options.output_filename, "w")
    text_file.write(result)
    text_file.close()
    print('stored animation in "' + options.output_filename + '"')

if __name__ == "__main__":
    cl_parser = setup_command_line_parser()
    (options, args) = cl_parser.parse_args()

    main()
