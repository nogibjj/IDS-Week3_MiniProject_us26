# Polars Descriptive Statistics Script

 [![Python Polar CI](https://github.com/nogibjj/IDS-Week3_MiniProject_us26/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/IDS-Week3_MiniProject_us26/actions/workflows/main.yml)

<p align="center">
  <img width="650" src="https://pypi-camo.global.ssl.fastly.net/6ee1fcdd8ef06e75b8a1d0bedceaa9faad6c093a/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f706f6c612d72732f706f6c6172732d7374617469632f6d61737465722f6c6f676f732f706f6c6172735f6769746875625f6c6f676f5f726563745f6461726b5f6e616d652e737667" alt="My Image1">
</p>

Here is the reference link : [Link]([https://www.google.com](https://www.pola.rs))

## Overview

This repo has been created using my week 1 mini project as the template which has all the necessary steps to automate the process and I will be using that repo for my future projects as well. The current repo is for creating Polar Descriptive Statistics Script using DevOps principles.


## Code Description

1. polar_stats.py - This python file contains 3 function to calculate mean, median, mode and standard deviation
2. test_stats.py - This python file is reading World University Ranking.csv and testing the four functions in stats_descriptive.py and asserts the true value
3. Generated summary report.md - This is markdown file containing the output. The function create_summary is present in polar_stats.py file which creates this markdown file when we run 'make test' command
4. test_graphs.py - This file contains analysis between count of top universities vs there mean industry income score based on the location. When we run the 'make test' command, the folder named output_graph is created with the graph as shown below.

   The output of the visualization code is  :

<p align="center">
  <img width="650" src="https://github.com/nogibjj/IDS-Week3_MiniProject_us26/blob/main/output_graph/visualization.png" alt="My Image1">
</p>

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
