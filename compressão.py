from matplotlib.image import imread
import numpy as np
import matplotlib.pyplot as plt
import pywt
plt.rcParams['figure.figsize'] = [16, 16]
plt.rcParams.update({'font.size': 18})

A = imread(r'C:\\Users\\artur\\OneDrive\\Área de Trabalho\\PDI\\exemplo_imagem\\img.jpg')
B = np.mean(A, -1); # converte para escala de cinza

#Compressão utilizando wavelets
n = 4
w = 'db1'
coeffs = pywt.wavedec2(B, wavelet = w, level=n)

coeffs_arr, coeff_slices = pywt.coeffs_to_array(coeffs)

Csort = np.sort(np.abs(coeffs_arr.reshape(-1)))

for keep in (0.1, 0.05, 0.01, 0.005):
    thresh= Csort[int(np.floor((1-keep)*len(Csort)))]
    ind = np.abs(coeffs_arr) > thresh
    Cfilt = coeffs_arr * ind  # Threshold small indices

    coeffs_filt = pywt.array_to_coeffs(Cfilt, coeff_slices, output_format='wavedec2')

    #plotando a imagem reconstruida
    Arecon = pywt.waverec2(coeffs_filt, wavelet=w)
    plt.figure()
    plt.imshow(Arecon.astype('uint8'), cmap='gray_r')
    plt.axis('off')
    plt.rcParams['figure.figsize'] = [8, 8]
    plt.title('Compressão = %.1f%% da energia original' % (keep*100))
    plt.show()
