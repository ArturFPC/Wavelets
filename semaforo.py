import numpy as np
import pywt
import matplotlib.pyplot as plt

# Frequências para simular as cores do semáforo
frequencia_vermelho = 3e14 
frequencia_amarelo = 4.1e14  
frequencia_verde = 6.1e14  

# Duração total da simulação
tempo_total = 20  # 20 segundos
tempo = np.linspace(0, tempo_total, num=1000, endpoint=False)

# Crie os sinais de ondas eletromagnéticas para as cores do semáforo
sinal_vermelho = np.sin(2 * np.pi * frequencia_vermelho * tempo)
sinal_amarelo = np.sin(2 * np.pi * frequencia_amarelo * tempo)
sinal_verde = np.sin(2 * np.pi * frequencia_verde * tempo)

# Combine os sinais para criar o sinal do semáforo
sinal_semáforo = np.concatenate([sinal_vermelho[:500], sinal_amarelo[500:800], sinal_verde[800:]])
sinal_incorreto_semáforo = np.concatenate([sinal_vermelho[0:], sinal_amarelo[0:1000], sinal_verde[0:]])
# Realize a análise de CWT e plote os resultados
scales = np.arange(1, 128)
#utilizando a wavelet de morlet
cwtmatr, freqs = pywt.cwt(sinal_semáforo, scales, 'mexh')
#utilizando a wavelet de analytic morlet
#cwtmatr, freqs = pywt.cwt(sinal_semáforo, scales, 'cmor1.5-1.0')
#chapeu mexicano mexh

# Plote dos sinais das cores do semáforo
plt.figure(figsize=(12, 4))
plt.plot(tempo, sinal_vermelho, label='Vermelho')
plt.plot(tempo, sinal_amarelo, label='Amarelo')
plt.plot(tempo, sinal_verde, label='Verde')
plt.title('Sinais das Cores do Semáforo (Ondas Eletromagnéticas)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()

# Plote da transformada wavelet contínua
plt.figure(figsize=(12, 6))
plt.imshow(np.abs(cwtmatr), extent=[0, tempo_total, 1, 128], cmap='cool', aspect='auto')
plt.colorbar(label='Magnitude')
plt.title('Transformada Wavelet Contínua do Sinal do Semáforo (Ondas Eletromagnéticas)')
plt.xlabel('Tempo (s)')
plt.ylabel('Escala')
plt.show()

#analise do sinal incorreto
scales = np.arange(1, 128)
cwtmatr, freqs = pywt.cwt(sinal_incorreto_semáforo, scales, 'morl')
# Plote da transformada wavelet contínua
plt.figure(figsize=(12, 6))
plt.imshow(np.abs(cwtmatr), extent=[0, tempo_total, 1, 128], cmap='cool', aspect='auto')
plt.colorbar(label='Magnitude')
plt.title('Transformada Wavelet Contínua do Sinal do Semáforo (Ondas Eletromagnéticas)')
plt.xlabel('Tempo (s)')
plt.ylabel('Escala')
plt.show()
