from matplotlib.image import imread
import numpy as np
import matplotlib.pyplot as plt
import pywt
plt.rcParams['figure.figsize'] = [16, 16]
plt.rcParams.update({'font.size': 18})

A = imread(r'C:\\Users\\artur\\OneDrive\\Área de Trabalho\\PDI\\exemplo_imagem\\img.jpg')
B = np.mean(A, -1); # converte para escala de cinza

#Decomposição wavelet (nível 2) utilizando wavelet db1
n = 2
w = 'db1'
coeffs = pywt.wavedec2(B, wavelet = w, level=n)

#normalização dos coeficientes
coeffs[0] /= np.abs(coeffs[0]).max()
for detail_level in range(n):
    coeffs[detail_level + 1] = [d/np.abs(d).max() for d in coeffs[detail_level + 1]]
arr, coeff_slices = pywt.coeffs_to_array(coeffs)

plt.imshow(arr, cmap='gray_r',vmin=-0.25, vmax=0.75)
plt.rcParams['figure.figsize'] = [16, 16]
plt.show()
