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
    return '</path>\n  </g>\n</svg>'

def get_path(path):
    return '''    <path
       style="fill:#000000"
       d="''' + path + '''" >
'''

def get_animation(name, duration, path, offset=None):
    result = '<animate id="img_' + name + '" attributeName="d" fill="freeze" dur="' + duration + '" '
    if offset != None:
        result += 'begin="' + offset + '" '
    result += 'to="' + path + '" />\n'
    return result 
