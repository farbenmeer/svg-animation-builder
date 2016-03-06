# svg-animation-builder - create stop-motion animated svg from images
Copyright (C) 2016 Josa Wode

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not, see [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).

# Readme

svg-animation-builder takes an image folder (containing png or svg images) as input and includes the still images into a stop-motion animation svg output file. Frames are ordered according to input filenames (in alphanumerical order).
It is written in Python 2.7 (visit [python.org](https://www.python.org) - there you can find instructions about how to install the python interpreter needed for running svg-animation-builder).

## Usage

python main.py [options]

### Options
*  -h, --help            show this help message and exit
*  -f OUTPUT\_FILENAME, --file=OUTPUT\_FILENAME
                        define output file (default: animation.svg)
*  -i INPUT\_FOLDER, --input=INPUT\_FOLDER
                        input folder (default: input/)
*  -o OUTPUT\_FOLDER, --output=OUTPUT\_FOLDER
                        output folder for png images (default: output/)
*  -t FILE\_TYPE, --type=FILE\_TYPE
                        input file type (png or svg) (default: png)
*  -s FRAME\_RATE, --step=FRAME\_RATE
                        frame rate in milliseconds (default: 100)
*  --width=WIDTH         scale images to the given width (ommit --height for aspect ratio)
*  --height=HEIGHT       scale images to the given height (ommit --width for aspect ratio)
*  -e, --embed           embed png data in svg animation file
*  -c, --copyright       show legal information and exit

### Examples

* python main.py
* python main.py --step=60 --output=fast-animation.svg
* python main.py -i svg-folder --type=svg 
* python main.py --width 1024

## Limitations / Known Issues / TODO

* Meta data for svg output file
* Allowed structure for input SVGs is very limited (program is only reading first `<path\>` of first `<g\>`-Element)
* Lots of limitations.

# Contact

* visit [coding.fotoelectrics](http://coding.fotoelectrics.de)
* mail to [coding@fotoelectrics](mailto:coding@fotoelectrics.de)
