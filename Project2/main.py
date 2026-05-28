# ==========================================
# DATA CLEANING + EXPLORATORY DATA ANALYSIS
# DecodeLabs Internship Project
# ==========================================

# ==========================================
# STEP 1 : IMPORT LIBRARIES
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# STEP 2 : LOAD DATASET
# ==========================================

file_path = "Dataset for Data Analytics.xlsx"

df = pd.read_excel(file_path)

print("DATASET LOADED SUCCESSFULLY")

# ==========================================
# STEP 3 : DISPLAY DATASET INFORMATION
# ==========================================

print("\n===================================")
print("FIRST 5 ROWS OF DATASET")
print("===================================")

print(df.head())

print("\n===================================")
print("DATASET SHAPE")
print("===================================")

print(df.shape)

print("\n===================================")
print("COLUMN NAMES")
print("===================================")

print(df.columns)

print("\n===================================")
print("DATASET INFORMATION")
print("===================================")

print(df.info())

# ==========================================
# TASK 1 : DATA CLEANING
# ==========================================

print("\n===================================")
print("TASK 1 : DATA CLEANING")
print("===================================")

# ==========================================
# IDENTIFY MISSING VALUES
# ==========================================

print("\nMISSING VALUES BEFORE CLEANING")

print(df.isnull().sum())

# ==========================================
# HANDLE MISSING VALUES
# ==========================================

# Numerical Columns
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

for col in numerical_columns:
    df[col].fillna(df[col].median(), inplace=True)

# Categorical Columns
categorical_columns = df.select_dtypes(include=['object']).columns

for col in categorical_columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\nMISSING VALUES AFTER CLEANING")

print(df.isnull().sum())

# ==========================================
# REMOVE DUPLICATES
# ==========================================

print("\nCHECKING DUPLICATE RECORDS")

duplicates = df.duplicated().sum()

print("NUMBER OF DUPLICATES :", duplicates)

df = df.drop_duplicates()

print("DUPLICATES REMOVED SUCCESSFULLY")

# ==========================================
# CORRECT DATA FORMATS
# ==========================================

print("\nCORRECTING DATA FORMATS")

# Convert Date Column
df['Date'] = pd.to_datetime(df['Date'])

# Convert Text Columns
for col in categorical_columns:
    df[col] = df[col].astype(str)

print("\nUPDATED DATA TYPES")

print(df.dtypes)

# ==========================================
# SAVE CLEANED DATASET
# ==========================================

cleaned_file_name = "Cleaned_Data_Analytics_Dataset.xlsx"

df.to_excel(cleaned_file_name, index=False)

print("\nCLEANED DATASET SAVED SUCCESSFULLY")

print("FILE NAME :", cleaned_file_name)

# ==========================================
# TASK 2 : EXPLORATORY DATA ANALYSIS
# ==========================================

print("\n===================================")
print("TASK 2 : EXPLORATORY DATA ANALYSIS")
print("===================================")

# ==========================================
# BASIC STATISTICS
# ==========================================

print("\nBASIC STATISTICS")

print(df.describe())

# ==========================================
# TOTAL PRICE ANALYSIS
# ==========================================

print("\n===================================")
print("TOTAL PRICE ANALYSIS")
print("===================================")

mean_price = df['TotalPrice'].mean()
median_price = df['TotalPrice'].median()
max_price = df['TotalPrice'].max()
min_price = df['TotalPrice'].min()

print("MEAN TOTAL PRICE :", mean_price)
print("MEDIAN TOTAL PRICE :", median_price)
print("MAXIMUM TOTAL PRICE :", max_price)
print("MINIMUM TOTAL PRICE :", min_price)

# ==========================================
# PRODUCT REVENUE ANALYSIS
# ==========================================

print("\n===================================")
print("PRODUCT REVENUE ANALYSIS")
print("===================================")

product_revenue = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False)

print(product_revenue)

# Bar Chart
plt.figure(figsize=(10,5))

product_revenue.plot(kind='bar')

plt.title("Product Revenue Analysis")
plt.xlabel("Products")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.show()

# ==========================================
# ORDER STATUS ANALYSIS
# ==========================================

print("\n===================================")
print("ORDER STATUS ANALYSIS")
print("===================================")

status_count = df['OrderStatus'].value_counts()

print(status_count)

# Pie Chart
plt.figure(figsize=(7,7))

status_count.plot(kind='pie', autopct='%1.1f%%')

plt.title("Order Status Distribution")

plt.ylabel("")

plt.show()

# ==========================================
# PAYMENT METHOD ANALYSIS
# ==========================================

print("\n===================================")
print("PAYMENT METHOD ANALYSIS")
print("===================================")

payment_count = df['PaymentMethod'].value_counts()

print(payment_count)

# Bar Chart
plt.figure(figsize=(8,5))

payment_count.plot(kind='bar')

plt.title("Payment Method Usage")
plt.xlabel("Payment Method")
plt.ylabel("Count")

plt.xticks(rotation=0)

plt.show()

# ==========================================
# REFERRAL SOURCE ANALYSIS
# ==========================================

print("\n===================================")
print("REFERRAL SOURCE ANALYSIS")
print("===================================")

referral_count = df['ReferralSource'].value_counts()

print(referral_count)

# Bar Chart
plt.figure(figsize=(8,5))

referral_count.plot(kind='bar')

plt.title("Referral Source Analysis")
plt.xlabel("Referral Source")
plt.ylabel("Count")

plt.xticks(rotation=0)

plt.show()

# ==========================================
# MONTHLY SALES TREND
# ==========================================

print("\n===================================")
print("MONTHLY SALES TREND")
print("===================================")

# Create Month-Year Column
df['MonthYear'] = df['Date'].dt.to_period('M')

monthly_sales = df.groupby('MonthYear')['TotalPrice'].sum()

print(monthly_sales)

# Line Chart
plt.figure(figsize=(12,5))

monthly_sales.plot(kind='line', marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.grid(True)

plt.show()

# ==========================================
# OUTLIER DETECTION
# ==========================================

print("\n===================================")
print("OUTLIER DETECTION")
print("===================================")

Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df['TotalPrice'] < lower_limit) |
    (df['TotalPrice'] > upper_limit)
]

print("NUMBER OF OUTLIERS :", len(outliers))

print("\nOUTLIER RECORDS")

print(outliers)

# Box Plot
plt.figure(figsize=(8,5))

plt.boxplot(df['TotalPrice'])

plt.title("Outlier Detection - Total Price")
plt.ylabel("Total Price")

plt.show()

# ==========================================
# FINAL OBSERVATIONS
# ==========================================

print("\n===================================")
print("FINAL OBSERVATIONS")
print("===================================")

print("""
1. Missing values were identified and handled successfully.

2. Duplicate rows were removed from the dataset.

3. Data formats such as dates and text columns were corrected.

4. Product revenue analysis shows which products perform best.

5. Online payment methods are widely used.

6. Sales trends vary month-wise.

7. Several outliers were detected in TotalPrice.

8. Referral sources like Instagram and Email contribute strongly.
""")

print("\nPROJECT COMPLETED SUCCESSFULLY")

