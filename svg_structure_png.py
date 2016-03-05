#TODO width height
#TODO clean-up unnecessary stuff
def get_document_begin():
    return '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="1920px"
   height="1080px"
   id="svg8454"
   version="1.1"
   inkscape:version="0.48.4 r9939"
   sodipodi:docname="New document 9">
  <defs
     id="defs8456" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.84"
     inkscape:cx="960"
     inkscape:cy="383.13725"
     inkscape:document-units="px"
     inkscape:current-layer="layer1"
     showgrid="false"
     inkscape:window-width="2495"
     inkscape:window-height="1416"
     inkscape:window-x="65"
     inkscape:window-y="24"
     inkscape:window-maximized="1" />
  <metadata
     id="metadata8459">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     id="layer1"
     inkscape:label="Layer 1"
     inkscape:groupmode="layer">'''

def get_document_end():
    return '</g>\n</svg>'

def get_image(path, width, height, opacity="0"):
    result = '<image y="0" x="0" xlink:href="' + path + '" width="' + width + '" height="' + height + '" opacity="' + opacity + '" >\n'
    return result

def get_animation(id, offset, value="0"):
    result = '<animate id="' + id + '" attributeName="opacity" fill="freeze" begin="' + offset + '" dur="1ms" to="' + value + '" />\n'
    return result
   
def get_image_close_tag():
    return '</image>\n' 
