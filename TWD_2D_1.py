import cv2
import pywt
import numpy as np
import matplotlib.pyplot as plt

# Carregue uma imagem
image = cv2.imread('imagem1.jpg', cv2.IMREAD_GRAYSCALE)

# Execução da transformada wavelet 2D (por exemplo, utilizando a wavelet de Haar)
coeffs = pywt.dwt2(image, 'haar')

cA, (cH, cV, cD) = coeffs  # cA: Aproximação, cH: Horizontal, cV: Vertical, cD: Diagonal

# Visualização das sub-imagens resultantes
plt.figure(figsize=(12, 3))
plt.subplot(141), plt.imshow(cA, cmap='gray'), plt.title('Aproximação')
plt.subplot(142), plt.imshow(cH, cmap='gray'), plt.title('Horizontal')
plt.subplot(143), plt.imshow(cV, cmap='gray'), plt.title('Vertical')
plt.subplot(144), plt.imshow(cD, cmap='gray'), plt.title('Diagonal')

plt.show()