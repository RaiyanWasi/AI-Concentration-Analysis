import pandas as pd

def clean_data():
# Load the dataset
    data = pd.read_csv('/Users/raiyanwasihrid/AI-Talent-Concentration-Analysis/Beta-AI-Data-Analysis/AI-Concentration-Analysis/data/fig_4.2.18.csv')

# Convert 'AI talent concentration' to float
    data['AI talent concentration'] = data['AI talent concentration'].str.rstrip('%').astype('float') / 100.0
    
# Save the cleaned data
    cleaned_data_path = '/Users/raiyanwasihrid/AI-Talent-Concentration-Analysis/Beta-AI-Data-Analysis/AI-Concentration-Analysis/data/cleaned_data.csv'
    data.to_csv(cleaned_data_path, index=False)
    print(f"Data cleaned and saved to{cleaned_data_path}")

# Check for missing values
    print(data.isnull().sum())
    print(data.head())
    
if __name__ =="__main__":
    clean_data()
