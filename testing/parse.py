# import pandas as pd
#
# # Load the CSV files
# checking_df = pd.read_csv(r'.\statement\Checking.csv')
# credit_df = pd.read_csv(r'.\statement\Credit.csv')
# categories_df = pd.read_csv(r'.\statement\Categories.csv')
#
#
# # Define the categorization rules
# def categorize_transaction(description):
#     # Define keywords for each category
#     keywords = {
#         'Savings': ['Transfer To Credit Card'],
#         'Other Debts': ['AMZN Mktp', '7-ELEVEN', 'ROSS STORES', 'TJMAXX', 'THE HOME DEPOT', 'BEST BUY', 'GREAT CLIPS', 'GOODWILL', 'OFFICE DEPOT', 'TARGET', 'FINAL SWITCHBACK', 'FEDEX'],
#         'Charity/Donations': [],
#         'Paychecks': ['PAYROLL', 'REWARD REDEMPTION', 'CREDIT CARD CASH ADVANCE', 'Deposit - EVATEC NA, INC.', 'Deposit - VAED TREAS 310', 'Deposit - HUMAN SERVICES'],
#         'Bills': ['TMOBILE', 'ZIPLY FIBER', 'PORTLAND GENERAL ELECTRIC'],
#         'Rent/Mortgage': ['Pallas Apartment Home'],
#         'Groceries': ['FRED-MEYER', 'NEW SEASONS', 'WINCO'],
#         'Other Obligations': ['IN N OUT', 'ATM Withdrawal'],
#         'Credit Card Payments': ['Transfer to Credit Card', 'AMEX EPAYMENT', 'MOB PAYMENT RECEIVED'],
#         'Fun/Entertainment': ['SPOTIFY', 'APPLE.COM/BILL', 'AMC', 'FANDANGO', 'TOP GOLF'],
#         'Restaurants': ["NOODLE HOUSE", 'PF CHANGS', 'NIKKI SUSHI', 'INTEL RA4 CAFE'],
#         'Other Wants': ['SALT & STRAW', 'IPSY GLAM BAG', '76', 'SQ *OREGON BEVERAGE', 'Voodoo Doughnut', '365 Market', 'NikePOS_US', 'FRIENDS OF THE HILLSBORO', 'Amazon.com'],
#         'Fast Food': ['OLO VG', 'CHICK-FIL-A', 'BURGER KING', 'KFC', 'THE MOCKING BIRD'],
#         'Gas': ['FRED M FUEL'],
#         'Animals': ['CHEWY.COM', 'PETCO', 'PETSMART'],
#         'Insurance': ['GEICO'],
#         'Credit Card Interest': ['INTEREST CHARGE'],
#         'Auto Payment': ['JPMorgan Chase', 'TOYOTA FINANCIAL RETAIL'],
#         'Software Sub': ['PwP CHATGPT SUB', 'SYMBOLAB.COM', 'Prime Video Channels', 'CHEGG ORDER', 'FLATLY', 'AMCREST', 'CLOUDFLARE', 'Amazon Prime', 'YouTubePremium', 'MATHWAY']
#     }
#
#     for category, keys in keywords.items():
#         for key in keys:
#             if key.lower() in description.lower():
#                 return category
#     return 'Uncategorized'  # Default category if no keywords match
#
#
# # Apply the categorization function
# checking_df['Category'] = checking_df['Description'].apply(categorize_transaction)
# credit_df['Category'] = credit_df['Description'].apply(categorize_transaction)
#
# # Merge with the categories dataframe to get the Group and Type
# checking_df = checking_df.merge(categories_df, on='Category', how='left')
# credit_df = credit_df.merge(categories_df, on='Category', how='left')
#
# # Save the categorized data to new CSV files
# checking_df.to_csv('Categorized_Checking.csv', index=False)
# credit_df.to_csv('Categorized_Credit.csv', index=False)
