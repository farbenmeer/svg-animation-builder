import sys, os, re
import xml.etree.ElementTree
import svg_structure, svg_structure_png

#input_dir = 'input/'
input_dir = 'png/'

ms_per_frame = "100ms"
ms_p_f = 100

width = '1920'#TODO from png
height = '1080'#TODO from png

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
    e = xml.etree.ElementTree.parse(input_dir + svg).getroot()
    e = e.find('{http://www.w3.org/2000/svg}g')
    e = e.find('{http://www.w3.org/2000/svg}path')
    path = e.get('d')
    return path

result = ""

def animate_svg():
    global result
    svgs = os.listdir(input_dir)
    svgs.sort(key=alphanum_key)
    
    result = svg_structure.get_document_begin()
    
    path = extract_path(svgs[0])
    result += svg_structure.get_path(path)
    offset = None
    for svg in svgs[1:]:
        svg_name = os.path.splitext(svg)[0]
        path = extract_path(svg)
        result += svg_structure.get_animation(name=svg_name, duration=ms_per_frame, path=path, offset=offset)
        offset = 'img_' + svg_name + '.begin + ' + ms_per_frame
    
    result += svg_structure.get_document_end()

def animate_png():
    global result
    pngs = os.listdir(input_dir)
    pngs.sort(key=alphanum_key)
    
    result = svg_structure_png.get_document_begin()
   
    offset = ms_p_f 
    
    #first image
    result += svg_structure_png.get_image(input_dir + pngs[0], width, height, opacity="1")
    id = 'img_' + os.path.splitext(pngs[0])[0]
    result += svg_structure_png.get_animation(id, ms_per_frame, "0")
    result += svg_structure_png.get_image_close_tag()

    for png in pngs[1:-1]:
        result += svg_structure_png.get_image(input_dir + png, width, height)
        id = 'img_' +  os.path.splitext(png)[0]
        result += svg_structure_png.get_animation(id, str(offset) + 'ms', "1")
        offset += ms_p_f
        result += svg_structure_png.get_animation(id, str(offset) + 'ms', "0")
        result += svg_structure_png.get_image_close_tag()
   
    #last image standing 
    result += svg_structure_png.get_image(input_dir + pngs[-1], width, height)
    id = 'img_' +  os.path.splitext(pngs[-1])[0]
    result += svg_structure_png.get_animation(id, str(offset) + 'ms', "1")
    result += svg_structure_png.get_image_close_tag()
    result += svg_structure_png.get_document_end()


#animate_svg()
animate_png()

#print(result)
text_file = open("animation.svg", "w")
text_file.write(result)
text_file.close()
