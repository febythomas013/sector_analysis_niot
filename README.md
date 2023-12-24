# Related Sectors Analysis

## Overview

This project performs an analysis of related sectors using Euclidean distance as a measure of dissimilarity. The goal is to identify sectors that exhibit similarity based on the provided input data.

## Files and Directories

- **code:** Contains the Python script for analyzing related sectors.
  - `niot_v1.ipynb`: Python script for analyzing related sectors based on Euclidean distance.

- **data:** Contains the input data and any intermediate datasets.
  - `NIOT_EventStudies.xlsx`: Input data used for the analysis. Have the NIOT values and the Coeffient of Relatedness Matrix.
  - `NIOT_V1`: Input data that only has the coefficient of Relatedness Matrix.
  - `Related_Sectors_Eucledian_V1.csv`: Excel file containing the results of the related sectors analysis.

## Getting Started

To run the analysis script, ensure you have Python installed and install the required dependencies:

```bash
pip install pandas scikit-learn seaborn numpy matplotlib.pyplot
