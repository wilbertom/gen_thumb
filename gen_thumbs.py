import os
from PIL import Image
from argparse import ArgumentParser


size = (144, 96)

def thumb(image_name, size):
    """
    Tries to create a thumbnail for image_name with
    the given size, size is a tuple (width, height).
    Returns the new image.

    """
    im = None

    try:
        im = Image.open(image_name)
        im.thumbnail(size)
        name, ext = os.path.splitext(image_name)
        im.save("%s_thumb%s" % (name, ext))
    except IOError as e:
        print("Error creating thumb for %s: %s" % (image_name, e))

    return im

def thumb_dir(dir_path, size, filter_fun):
    """
    Creates thumbnails for all the images who return
    true with filter_fun(image_name).

    """
    for filename in os.listdir(dir_path):
        if filter_fun(filename):
            thumb("%s%s" % (dir_path, filename), size)

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('--ext', '-e', help='Extension of images', default='jpg')
    parser.add_argument('dirpath', help='Directory to thumbnail files.')
    parser.add_argument('--width', '-w', help='Width of the thumbnails', type=int, default=144)
    parser.add_argument('--height', '-he', help='Height of the thumbnails', type=int, default=96)
    
    args = parser.parse_args()

    thumb_dir(args.dirpath, (args.width, args.height), lambda f: f.endswith(args.ext))

