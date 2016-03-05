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
