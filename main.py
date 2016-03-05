import sys, os, re
import xml.etree.ElementTree
from optparse import OptionParser
import svg_structure, svg_structure_png
import png_tools

cl_parser = OptionParser()
cl_parser.add_option("-o", "--output", dest="output_filename", help="define output file", default='animation.svg')
cl_parser.add_option("-s", "--source", dest="input_folder", help="input folder", default='input/')
cl_parser.add_option("-t", "--type", dest="file_type", help="input file type (png or svg)", default='png')

(options, args) = cl_parser.parse_args()

if options.input_folder[-1] != '/':#TODO windows?
    options.input_folder += '/'

ms_per_frame = 100

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

def extract_path(svg):
    e = xml.etree.ElementTree.parse(options.input_folder + svg).getroot()
    e = e.find('{http://www.w3.org/2000/svg}g')
    e = e.find('{http://www.w3.org/2000/svg}path')
    path = e.get('d')
    return path

def extract_image_info(svg):
    e = xml.etree.ElementTree.parse(options.input_folder + svg).getroot()
    return (e.get('width'), e.get('height'))

result = ""

def animate_svg():
    global result
    svgs = os.listdir(options.input_folder)
    svgs.sort(key=alphanum_key)
    
    (width, height) = extract_image_info(svgs[0]) 
    result = svg_structure.get_document_begin(width, height)
    
    path = extract_path(svgs[0])
    result += svg_structure.get_path(path)
    offset = None
    for svg in svgs[1:]:
        svg_name = os.path.splitext(svg)[0]
        path = extract_path(svg)
        result += svg_structure.get_animation(name=svg_name, duration=str(ms_per_frame) + 'ms', path=path, offset=offset)
        offset = 'img_' + svg_name + '.begin + ' + str(ms_per_frame) + 'ms'
    
    result += svg_structure.get_document_end()

def animate_png():
    global result
    pngs = os.listdir(options.input_folder)
    pngs.sort(key=alphanum_key)
    
    #take width, height from first image (all should be same size)
    width, height = png_tools.get_image_info(options.input_folder + pngs[0])
    width = str(width)
    height = str(height)

    result = svg_structure_png.get_document_begin(width, height)
   
    offset = ms_per_frame 
    
    #first image
    result += svg_structure_png.get_image(options.input_folder + pngs[0], width, height, opacity="1")
    id = 'img_' + os.path.splitext(pngs[0])[0]
    result += svg_structure_png.get_animation(id, str(offset) + 'ms', "0")
    result += svg_structure_png.get_image_close_tag()

    for png in pngs[1:-1]:
        result += svg_structure_png.get_image(options.input_folder + png, width, height)
        id = 'img_' +  os.path.splitext(png)[0]
        result += svg_structure_png.get_animation(id, str(offset) + 'ms', "1")
        offset += ms_per_frame
        result += svg_structure_png.get_animation(id, str(offset) + 'ms', "0")
        result += svg_structure_png.get_image_close_tag()
   
    #last image standing 
    result += svg_structure_png.get_image(options.input_folder + pngs[-1], width, height)
    id = 'img_' +  os.path.splitext(pngs[-1])[0]
    result += svg_structure_png.get_animation(id, str(offset) + 'ms', "1")
    result += svg_structure_png.get_image_close_tag()
    result += svg_structure_png.get_document_end()


if options.file_type.upper() == "SVG":
    animate_svg()
elif options.file_type.upper() == "PNG":
    animate_png()
else:
    print('invalid input file type "' + options.file_type + '", supported: png, svg')
    exit()

#print(result)
text_file = open(options.output_filename, "w")
text_file.write(result)
text_file.close()
