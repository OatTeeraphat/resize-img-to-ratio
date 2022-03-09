#!/usr/bin/python
from PIL import Image, ImageFilter
import math
import os

def resize_canvas(old_image_dir, new_image_dir, type='.png', padding=0, 
                  canvas_width=500, canvas_height=500):

    # Directory
    path = os.path.dirname(os.path.abspath(__file__)) + '/'
    dirs = os.listdir( path + str(old_image_dir) )

    for index, item in enumerate(dirs):

        try :

            old_image_path = path + str(old_image_dir) + item
            new_image_path, _ = os.path.splitext(path + str(new_image_dir) + item)

            if os.path.isfile(old_image_path):

                im = Image.open(old_image_path).convert('RGBA')
                old_width, old_height = im.size

                ratio = canvas_height / old_height

                if (old_width * ratio) > canvas_width :
                    ratio = canvas_width / old_width

                # Resize
                re_width = int(math.floor(old_width * ratio) - padding)
                re_height = int(math.floor(old_height * ratio) - padding)

                # Center the image
                x1 = int(math.floor((canvas_width - re_width) / 2))
                y1 = int(math.floor((canvas_height - re_height) / 2))

                im = im.resize((re_width, re_height), Image.ANTIALIAS)
                im = im.filter(ImageFilter.DETAIL)

                # New canvas
                if type == '.png' :
                    newImage = Image.new('RGBA', (canvas_width, canvas_height), (255, 255, 255, 0))
                    newImage.paste(im, (x1, y1, x1 + re_width, y1 + re_height))
                    newImage.save(new_image_path + str(type), 'PNG', quality=90, optimize=False)

                elif type == '.jpg' :
                    newImage = Image.new('RGB', (canvas_width, canvas_height), (255, 255, 255))
                    newImage.paste(im, (x1, y1, x1 + re_width, y1 + re_height), mask=im.split()[3])
                    newImage.save(new_image_path + str(type), 'JPEG', quality=90, optimize=False)

                else :
                    print('error : %s' %'not found extention of file (.jpg|.png)')
                    continue

                print('%d/%d : %s' %(index+1, len(dirs), new_image_path))

        except Exception as e :
            print('error : %s' %e)
            continue