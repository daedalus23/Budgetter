import pandas as pd
import json

# Load the CSV files
checking_df = pd.read_csv(r'.\statement\Checking.csv')
credit_df = pd.read_csv(r'.\statement\Credit.csv')
categories_df = pd.read_csv(r'.\statement\Categories.csv')

# Load keywords from JSON file
with open(r'.\bin\keywords.json', 'r') as file:
    keywords = json.load(file)

# Define the categorization rules
def categorize_transaction(description):
    for category, keys in keywords.items():
        for key in keys:
            if key.lower() in description.lower():
                return category
    return 'Uncategorized'  # Default category if no keywords match


# Apply the categorization function with user input
checking_df['Category'] = checking_df['Description'].apply(categorize_transaction)
credit_df['Category'] = credit_df['Description'].apply(categorize_transaction)

# Merge with the categories dataframe to get the Group and Type
checking_df = checking_df.merge(categories_df, on='Category', how='left')
credit_df = credit_df.merge(categories_df, on='Category', how='left')

# Save the categorized data to new CSV files
checking_df.to_csv('Categorized_Checking.csv', index=False)
credit_df.to_csv('Categorized_Credit.csv', index=False)
