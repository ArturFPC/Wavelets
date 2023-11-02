import matplotlib.pyplot as plt
import numpy as np
import pywt
from matplotlib.image import imread

# Carrega a imagem
i = imread(r'C:\\Users\\artur\\OneDrive\\Área de Trabalho\\PDI\\filtragem\\big-ben.jpg')
im = np.mean(i, -1); # converte para escala de cinza

# Aplica ruído gaussiano
imn = im + 30*np.random.randn(*im.shape)

#Mostra a imagem
plt.figure()
plt.imshow(imn.astype('uint8'), cmap='gray')
plt.axis('off')
plt.title('Imagem com ruído')
plt.show()

# Realiza decomposição wavelet
n = 2
w = 'db1'
coeffs = pywt.wavedec2(imn, wavelet = w, level=n)

#Zera os coeficientes de detalhes do nivel 1
coeffs[1] = [np.zeros_like(c) for c in coeffs[1]]

#Reconstrói a imagem
imr = pywt.waverec2(coeffs, wavelet=w)

#Mostra a imagem
plt.figure()
plt.imshow(imr.astype('uint8'), cmap='gray')
plt.axis('off')
plt.title('Imagem filtrada')
plt.show()

#Zera os coeficientes de detalhes do nivel 2
coeffs[2] = [np.zeros_like(c) for c in coeffs[2]]

#Reconstrói a imagem
imr = pywt.waverec2(coeffs, wavelet=w)

#Mostra a imagem
plt.figure()
plt.imshow(imr.astype('uint8'), cmap='gray')
plt.axis('off')
plt.title('Imagem filtrada')
plt.show()
