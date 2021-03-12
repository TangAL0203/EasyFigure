import os

import cv2
from tqdm import tqdm

img_dir = 'xxx'

# general settings
framesize = (1920, 1080)  # WH
fps = 15
time = 190  # seconds
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
save = 'save.mp4'.format(time)
videoWriter = cv2.VideoWriter(save, fourcc, fps, framesize)

sorted_imgs = os.listdir(img_dir)
num_img = time * fps
assert num_img < len(sorted_imgs)

for ii in tqdm(range(num_img)):
    img_name = sorted_imgs[ii]
    img = cv2.imread(os.path.join(img_dir, img_name))
    videoWriter.write(img)

videoWriter.release()
cv2.destroyAllWindows()
