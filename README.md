# Data Analytics Seminar

This repository holds the code for the Data Analytics Seminar project. The main research question was: *To what extent have model updates in publicly available Generative AI Large Language Models (LLMs) improved the detection of hate speech related to sexism?*

## Structure

Explains the structure of the repository.

### Data

- **raw**: This folder contains all the original data files used in the project.
- **preprocessed**: This folder contains all the data files that have been preprocessed and are ready for analysis. It has the following format `text,SEXISM` where `SEXISM` is either `0` or `1`
- **result**: This folder contains all the results obtained from the LLMs.

### LLM

- contains all api calls to the LLMs used in the project.

### Plots

- contains plots generated from the analysis

### Main

- **evaluation.ipynb**: This notebook evaluates the results. It contains the code for calculating the confusoin matrix, evaluation metrics, word statistics and the contingnecy test. It also generatres the plots.
- **main.ipynb**: This notebook contains the code for prompting the LLMs and populating the data table.
- **preprocess.py**: This script preprocesses the data, converting it into the required format for analysis.
