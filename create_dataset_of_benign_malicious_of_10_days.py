import pandas as pd

# first day - bot and benign - 02-03-2018

# read file
df_friday1 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/03-02-2018.csv')

# drop rows label = wrong rows
df_friday1.drop(df_friday1.loc[df_friday1["Label"] == "Label"].index, inplace=True)

# turn protocol column to many protocol columns
df_friday1 = pd.get_dummies(df_friday1, columns=['Protocol'], drop_first=True)

# pop label column to last column
df_friday1.insert(len(df_friday1.columns)-1, 'Label', df_friday1.pop('Label'))

# drop unrelavant columns
columns_to_drop = [
    'Dst Port',
    'Timestamp',
    'Fwd PSH Flags',
    'Bwd PSH Flags',
    'Fwd URG Flags',
    'Bwd URG Flags',
    'Flow Byts/s',  # This field had np.inf values during training, as such was removed
    'Flow Pkts/s'  # This field had np.inf values during training, as such was removed
]

df_friday1.drop(columns=columns_to_drop, inplace=True)

# drop duplicate values
df_friday1.drop_duplicates(inplace=True)

# drop missing values
df_friday1 = df_friday1.dropna()

# take only 14310 bot and 6349 benign
mask_bot = (df_friday1["Label"] == "Bot") 
mask_benign = (df_friday1["Label"] == "Benign") 
df_friday1.loc[mask_bot] = df_friday1.loc[mask_bot].head(14310)
df_friday1.loc[mask_benign] = df_friday1.loc[mask_benign].head(6349)

# drop rows having nan value
df_friday1 = df_friday1.dropna()

# replace Bot attack label with value 1 and benign with value 0
df_friday1.replace(to_replace=['Bot'], value=1, inplace=True)
df_friday1.replace(to_replace="Benign", value=0, inplace=True)

print(df_friday1.info())

# check again number of benign and bot
print(df_friday1["Label"].value_counts()[[0]].sum())
print(df_friday1["Label"].value_counts()[[1]].sum())



# 2. second day - dos slowhttptest and dos hulk and benign - 02-16-2018



df_friday2 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-16-2018.csv', low_memory=False)

# drop rows label = wrong rows
df_friday2.drop(df_friday2.loc[df_friday2["Label"] == "Label"].index, inplace=True)

# turn protocol column to many protocol columns
df_friday2 = pd.get_dummies(df_friday2, columns=['Protocol'], drop_first=True)

# pop label column to last column
df_friday2.insert(len(df_friday2.columns)-1, 'Label', df_friday2.pop('Label'))

df_friday2.drop(columns=columns_to_drop, inplace=True)

# drop duplicate values
df_friday2.drop_duplicates(inplace=True)

# drop missing values
df_friday2 = df_friday2.dropna()

# take only 55 DoS attacks-SlowHTTPTest and 23334 DoS attacks-Hulk and 6349 benign
mask_dos_slowhttp = (df_friday2["Label"] == "DoS attacks-SlowHTTPTest") 
mask_dos_hulk = (df_friday2["Label"] == "DoS attacks-Hulk") 
mask_benign2 = (df_friday2["Label"] == "Benign") 

df_friday2.loc[mask_dos_slowhttp] = df_friday2.loc[mask_dos_slowhttp].head(55)
df_friday2.loc[mask_dos_hulk] = df_friday2.loc[mask_dos_hulk].head(23334)
df_friday2.loc[mask_benign2] = df_friday2.loc[mask_benign2].head(6349)

# drop rows having nan value
df_friday2 = df_friday2.dropna()

# replace Bot attack label with value 1 and benign with value 0
df_friday2.replace(to_replace=['DoS attacks-SlowHTTPTest'], value=2, inplace=True)
df_friday2.replace(to_replace="DoS attacks-Hulk", value=3, inplace=True)
df_friday2.replace(to_replace="Benign", value=0, inplace=True)

print(df_friday2.info())

# check again number of benign and dos slowhhtptest and dos hulk
print(df_friday2["Label"].value_counts()[[0]].sum())
print(df_friday2["Label"].value_counts()[[2]].sum())
print(df_friday2["Label"].value_counts()[[3]].sum())



# 3. third day - brute force web; brute force xss; sql injection and benign - 02-23-2018



df_friday3 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-23-2018.csv', low_memory=False)

# drop rows label = wrong rows
df_friday3.drop(df_friday3.loc[df_friday3["Label"] == "Label"].index, inplace=True)

# turn protocol column to many protocol columns
df_friday3 = pd.get_dummies(df_friday3, columns=['Protocol'], drop_first=True)

# pop label column to last column
df_friday3.insert(len(df_friday3.columns)-1, 'Label', df_friday3.pop('Label'))

df_friday3.drop(columns=columns_to_drop, inplace=True)

# drop duplicate values
df_friday3.drop_duplicates(inplace=True)

# drop missing values
df_friday3 = df_friday3.dropna()

# take only 342 Brute Force Web; 150 Brute Force XSS and 51 SQL Injection and 6349 benign
mask_bruteforce_web = (df_friday3["Label"] == "Brute Force -Web") 
mask_bruteforce_xss = (df_friday3["Label"] == "Brute Force -XSS") 
mask_sql_injection = (df_friday3["Label"] == "SQL Injection") 
mask_benign3 = (df_friday3["Label"] == "Benign") 

df_friday3.loc[mask_bruteforce_web] = df_friday3.loc[mask_bruteforce_web].head(342)
df_friday3.loc[mask_bruteforce_xss] = df_friday3.loc[mask_bruteforce_xss].head(150)
df_friday3.loc[mask_sql_injection] = df_friday3.loc[mask_sql_injection].head(51)
df_friday3.loc[mask_benign3] = df_friday3.loc[mask_benign3].head(6349)

print(df_friday3["Label"].value_counts()[['Brute Force -Web']].sum())
print(df_friday3["Label"].value_counts()[['Brute Force -XSS']].sum())
print(df_friday3["Label"].value_counts()[['SQL Injection']].sum())
print(df_friday3["Label"].value_counts()[['Benign']].sum())

# drop rows having nan value
df_friday3 = df_friday3.dropna()

# replace Brute Force -Web attack label with value 4; Brute Force -XSS with value 5; \
# SQL Injection with value 6 and benign with value 0
df_friday3.replace(to_replace=['Brute Force -Web'], value=4, inplace=True)
df_friday3.replace(to_replace=['Brute Force -XSS'], value=5, inplace=True)
df_friday3.replace(to_replace=['SQL Injection'], value=6, inplace=True)
df_friday3.replace(to_replace=['Benign'], value=0, inplace=True)

print(df_friday3.info())

# check again number of benign and dos slowhhtptest and dos hulk
print(df_friday3["Label"].value_counts()[[0]].sum())
print(df_friday3["Label"].value_counts()[[4]].sum())
print(df_friday3["Label"].value_counts()[[5]].sum())
print(df_friday3["Label"].value_counts()[[6]].sum())


# 4. forth day - brute force web; brute force xss; sql injection and benign - 02-20-2018


df_thursday1 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-20-2018.csv', low_memory=False)

# drop rows label = wrong rows
df_thursday1.drop(df_thursday1.loc[df_thursday1["Label"] == "Label"].index, inplace=True)

# turn protocol column to many protocol columns
df_thursday1 = pd.get_dummies(df_thursday1, columns=['Protocol'], drop_first=True)

# pop label column to last column
df_thursday1.insert(len(df_thursday1.columns)-1, 'Label', df_thursday1.pop('Label'))

df_thursday1.drop(columns=columns_to_drop, inplace=True)

# drop duplicate values
df_thursday1.drop_duplicates(inplace=True)

# drop missing values
df_thursday1 = df_thursday1.dropna()

# take only 28810 DDoS LOIC HTTP and 6349 benign
mask_benign4 = (df_thursday1["Label"] == "Benign") 
mask_dos_loichttp = (df_thursday1["Label"] == "DDoS attacks-LOIC-HTTP") 

df_thursday1.loc[mask_benign4] = df_thursday1.loc[mask_benign4].head(6349)
df_thursday1.loc[mask_dos_loichttp] = df_thursday1.loc[mask_dos_loichttp].head(28810)

print(df_thursday1["Label"].value_counts()[['Benign']].sum())
print(df_thursday1["Label"].value_counts()[['DDoS attacks-LOIC-HTTP']].sum())

# drop rows having nan value
df_thursday1 = df_thursday1.dropna()

# replace Brute Force -Web attack label with value 4; Brute Force -XSS with value 5; \
# SQL Injection with value 6 and benign with value 0
df_thursday1.replace(to_replace=['DDoS attacks-LOIC-HTTP'], value=7, inplace=True)
df_thursday1.replace(to_replace=['Benign'], value=0, inplace=True)

print(df_thursday1.info())

# check again number of benign and dos slowhhtptest and dos hulk
print(df_thursday1["Label"].value_counts()[[0]].sum())
print(df_thursday1["Label"].value_counts()[[7]].sum())


# 5. fifth day - Infilteration and benign - 01-03-2018


df_thursday2 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/03-01-2018.csv')

# drop rows label = wrong rows
df_thursday2.drop(df_thursday2.loc[df_thursday2["Label"] == "Label"].index, inplace=True)

# turn protocol column to many protocol columns
df_thursday2 = pd.get_dummies(df_thursday2, columns=['Protocol'], drop_first=True)

# pop label column to last column
df_thursday2.insert(len(df_thursday2.columns)-1, 'Label', df_thursday2.pop('Label'))

df_thursday2.drop(columns=columns_to_drop, inplace=True)

# drop duplicate values
df_thursday2.drop_duplicates(inplace=True)

# drop missing values
df_thursday2 = df_thursday2.dropna()

# take only 4049 Infilteration and 6349 benign
mask_benign5 = (df_thursday2["Label"] == "Benign") 
mask_infilteration = (df_thursday2["Label"] == "Infilteration") 

df_thursday2.loc[mask_benign5] = df_thursday2.loc[mask_benign5].head(6349)
df_thursday2.loc[mask_infilteration] = df_thursday2.loc[mask_infilteration].head(4049)

print(df_thursday2["Label"].value_counts()[['Benign']].sum())
print(df_thursday2["Label"].value_counts()[['Infilteration']].sum())

# drop rows having nan value
df_thursday2 = df_thursday2.dropna()

# replace Brute Force -Web attack label with value 4; Brute Force -XSS with value 5; \
# SQL Injection with value 6 and benign with value 0
df_thursday2.replace(to_replace=['Infilteration'], value=8, inplace=True)
df_thursday2.replace(to_replace=['Benign'], value=0, inplace=True)

print(df_thursday2.info())

# check again number of benign and dos slowhhtptest and dos hulk
print(df_thursday2["Label"].value_counts()[[0]].sum())
print(df_thursday2["Label"].value_counts()[[8]].sum())







