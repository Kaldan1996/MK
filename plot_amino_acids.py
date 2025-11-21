#!/usr/bin/env python3
"""
Plot amino acid hydrophobicity vs IDP propensity
with amino acid one-letter codes as scatter plot markers
"""

import matplotlib.pyplot as plt
import pandas as pd
import argparse


def plot_amino_acid_properties(data_file=None, hydrophobicity_col='hydrophobicity',
                                idp_col='IDP_propensity', aa_col='amino_acid',
                                output_file='amino_acid_plot.png', figsize=(12, 8),
                                title='Amino Acid Hydrophobicity vs IDP Propensity'):
    """
    Create a scatter plot with amino acid letters as markers

    Parameters:
    -----------
    data_file : str
        Path to CSV file containing the data
    hydrophobicity_col : str
        Name of the column containing hydrophobicity values
    idp_col : str
        Name of the column containing IDP propensity values
    aa_col : str
        Name of the column containing amino acid one-letter codes
    output_file : str
        Name of the output image file
    figsize : tuple
        Figure size (width, height)
    title : str
        Plot title
    """

    # Load data
    if data_file:
        df = pd.read_csv(data_file)
    else:
        # Example data - replace with your actual data
        print("No data file provided. Using example data.")
        print("To use your data, provide a CSV file with columns for hydrophobicity, IDP propensity, and amino acid codes.")
        return

    # Extract data
    x = df[hydrophobicity_col].values
    y = df[idp_col].values
    labels = df[aa_col].values

    # Create figure and axis
    fig, ax = plt.subplots(figsize=figsize)

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
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)

    # Add grid for better readability
    ax.grid(True, alpha=0.3, linestyle='--')

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Save the plot
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Plot saved as {output_file}")

    # Show the plot
    plt.show()


def main():
    parser = argparse.ArgumentParser(
        description='Plot amino acid hydrophobicity vs IDP propensity'
    )
    parser.add_argument('data_file',
                       help='Path to CSV file containing amino acid data')
    parser.add_argument('--hydrophobicity', '-x', default='hydrophobicity',
                       help='Column name for hydrophobicity (default: hydrophobicity)')
    parser.add_argument('--idp', '-y', default='IDP_propensity',
                       help='Column name for IDP propensity (default: IDP_propensity)')
    parser.add_argument('--aa', '-a', default='amino_acid',
                       help='Column name for amino acid codes (default: amino_acid)')
    parser.add_argument('--output', '-o', default='amino_acid_plot.png',
                       help='Output file name (default: amino_acid_plot.png)')
    parser.add_argument('--title', '-t',
                       default='Amino Acid Hydrophobicity vs IDP Propensity',
                       help='Plot title')
    parser.add_argument('--figsize', nargs=2, type=float, default=[12, 8],
                       help='Figure size as width height (default: 12 8)')

    args = parser.parse_args()

    plot_amino_acid_properties(
        data_file=args.data_file,
        hydrophobicity_col=args.hydrophobicity,
        idp_col=args.idp,
        aa_col=args.aa,
        output_file=args.output,
        figsize=tuple(args.figsize),
        title=args.title
    )


if __name__ == '__main__':
    main()
