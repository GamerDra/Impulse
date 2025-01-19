
import numpy as np

# Load the uploaded .npy file
file_path = r'C:\Users\RUDRA\Downloads\generation\lsgan\synthetic_eeg_1.npy'
data = np.load(file_path)


# Inspect the shape of the loaded data
print(data.shape)


num_channels = 19
num_points_per_channel = 500
# Calculate the number of samples
num_samples = data.size // (num_channels * num_points_per_channel)

print(f"Number of samples: {num_samples}")

reshaped_data = data.reshape(num_samples, num_channels, num_points_per_channel)

# Verify the new shape
reshaped_data.shape


import matplotlib.pyplot as plt

# Specify the sample index you want to plot (e.g., 0 for the first sample)
sample_idx = 5

# Plot the data for each channel of the specified sample
fig, axes = plt.subplots(nrows=19, ncols=1, figsize=(12, 20), sharex=True)

for channel_idx in range(num_channels):
    # Extract data for the specific sample and channel
    channel_data = reshaped_data[sample_idx, channel_idx, :]
    axes[channel_idx].plot(channel_data, label=f'Channel {channel_idx + 1}')
    axes[channel_idx].legend(loc='upper right')
    axes[channel_idx].set_ylabel('Amplitude')

axes[-1].set_xlabel('Data Points')
plt.tight_layout()
plt.show()
