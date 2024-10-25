import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
def analyze_data():
    data = pd.read_csv('/Users/raiyanwasihrid/AI-Talent-Concentration-Analysis/Beta-AI-Data-Analysis/AI-Concentration-Analysis/data/cleaned_data.csv')

    #Set the AI talent concentration target (2%)
    target_concentration = 0.02  # 2%

    # Function to calculate the yearly growth rate
    def calculate_growth_rate(country_data):
        # Only calculate the rate between consecutive years where data exists
        country_data = country_data.sort_values('Year')
        country_data['growth_rate'] = country_data['AI talent concentration'].pct_change()
        return country_data['growth_rate'].mean()

    # Function to estimate the year of reaching 2% concentration
    def project_year_to_2_percent(country, gender, data):
        country_gender_data = data[(data['Geographic area'] == country) & (data['Gender'] == gender)]
    
        # Calculate average growth rate
        growth_rate = calculate_growth_rate(country_gender_data)
    
        # Start from the latest available data point
        last_year = country_gender_data['Year'].max()
        last_concentration = country_gender_data[country_gender_data['Year'] == last_year]['AI talent concentration'].values[0]
    
        # If the concentration is already above 2%, return the current year
        if last_concentration >= target_concentration:
            return last_year
    
        # Project year by year until we reach the target concentration
        projected_year = last_year
        projected_concentration = last_concentration
    
        while projected_concentration < target_concentration:
            projected_year += 1
            projected_concentration *= (1 + growth_rate)
    
        return projected_year

# Project the year for each country and gender
    countries = data['Geographic area'].unique()
    projections = []

    for country in countries:
        male_year = project_year_to_2_percent(country, 'Male', data)
        female_year = project_year_to_2_percent(country, 'Female', data)
        projections.append((country, male_year, female_year))
    
    
# Save the projections to a CSV or pass directly to the next step
    projections_df = pd.DataFrame(projections, columns=['Country', 'Male_Year', 'Female_Year'])
    projections_df.to_csv('/Users/raiyanwasihrid/AI-Talent-Concentration-Analysis/Beta-AI-Data-Analysis/AI-Concentration-Analysis/data/projections.csv', index=False)
    print("Projections saved to data/projections.csv")
    
if __name__ == "__main__":
    analyze_data()
