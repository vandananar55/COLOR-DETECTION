

import numpy as np
import cv2
import matplotlib.pyplot as plt

# change this image path accroding to local image path
img = cv2.imread("/home/anmol/Downloads/ne.png")
plt.figure(figsize=(10,10))
plt.imshow(img)


new_image=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10,10))
plt.imshow(new_image)

hsv_image=cv2.cvtColor(new_image,cv2.COLOR_RGB2HSV)
lower=np.array([0,100,100])
upper=np.array([200,255,255])
mask=cv2.inRange(hsv_image,lower,upper)

plt.figure(figsize=(10,10))
plt.imshow(mask)

rest=cv2.bitwise_and(new_image,new_image,mask=mask)
plt.figure(figsize=(10,10))
plt.imshow(rest)
