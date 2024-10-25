import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def visualize_data():
    # Load the projections from CSV
    projections = pd.read_csv('/Users/raiyanwasihrid/AI-Talent-Concentration-Analysis/Beta-AI-Data-Analysis/AI-Concentration-Analysis/data/projections.csv')
    
    countries = projections['Country'].values
    male_years = projections['Male_Year'].values
    female_years = projections['Female_Year'].values
    
    # Convert to Numpy arrays for manipulation 
    ind = np.arange(len(countries)) # the x locations for the groups
    width = 0.35      # the width of the bars
    
    #Create the plot
    fig, ax = plt.subplots(figsize=(15, 8))
    
    #Plot male data with offset 
    bars1 = ax.barh(ind - width/2, male_years, width, color='blue', label='Male')
    
    #Plot female data with offset  
    bars2 = ax.barh(ind + width/2, female_years, width, color='pink', label='Female') 
    
    # Add some labels and title
    ax.set_xlabel('Year')
    ax.set_title('Projected Year to reach 2% AI Talent Concentration')
    ax.set_yticks(ind)
    ax.set_yticklabels(countries)
    ax.legend(loc='upper right', bbox_to_anchor=(1,1))
    
    # Set the x-axis limit and increments 
    ax.set_xlim(2015, 2090)
    ax.set_xticks(np.arange(2015, 2091, 5))
    
    #Show the plot
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    visualize_data()