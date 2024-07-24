import cv2
import numpy as np
from matplotlib import pyplot as plt
### classes i need
### worldstate contains pitch and both team objects
### team contains all players on a team
### player contains player position

img = cv2.imread("test.png")
plt.imshow(img)
plt.title("test image")
plt.xticks([]), plt.yticks([])
plt.show()