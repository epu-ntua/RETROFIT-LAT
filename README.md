# RETROFIT-LAT: A Comprehensive Dataset for Energy Efficiency Investments in Latvia

[![DOI](https://zenodo.org/badge/913311588.svg)](https://doi.org/10.5281/zenodo.14697230)

## Overview

This repository contains datasets and supporting scripts from the study **"RETROFIT-LAT: A Comprehensive Dataset for Energy Efficiency Investments in Latvia"**. It provides detailed information on residential building energy efficiency projects funded by the Latvian Environmental Investment Fund (LEIF). The data focuses on retrofitting and solar panel installations, offering insights into energy performance improvements and sustainability measures.

---

## Table of Contents
- [About the Dataset](#about-the-dataset)
- [Structure of the Repository](#structure-of-the-repository)
- [Key Features of the Dataset](#key-features-of-the-dataset)
  - [Building Retrofitting Data](#building-retrofitting-data)
  - [Solar Panel Installation Data](#solar-panel-installation-data)
- [Data Preprocessing and Privacy](#data-preprocessing-and-privacy)
- [Potential Applications](#potential-applications)
- [Limitations](#limitations)
- [Citation](#citation)
- [Acknowledgements](#acknowledgements)

---

## About the Dataset

The repository contains two primary datasets:
1. **EF_comp Dataset:** Focuses on building retrofitting, including energy performance, CO2 emissions, and energy-saving measures before and after renovations.
2. **Sol_pan_comp Dataset:** Details solar panel installations, including electricity consumption, energy production, and CO2 emissions reductions.

These datasets cover projects implemented from 1870 to 2022 across Latvia, providing a rich source for evaluating the impacts of energy-saving initiatives.

---

## Structure of the Repository

- `data/`
  - `EF_comp.csv`: Retrofitting data for buildings.
  - `Sol_pan_comp.csv`: Data on solar panel projects.
- `scripts/`
  - Python scripts for data preprocessing and analysis.
- `docs/`
  - Detailed documentation on dataset structure and feature descriptions.
- `README.md`: Overview of the repository.
- `LICENSE`: License information for the dataset and scripts.

---

## Key Features of the Dataset

### Building Retrofitting Data
The **EF_comp** dataset contains:
- **General building information**: Location, year of construction, and building size.
- **Energy performance**: Energy class, energy consumption, and CO2 emissions before and after retrofitting.
- **Structural details**: Floor height, number of floors, and insulation metrics.
- **Energy-saving measures**: Heat loss coefficients, energy-saving percentages, and compliance with almost zero energy standards.

### Solar Panel Installation Data
The **Sol_pan_comp** dataset includes:
- **Project details**: Year, region, and funding specifics.
- **Energy metrics**: Pre- and post-installation energy consumption, inverter capacity, and solar electricity production.
- **Environmental impact**: Reductions in primary energy use and CO2 emissions.

---

## Data Preprocessing and Privacy

To ensure privacy and comply with data protection standards:
- Personally identifiable information (PII) such as addresses and project numbers has been removed.
- Location data has been pseudo-anonymized (e.g., `town1`, `county1`).
- Specific dates have been generalized to the year level.

---

## Potential Applications

The datasets can be utilized for:
- Analyzing the impact of building renovations on energy efficiency and CO2 emissions.
- Evaluating the effectiveness of solar panel installations in reducing energy consumption.
- Identifying trends and patterns in energy efficiency across different building types and regions.
- Supporting policy development and decision-making in energy sustainability.

---

## Limitations

- The datasets are limited to 1,010 buildings, potentially affecting the generalizability of findings.
- Some features are underrepresented or incomplete, such as region-specific energy class distributions.

---

## Citation

If you use this dataset in your research, please cite this repository
