# sine_wave.py
import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(frequency, duration, sample_rate):
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    amplitude = np.sin(2 * np.pi * frequency * time)
    return time, amplitude

def plot_sine_wave(frequency=250, duration=1, sample_rate=44100):
    time, amplitude = generate_sine_wave(frequency, duration, sample_rate)

    plt.plot(time, amplitude, label=f'Sine Wave ({frequency} Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Single Sine Wave')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_sine_wave()
