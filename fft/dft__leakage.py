import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Sample rate and duration
fs = 100  # Hz
t = np.arange(0, 1, 1/fs)  # time vector

# Original signal (sine wave)
f = 5  # frequency in Hz
#original_signal = np.sin(2 * np.pi * f * t)

sigma = 0.08
mu = 0.5*np.max(t)
original_signal = 1/np.sqrt(2*np.pi)/sigma * np.exp(-0.5*((t-mu)/sigma)**2)

# Rectangular window function
window = np.ones_like(t)
window_width = 0.2
window[:int((0.5-window_width/2)*len(t))] = 0
window[ int((0.5+window_width/2)*len(t)):] = 0

# Signal multiplied by the window function
windowed_signal = original_signal * window

# Perform Discrete Fourier Transform (DFT)
fft_original = fft(original_signal)
fft_window = fft(window)
fft_windowed_signal = fft(windowed_signal)

# Frequency vector for plotting
freq = np.linspace(0, fs, len(t))

# Creating a 3x2 subplot structure
fig, axs = plt.subplots(3, 2, figsize=(12, 8))

# Plotting the original signal in time and frequency domain
axs[0, 0].plot(t, original_signal, linestyle=":", color='blue')
axs[0, 0].set_title("Original Signal (Time Domain)")
axs[0, 0].set_xlabel("Time")
axs[0, 0].set_ylabel("$s$")
axs[0, 0].set_xlim(min(t), max(t))

axs[0, 1].plot(freq, np.abs(fft_original), linestyle=":", color='red')
axs[0, 1].set_title("Original Signal (Frequency Domain)")
axs[0, 1].set_xlabel("Frequency")
axs[0, 1].set_ylabel(r"$|F(s)|$")
axs[0, 1].set_xlim(min(freq), max(freq))
axs[0, 1].set_yscale('log')

# Plotting the window function in time and frequency domain
axs[1, 0].plot(t, window, linestyle=":", color='blue')
axs[1, 0].set_title("Rectangular Window (Time Domain)")
axs[1, 0].set_xlabel("Time")
axs[1, 0].set_ylabel("$s$")
axs[1, 0].set_xlim(min(t), max(t))

axs[1, 1].plot(freq, np.abs(fft_window), linestyle=":", color='red')
axs[1, 1].set_title("Rectangular Window (Frequency Domain)")
axs[1, 1].set_xlabel("Frequency")
axs[1, 1].set_ylabel(r"$|F(s)|$")
axs[1, 1].set_xlim(min(freq), max(freq))
axs[1, 1].set_yscale('log')


# Plotting the windowed signal in time and frequency domain
axs[2, 0].plot(t, windowed_signal, linestyle=":", color='blue')
axs[2, 0].set_title("Windowed Signal (Time Domain)")
axs[2, 0].set_xlabel("Time")
axs[2, 0].set_ylabel("$s$")
axs[2, 0].set_xlim(min(t), max(t))

axs[2, 1].plot(freq, np.abs(fft_windowed_signal), linestyle=":", color='red')
axs[2, 1].set_title("Windowed Signal (Frequency Domain)")
axs[2, 1].set_xlabel("Frequency")
axs[2, 1].set_ylabel(r"$|F(s)|$")
axs[2, 1].set_xlim(min(freq), max(freq))
axs[2, 1].set_yscale('log')

axs[0, 0].tick_params(axis='both',which='both', direction='in')
axs[1, 0].tick_params(axis='both',which='both', direction='in')
axs[2, 0].tick_params(axis='both',which='both', direction='in')
axs[0, 1].tick_params(axis='both',which='both', direction='in')
axs[1, 1].tick_params(axis='both',which='both', direction='in')
axs[2, 1].tick_params(axis='both',which='both', direction='in')



# Get the full path of the script
script_full_path = __file__

# Get the script name with extension
script_name_with_extension = os.path.basename(script_full_path)

# Remove the extension to get just the script name
script_name, _ = os.path.splitext(script_name_with_extension)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.savefig("fig__"+script_name+".png", format='png', bbox_inches='tight')
plt.show()

