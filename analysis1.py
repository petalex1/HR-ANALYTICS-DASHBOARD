import pandas as pd


df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')


columns_to_keep = [
    'EmployeeNumber', 'Department', 'JobRole', 
    'MonthlyIncome', 'PerformanceRating', 'Attrition',
    'JobLevel'
]
df_clean = df[columns_to_keep].copy()


df_clean['Cost_Per_Performance_Point'] = round(df_clean['MonthlyIncome'] / df_clean['PerformanceRating'], 2)


df_clean.to_csv('HR_Data_Ready_For_PowerBI.csv', index=False)

print("Τα δεδομένα καθαρίστηκαν και το νέο αρχείο είναι έτοιμο!")