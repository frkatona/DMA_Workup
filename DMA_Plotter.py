import pandas as pd
import matplotlib.pyplot as plt
import re
import glob

# Initialize the figure
fig, ax1 = plt.subplots(figsize=(10, 7))
ax2 = ax1.twinx()

# Loop over all .txt files in the directory
for file_name in glob.glob('*.txt'):
    
    # Read the file with UTF-16 encoding
    with open(file_name, 'r', encoding='utf-16') as f:
        lines = f.readlines()

    # Extract the sample name
    sample_name = lines[12].split('\t')[1]

    # Define the column names
    columns = []
    for line in lines:
        if re.match(r'Sig\d', line.split('\t')[0]):
            columns.append(line.split('\t')[1][0:-1])

    # Create a DataFrame from the data, specifying the encoding
    data = pd.read_csv(file_name, names=columns, skiprows=65, delimiter='\t', encoding='utf-16')

    # Plot data
    ax1.plot(data['Time (min)'], data['Storage Modulus (MPa)'], label=f'{sample_name}: Storage Modulus')
    ax1.plot(data['Time (min)'], data['Loss Modulus (MPa)'], label=f'{sample_name}: Loss Modulus')
    ax2.plot(data['Time (min)'], data['Temperature (°C)'], label=f'{sample_name}: Temperature')

# Set labels
ax1.set_xlabel('Time (min)')
ax1.set_ylabel('Modulus (MPa)', color='b')
ax2.set_ylabel('Temperature (°C)', color='r')

# Set color for y tick labels
for tl in ax1.get_yticklabels():
    tl.set_color('b')
for tl in ax2.get_yticklabels():
    tl.set_color('r')

# Add a legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Add a title
plt.title('Data for all samples')
fig.tight_layout()
plt.show()
