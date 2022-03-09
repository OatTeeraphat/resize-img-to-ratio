# PY- Resize Image To Ratio
python script to resize image to your ratio (new canvas) with fit scale use PIL

Clone this repository, config your directory and file resolution and run these commands in  python3 terminal .

First Step Install Dependency:
```sh
pip install -r requirements.txt
```

Second Step - Config function in app.py file:
```sh
r.resize_canvas(
    old_image_dir='sample_image/', #original image directory
    new_image_dir='resize/', #new image directory
    type='.png', #.png|.jpg
    padding=50, #padding your image
    canvas_width=750, #new canvas width
    canvas_height=400 #new canvas height
)
```

Third Step - Run python script:
```sh
python app.py
```

> Note: required python 3 and PILLOW Library.

enjoy it :)

*Hell Yeah! - https://github.com/OatTeeraphat/resize-img-to-ratio**

