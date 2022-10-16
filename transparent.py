import glob
import re

import cv2
import numpy as np

# Get paths to all images in the folder
img_path = glob.glob('img/*.jpg') + glob.glob('img/*.png')

for img in img_path:
    # get file name
    fn = re.findall(r"/(.+)\.", img)[0]

    # load the image
    img = cv2.imread(img, -1)

    # create a mask
    img[:, :, 3] = np.where(np.all(img == 255, axis=-1), 0, 255)

    # save the image
    print(f"save {fn}.png")
    cv2.imwrite(f"{fn}.png", img)
