#!/bin/bash

# Step 1: Run the data cleaning script
echo "Running data_cleaning.py"
python3 ../data/data_cleaning.py

# Step 2: Run the analysis script
echo "Running beta_data_analysis.py"
python3 beta_data_analysis.py

# Step 3: Run the visualization script
echo "Running data_visualization.py"
python3 ../Visualization/data_visualization.py