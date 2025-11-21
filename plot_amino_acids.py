import matplotlib.pyplot as plt
import pandas as pd

# Load your data - replace 'your_data.csv' with your actual file
df = pd.read_csv('your_data.csv')

# Specify your column names
hydrophobicity_col = 'hydrophobicity'
idp_col = 'IDP_propensity'
aa_col = 'amino_acid'

# Extract data
x = df[hydrophobicity_col].values
y = df[idp_col].values
labels = df[aa_col].values

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each amino acid as a text marker
for i in range(len(x)):
    ax.text(x[i], y[i], labels[i],
            ha='center', va='center',
            fontsize=12, fontweight='bold',
            bbox=dict(boxstyle='circle,pad=0.3',
                     facecolor='lightblue',
                     edgecolor='navy',
                     alpha=0.7))

# Set labels and title
ax.set_xlabel('Hydrophobicity', fontsize=14, fontweight='bold')
ax.set_ylabel('IDP Propensity', fontsize=14, fontweight='bold')
ax.set_title('Amino Acid Hydrophobicity vs IDP Propensity', fontsize=16, fontweight='bold', pad=20)

# Add grid for better readability
ax.grid(True, alpha=0.3, linestyle='--')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save and show the plot
plt.savefig('amino_acid_plot.png', dpi=300, bbox_inches='tight')
plt.show()
