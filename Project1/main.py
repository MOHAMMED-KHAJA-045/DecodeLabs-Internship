import pandas as pd #importing libraries

# Load the Dataset
df = pd.read_excel("Dataset for Data Analytics.xlsx")

# Check missing values 
print(df['CouponCode'].isnull().sum())

# Replace missing CouponCode values
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')

# Verify again
print(df['CouponCode'].isnull().sum())

# Save cleaned dataset
df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("Dataset cleaned successfully!")
