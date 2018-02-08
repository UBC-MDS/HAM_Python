# HAM_Python

Handle All Missing (Values) 

*Feb 8th, 2018*



## Project contributors:

1. Duong Vu
2. Jordan Dubchak
3. Linsey Yao



## Introduction

Our package intends to explore the pattern of missing values in users' dataset and also imputes the missing values using several methods. 

We decided to make this project because we have not found any package that handle both tasks in either R or Python. In R, we found *Amelia* and *vis_dat* package that only visualize the missing data and in Python we found *fancyimpute* that deals with missing value but does not have any visualization. We thought this would be better package for users who do not have much experience in data wrangling.



## Functions 

Currently, our package only handles continuous features.

- Exploratory Function: use ggplot2/matplotlib/seaborn to plot patterns or proportions of missing values in the dataset:
  - `function1()`: possibly heatmap -  whole dataset to give an overview of the situation
    - Argument: 
      - dataset
      - color
  - `function2()`: density/ bar (vizmis): single variable to dig deeper.
    - Argument: 
      - dataset
      - feature (if not specified, plot all missing value feature)
      - color
- `Function3()`: Impute the missing value (para:  method (CC, Imputation, KNN imputation, ....))
  - Input: dataset with missing values
  - Function:
    - Handle missing values of all features using specified method
    - Argument:
      - dataset (if user don't want to impute the whole dataset, they will have to subset upfront)
      - method
  - Output: dataset with no missing values
- `Function4()`: Compare summary statistics between various imputation methods
  - Function:
    - Arguments: 
      - Input:  Original dataset containing missing values 
      - Methods that users want to compare
      - Output: A summary table.
    - Call the above function for several methods
    - Compare the summary statistics of what being imputed in the data using several available methods above


