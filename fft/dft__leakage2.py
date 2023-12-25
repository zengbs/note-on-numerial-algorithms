import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft


# Creating a 3x2 subplot structure
fig, axs = plt.subplots(5, 2, figsize=(12, 16))
#plt.subplots_adjust(hspace=10, wspace=10)

# Sample rate and duration
N = 8.0/32  # Hz
tmax = +4
tmin = -4
t = np.arange(tmin, tmax, N)  # time vector

# Frequency vector for plotting
freq = np.linspace(0, N, len(t))



# Original signal
f = 0.5  # frequency in Hz
original_signal = np.cos(2 * np.pi * f * t)

# Perform Discrete Fourier Transform (DFT)
fft_original = fft(original_signal)

# Plotting the original signal in time and frequency domain
axs[0, 0].plot(t, original_signal, linestyle="-", color='blue', marker='o', label='line with marker', ms=3)
axs[0, 0].set_title(r"Time Domain ($f=1/2$)")
axs[0, 0].set_ylabel("$s$")
axs[0, 0].set_xlim(tmin, tmax)

axs[0, 1].plot(freq, np.abs(fft_original), linestyle="-", color='red', marker='o', label='line with marker', ms=3)
axs[0, 1].set_title(r"Frequency Domain ($f=1/2$)")
axs[0, 1].set_ylabel(r"$|F(s)|$")
axs[0, 1].set_xlim(min(freq), max(freq))
axs[0, 1].set_yscale('log')

# Original signal
f = 17/32
original_signal = np.cos(2 * np.pi * f * t)

# Perform Discrete Fourier Transform (DFT)
fft_original = fft(original_signal)

# Plotting the the signal in time and frequency domain
axs[1, 0].plot(t, original_signal, linestyle="-", color='blue', marker='o', label='line with marker', ms=3)
axs[1, 0].set_title(r"Time Domain ($f=17/32$)")
axs[1, 0].set_ylabel("$s$")
axs[1, 0].set_xlim(tmin, tmax)

axs[1, 1].plot(freq, np.abs(fft_original), linestyle="-", color='red', marker='o', label='line with marker', ms=3)
axs[1, 1].set_title(r"Frequency Domain ($f=17/32$)")
axs[1, 1].set_ylabel(r"$|F(s)|$")
axs[1, 1].set_xlim(min(freq), max(freq))
axs[1, 1].set_yscale('log')


# Original signal
f = 18/32
original_signal = np.cos(2 * np.pi * f * t)

# Perform Discrete Fourier Transform (DFT)
fft_original = fft(original_signal)

# Plotting the windowed signal in time and frequency domain
axs[2, 0].plot(t, original_signal, linestyle="-", color='blue', marker='o', label='line with marker', ms=3)
axs[2, 0].set_title(r"Time Domain ($f=18/32$)")
axs[2, 0].set_ylabel("$s$")
axs[2, 0].set_xlim(tmin, tmax)

axs[2, 1].plot(freq, np.abs(fft_original), linestyle="-", color='red', marker='o', label='line with marker', ms=3)
axs[2, 1].set_title(r"Frequency Domain ($f=18/32$)")
axs[2, 1].set_ylabel(r"$|F(s)|$")
axs[2, 1].set_xlim(min(freq), max(freq))
axs[2, 1].set_yscale('log')


# Original signal
f = 19/32
original_signal = np.cos(2 * np.pi * f * t)

# Perform Discrete Fourier Transform (DFT)
fft_original = fft(original_signal)

# Plotting the windowed signal in time and frequency domain
axs[3, 0].plot(t, original_signal, linestyle="-", color='blue', marker='o', label='line with marker', ms=3)
axs[3, 0].set_title(r"Time Domain ($f=19/32$)")
axs[3, 0].set_ylabel("$s$")
axs[3, 0].set_xlim(tmin, tmax)

axs[3, 1].plot(freq, np.abs(fft_original), linestyle="-", color='red', marker='o', label='line with marker', ms=3)
axs[3, 1].set_title(r"Frequency Domain ($f=19/32$)")
axs[3, 1].set_ylabel(r"$|F(s)|$")
axs[3, 1].set_xlim(min(freq), max(freq))
axs[3, 1].set_yscale('log')


# Original signal
f = 20/32
original_signal = np.cos(2 * np.pi * f * t)

# Perform Discrete Fourier Transform (DFT)
fft_original = fft(original_signal)

# Plotting the windowed signal in time and frequency domain
axs[4, 0].plot(t, original_signal, linestyle="-", color='blue', marker='o', label='line with marker', ms=3)
axs[4, 0].set_title(r"Time Domain ($f=20/32$)")
axs[4, 0].set_xlabel("Time")
axs[4, 0].set_ylabel("$s$")
axs[4, 0].set_xlim(tmin, tmax)

axs[4, 1].plot(freq, np.abs(fft_original), linestyle="-", color='red', marker='o', label='line with marker', ms=3)
axs[4, 1].set_xlabel("Frequency ($f=20/32$)")
axs[4, 1].set_ylabel(r"$|F(s)|$")
axs[4, 1].set_xlim(min(freq), max(freq))
axs[4, 1].set_yscale('log')

axs[0, 0].tick_params(axis='both',which='both', direction='in')
axs[1, 0].tick_params(axis='both',which='both', direction='in')
axs[2, 0].tick_params(axis='both',which='both', direction='in')
axs[3, 0].tick_params(axis='both',which='both', direction='in')
axs[4, 0].tick_params(axis='both',which='both', direction='in')
axs[0, 1].tick_params(axis='both',which='both', direction='in')
axs[1, 1].tick_params(axis='both',which='both', direction='in')
axs[2, 1].tick_params(axis='both',which='both', direction='in')
axs[3, 1].tick_params(axis='both',which='both', direction='in')
axs[4, 1].tick_params(axis='both',which='both', direction='in')



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

