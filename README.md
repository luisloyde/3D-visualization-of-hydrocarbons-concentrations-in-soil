# README
## 3D visualization of hydrocarbons concentrations in soil
### Overview

This project allows the analysis and visualization of soil hydrocarbon concentrations using point data with UTM coordinates and depth. 3D interpolation techniques generate a detailed visualization of affected areas, and key metrics such as the volume of contaminated soil and the maximum depth of contamination are calculated.

## Features

- Load data from an Excel file with UTM coordinates and hydrocarbon concentrations.
- Perform 3D interpolation of data points (X, Y, Z).
- Generate interactive 3D visualizations of hydrocarbon concentration.
- Calculate the volume of soil exceeding a defined concentration threshold.
- Determine the maximum depth of contaminated areas.

## System Requirements

- Python 3.8 or later
- Required libraries:
  - `numpy`
  - `pandas`
  - `scipy`
  - `matplotlib`
  - `plotly`
- Input data in `.xlsx` format with the following columns:
  - `UTM_E` (UTM Easting coordinate)
  - `UTM_N` (UTM Northing coordinate)
  - `Depth` (Z-coordinate)
  - `Concentration` (Hydrocarbon concentration)

## Examples
![volumetric_visualization](https://github.com/user-attachments/assets/d81ff462-9a6f-41fb-9d40-bb980daf259d)

![polluted_visualization](https://github.com/user-attachments/assets/c05d5f7a-de61-4741-861f-2464c1d22c66)
