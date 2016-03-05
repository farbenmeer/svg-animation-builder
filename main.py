import sys, os, re
#import xml.etree.ElementTree
from optparse import OptionParser
import svg_structure, svg_structure_png
import png_tools, svg_tools

def setup_command_line_parser():
    cl_parser = OptionParser()
    cl_parser.add_option("-o", "--output", dest="output_filename", help="define output file", default='animation.svg')
    cl_parser.add_option("-i", "--input", dest="input_folder", help="input folder", default='input/')
    cl_parser.add_option("-t", "--type", dest="file_type", help="input file type (png or svg)", default='png')
    cl_parser.add_option("-s", "--step", dest="frame_rate", help="frame rate in milliseconds", type="int", default=100)
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
    
    (width, height) = svg_tools.extract_image_info(options.input_folder + svgs[0]) 
    result = svg_structure.get_document_begin(width, height)
    
    path = svg_tools.extract_path(options.input_folder + svgs[0])
    result += svg_structure.get_path(path)
    offset = None
    for svg in svgs[1:]:
        svg_name = os.path.splitext(svg)[0]
        path = svg_tools.extract_path(options.input_folder + svg)
        result += svg_structure.get_animation(name=svg_name, duration=str(options.frame_rate) + 'ms', path=path, offset=offset)
        offset = 'img_' + svg_name + '.begin + ' + str(options.frame_rate) + 'ms'
    
    result += svg_structure.get_document_end()
    return result


def animate_png():
    global result
    pngs = os.listdir(options.input_folder)
    pngs.sort(key=alphanum_key)
    
    #take width, height from first image (all should be same size)
    width, height = png_tools.get_image_info(options.input_folder + pngs[0])
    width = str(width)
    height = str(height)

    result = svg_structure_png.get_document_begin(width, height)
   
    offset = options.frame_rate 
    
    #first image
    result += svg_structure_png.get_image(options.input_folder + pngs[0], width, height, opacity="1")
    id = 'img_' + os.path.splitext(pngs[0])[0]
    result += svg_structure_png.get_animation(id, str(offset) + 'ms', "0")
    result += svg_structure_png.get_image_close_tag()

    for png in pngs[1:-1]:
        result += svg_structure_png.get_image(options.input_folder + png, width, height)
        id = 'img_' +  os.path.splitext(png)[0]
        result += svg_structure_png.get_animation(id, str(offset) + 'ms', "1")
        offset += options.frame_rate
        result += svg_structure_png.get_animation(id, str(offset) + 'ms', "0")
        result += svg_structure_png.get_image_close_tag()
   
    #last image standing 
    result += svg_structure_png.get_image(options.input_folder + pngs[-1], width, height)
    id = 'img_' +  os.path.splitext(pngs[-1])[0]
    result += svg_structure_png.get_animation(id, str(offset) + 'ms', "1")
    result += svg_structure_png.get_image_close_tag()
    result += svg_structure_png.get_document_end()
    return result


def main():
    if options.input_folder[-1] != '/':#TODO windows?
        options.input_folder += '/'
    
    #result = ""

    if options.file_type.upper() == "SVG":
        result = animate_svg()
    elif options.file_type.upper() == "PNG":
        result = animate_png()
    else:
        print('invalid input file type "' + options.file_type + '", supported: png, svg')
        exit()

    #print(result)
    text_file = open(options.output_filename, "w")
    text_file.write(result)
    text_file.close()

if __name__ == "__main__":
    cl_parser = setup_command_line_parser()
    (options, args) = cl_parser.parse_args()
    
    main()

