# Amino Acid Hydrophobicity vs IDP Propensity Plot

This repository contains tools to create scatter plots visualizing the relationship between amino acid hydrophobicity and IDP (Intrinsically Disordered Protein) propensity, using amino acid one-letter codes as the markers.

## Features

- Scatter plot with amino acid letters as markers
- Color-coded version based on hydrophobicity
- Both command-line script and Jupyter notebook versions
- Example data included

## Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Option 1: Command-line Script

```bash
python plot_amino_acids.py your_data.csv
```

With custom column names:

```bash
python plot_amino_acids.py your_data.csv \
  --hydrophobicity hydro_column \
  --idp idp_column \
  --aa aa_column \
  --output my_plot.png
```

### Option 2: Jupyter Notebook

Open and run the interactive notebook:

```bash
jupyter notebook plot_notebook.ipynb
```

### Option 3: Python Script

Run the example:

```bash
python plot_amino_acids.py example_data.csv
```

## Data Format

Your CSV file should contain three columns:

- Amino acid one-letter codes (e.g., A, C, D, E, ...)
- Hydrophobicity values
- IDP propensity values

Example (`example_data.csv`):

```csv
amino_acid,hydrophobicity,IDP_propensity
A,1.8,0.06
C,2.5,-1.00
D,-3.5,0.192
...
```

## Customization

You can customize:

- Figure size
- Font sizes
- Marker colors and styles
- Grid appearance
- Output resolution (DPI)

See the notebook for examples of different styling options.

## Output

The scripts generate high-resolution PNG images (300 DPI) showing:

1. Standard version with light blue circular markers
2. Color-coded version where marker color reflects hydrophobicity

## Example Output

The plot displays:
- **X-axis**: Hydrophobicity
- **Y-axis**: IDP Propensity
- **Markers**: Amino acid one-letter codes (A, C, D, E, F, etc.)

Each amino acid is displayed as a letter within a circular marker, making it easy to identify which amino acid corresponds to each data point.
