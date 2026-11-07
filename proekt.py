import numpy as np
import matplotlib.pyplot as plt

chastota_diskret = 1000
dlitelnost = 1.0
chastota_signala = 50

t = np.arange(0, dlitelnost, 1 / chastota_diskret)
signal = np.sin(2 * np.pi * chastota_signala * t)
np.random.seed(42)
noise = np.random.normal(0, 0.5, len(t))
noisy_signal = signal + noise
spectr = np.fft.rfft(noisy_signal)
frequencies = np.fft.rfftfreq(len(t), 1 / chastota_diskret)
amplituda = 2 * np.abs(spectr) / len(t)
amplituda[0] /= 2
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, signal)
plt.title('Исходный сигнал')
plt.xlabel('Времяб с')
plt.ylabel('Амплитуда')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, noisy_signal)
plt.title('С шумом')
plt.xlabel('Времяб с')
plt.ylabel('Амплитуда')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(frequencies, amplituda)
plt.title('Спектр после ФФТ')
plt.xlabel('Частота, гц')
plt.ylabel('Амплитуда')
plt.xlim(0, 200)
plt.grid()

plt.tight_layout()
plt.show()