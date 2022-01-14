This project is forked from https://bitbucket.org/ausguss/svg-animation-builder

# svg-animation-builder

svg-animation-builder creates stop-motion animated svg from images.

svg-animation-builder takes an image folder (containing svg images) as input and includes the still images into a stop-motion animation svg output file. Frames are ordered according to input filenames (in alphanumerical order).
It is written in Python 2.7 (visit [python.org](https://www.python.org) - there you can find instructions about how to install the python interpreter needed for running svg-animation-builder).

## Usage

```sh
python main.py [options]
```

### Options

- `-h`, `--help`

  show this help message and exit

- `-f OUTPUT_FILENAME`, `--file=OUTPUT_FILENAME`

  define output file (default: `animation.svg`)

- `-i INPUT_FOLDER`, `--input=INPUT_FOLDER`

  input folder (default: `input/`)

- `-s FRAME_RATE`, `--step=FRAME_RATE`

  frame rate in milliseconds (default: `100`)

- `--width=WIDTH`

  scale images to the given width (ommit `--height` for aspect ratio)

- `--height=HEIGHT`

  scale images to the given height (ommit `--width` for aspect ratio)

- `-c`, `--copyright`

  show legal information and exit

### Examples

```sh
python main.py
python main.py --step=60 --output=fast-animation.svg
python main.py -i svg-folder
python main.py --width 1024
```

## Limitations / Known Issues / TODO

- Meta data for svg output file
- Allowed structure for input SVGs is very limited (program is only reading first `<path\>` of first `<g\>`-Element)
- Lots of limitations.

# Licence

Author: Josa Wode 2016

This project is [GNU licensed](./LICENCE)

# Contact

- visit [coding.josawode](https://coding.josawode.de)
- mail to [coding@josawode](mailto:coding@josawode.de)
