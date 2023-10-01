import numpy as np
import cv2

image_hsv = 2

m = 1
x = 2

limite_superior = ((m + x) / 2) % 180
limite_inferior = ((m - x) / 2) % 180

h = image_hsv[:, :, 0]
s = image_hsv[:, :, 1]
v = image_hsv[:, :, 2]

inicio = h >= limite_inferior
final = h <= limite_superior

h = h.astype(np.uint16)

operacao = inicio & final if limite_inferior < limite_superior else inicio | final
h[operacao] = np.mod(h[operacao] + 90, 180).astype(np.uint8)

h = h.astype(np.uint8)

image_hsv = cv2.merge([h, s, v])