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

#TODO meta data
def get_document_begin(width, height):
    return '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with svg-animation-builder (https://bitbucket.org/ausguss/svg-animation-builder) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   width="''' + str(width) + '''px"
   height="''' + str(height) + '''px"
   version="1.1">
  <metadata>
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/MovingImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g id="animation">
'''

def get_document_end():
    return '</path>\n  </g>\n</svg>'

def get_path(path, wratio=1.0, hratio=1.0):
    result = '<path style="fill:#000000" '
    if wratio != 1.0 and hratio != 1.0:
        result += 'transform="scale(' + str(wratio) + ',' + str(hratio) + ')" \n'
    result += 'd="' + path + '" >\n'
    return result

def get_animation(name, duration, path, offset=None):
    result = '<animate id="img_' + name + '" attributeName="d" fill="freeze" dur="' + duration + '" '
    if offset != None:
        result += 'begin="' + offset + '" '
    result += 'to="' + path + '" />\n'
    return result 
