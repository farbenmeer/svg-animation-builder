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
   width="''' + width + '''px"
   height="''' + height + '''px"
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
    return '</g>\n</svg>'

def get_image(path, width, height, opacity="0", data=None):
    if data == None:
        png = path
    else:
        png = 'data:image/png;base64,' + data
    result = '<image y="0" x="0" xlink:href="' + png + '" width="' + width + '" height="' + height + '" opacity="' + opacity + '" >\n'
    return result

def get_animation(id, offset, value="0"):
    result = '<animate id="' + id + '" attributeName="opacity" fill="freeze" begin="' + offset + '" dur="1ms" to="' + value + '" />\n'
    return result
   
def get_image_close_tag():
    return '</image>\n' 
