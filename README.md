# bikeshare

This project explores data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington.The data for this project provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States.

## Contents

1. bikeshare.py
    * Python file that outputs the results of analysis.
2. data
    * chicago.csv
    * new_york_city.csv
    * washington.csv
3. environment.yaml
    * environment file for this project

## Installation
please follow below instruction to create this project environment on your local desktop.
- download the project folder from the github url
     ```
    git clone https://github.com/shilpamadini/bikeshare.git
    ```
- install the conda environment using the environment file. this will create a conda environment with the same name listed in the environment file. this will also install all the required packages for this project
    ```
    conda env create -f environment.yaml
    ```
    - list the conda environments
     ```
     conda env list
     ```
    - activate the enviroment for bikeshare
     ```
     source activate dand_py3
     ```

## Functionality

The bikeshare.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:
    * Would you like to see data for Chicago, New York, or Washington?
    * Would you like to filter the data by month, day, or not at all?
    * (If they chose month) Which month - January, February, March, April, May, or  June?
    * (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?
The answers to the questions above will determine the city and timeframe on which data will be selected for analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.
