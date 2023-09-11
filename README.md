# IDS706-Week_1_Mini-project

[![Python CI](https://github.com/udyansachdev1/IDS706-Week_1_Mini-project/actions/workflows/main.yml/badge.svg)](https://github.com/udyansachdev1/IDS706-Week_1_Mini-project/actions/workflows/main.yml)

### Creating  a Python GitHub template

## Overview

Creating a Python GitHub template that will be used in my future projects.


## Code Description

1. calc.py.py - This python file contains 3 function to multiply, subtract and add.
2. test_calc.py - This python file contains a test function and asserts the true value.


## CI/CD Automation files

1. requirements.txt - Contains all the required python packages
2. Makfefile - Using make to automate different parts of developing a Python project, like -
   
       1. running tests
       2. cleaning builds
       3. installing dependencies
   
   Integrating it into my routine, so can save time and avoid errors.
   
5. .github/workflows - This directory in a Python project (or any GitHub repository) is used for creating and storing GitHub Actions workflows. GitHub Actions is a continuous integration and continuous delivery                           (CI/CD) platform provided by GitHub. The workflow is triggered on pushes to the main branch. It sets up :
   
       1. Python environment
       2. Installs project dependencies
       3. Install packages
       4. Linitng
       5. Runs tests
       6. Format
