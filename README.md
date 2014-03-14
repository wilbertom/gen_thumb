Gen Thumb
====

A utility for generating thumbnails on the fly.


Usage
====

Requirements: `pip install -r requirements.txt`

This command creates a thumbnail of size `500px` by `500px` for all `jpg` images in the `images_directory`.

`python gen_thumbs.py -e jpg -w 500 -he 500 <images_directory>`

Thumbnails for all `jpg` images with default `144px` by `96px` values.

`python gen_thumbs.py -e jpg ./images/`

With `jpg` default:

`python gen_thumbs.py ./images/`

You can read the source code and have it do fancier stuff, but this is just a simple script.

```
usage: gen_thumbs.py [-h] [--ext EXT] [--width WIDTH] [--height HEIGHT]
                     dirpath

positional arguments:
  dirpath               Directory to thumbnail files.

optional arguments:
  -h, --help            show this help message and exit
  --ext EXT, -e EXT     Extension of images
  --width WIDTH, -w WIDTH
                        Width of the thumbnails
  --height HEIGHT, -he HEIGHT
                        Height of the thumbnails

```
