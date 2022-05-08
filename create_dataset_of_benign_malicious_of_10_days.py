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


# 6. sixth day - Infilteration and benign - 15-02-2018


df_thursday3 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-15-2018.csv')

# drop rows label = wrong rows
df_thursday3.drop(df_thursday3.loc[df_thursday3["Label"] == "Label"].index, inplace=True)

# turn protocol column to many protocol columns
df_thursday3 = pd.get_dummies(df_thursday3, columns=['Protocol'], drop_first=True)

# pop label column to last column
df_thursday3.insert(len(df_thursday3.columns)-1, 'Label', df_thursday3.pop('Label'))

df_thursday3.drop(columns=columns_to_drop, inplace=True)

# drop duplicate values
df_thursday3.drop_duplicates(inplace=True)

# drop missing values
df_thursday3 = df_thursday3.dropna()

# take only 20754 DoS attacks-GoldenEye; 5495 DoS attacks-Slowloris and 6349 benign
mask_benign6 = (df_thursday3["Label"] == "Benign") 
mask_dos_goldeneye = (df_thursday3["Label"] == "DoS attacks-GoldenEye") 
mask_dos_slowloris = (df_thursday3["Label"] == "DoS attacks-Slowloris") 

df_thursday3.loc[mask_benign6] = df_thursday3.loc[mask_benign6].head(6349)
df_thursday3.loc[mask_dos_goldeneye] = df_thursday3.loc[mask_dos_goldeneye].head(20754)
df_thursday3.loc[mask_dos_slowloris] = df_thursday3.loc[mask_dos_slowloris].head(5495)

print(df_thursday3["Label"].value_counts()[['Benign']].sum())
print(df_thursday3["Label"].value_counts()[['DoS attacks-GoldenEye']].sum())
print(df_thursday3["Label"].value_counts()[['DoS attacks-Slowloris']].sum())

# drop rows having nan value
df_thursday3 = df_thursday3.dropna()

# replace Brute Force -Web attack label with value 4; Brute Force -XSS with value 5; \
# SQL Injection with value 6 and benign with value 0
df_thursday3.replace(to_replace=['DoS attacks-GoldenEye'], value=9, inplace=True)
df_thursday3.replace(to_replace=['DoS attacks-Slowloris'], value=10, inplace=True)
df_thursday3.replace(to_replace=['Benign'], value=0, inplace=True)

print(df_thursday3.info())

# check again number of benign and dos slowhhtptest and dos hulk
print(df_thursday3["Label"].value_counts()[[0]].sum())
print(df_thursday3["Label"].value_counts()[[9]].sum())
print(df_thursday3["Label"].value_counts()[[10]].sum())


# 7. seventh day - Infilteration and benign - 22-02-2018


df_thursday4 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-22-2018.csv')

# drop rows label = wrong rows
df_thursday4.drop(df_thursday4.loc[df_thursday4["Label"] == "Label"].index, inplace=True)

# turn protocol column to many protocol columns
df_thursday4 = pd.get_dummies(df_thursday4, columns=['Protocol'], drop_first=True)

# pop label column to last column
df_thursday4.insert(len(df_thursday4.columns)-1, 'Label', df_thursday4.pop('Label'))

df_thursday4.drop(columns=columns_to_drop, inplace=True)

# drop duplicate values
df_thursday4.drop_duplicates(inplace=True)

# drop missing values
df_thursday4 = df_thursday4.dropna()

# take only 20754 DoS attacks-GoldenEye; 5495 DoS attacks-Slowloris and 6349 benign
mask_bruteforce_web = (df_thursday4["Label"] == "Brute Force -Web") 
mask_bruteforce_xss = (df_thursday4["Label"] == "Brute Force -XSS") 
mask_sql_injection = (df_thursday4["Label"] == "SQL Injection") 
mask_benign7 = (df_thursday4["Label"] == "Benign") 

df_thursday4.loc[mask_benign7] = df_thursday4.loc[mask_benign7].head(6349)
df_thursday4.loc[mask_bruteforce_web] = df_thursday4.loc[mask_bruteforce_web].head(228)
df_thursday4.loc[mask_bruteforce_xss] = df_thursday4.loc[mask_bruteforce_xss].head(79)
df_thursday4.loc[mask_sql_injection] = df_thursday4.loc[mask_sql_injection].head(34)


print(df_thursday4["Label"].value_counts()[['Benign']].sum())
print(df_thursday4["Label"].value_counts()[['Brute Force -Web']].sum())
print(df_thursday4["Label"].value_counts()[['Brute Force -XSS']].sum())
print(df_thursday4["Label"].value_counts()[['SQL Injection']].sum())

# drop rows having nan value
df_thursday4 = df_thursday4.dropna()

# replace Brute Force -Web attack label with value 4; Brute Force -XSS with value 5; \
# SQL Injection with value 6 and benign with value 0
df_thursday4.replace(to_replace=['Brute Force -Web'], value=4, inplace=True)
df_thursday4.replace(to_replace=['Brute Force -XSS'], value=5, inplace=True)
df_thursday4.replace(to_replace=['SQL Injection'], value=6, inplace=True)
df_thursday4.replace(to_replace=['Benign'], value=0, inplace=True)

print(df_thursday4.info())

# check again number of benign and dos slowhhtptest and dos hulk
print(df_thursday4["Label"].value_counts()[[0]].sum())
print(df_thursday4["Label"].value_counts()[[4]].sum())
print(df_thursday4["Label"].value_counts()[[5]].sum())
print(df_thursday4["Label"].value_counts()[[6]].sum())


# 8. 8th day - FTP-Brute Force, SSH-BruteForce and benign - 14-02-2018


df_wednesday1 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-14-2018.csv')

# drop rows label = wrong rows
df_wednesday1.drop(df_wednesday1.loc[df_wednesday1["Label"] == "Label"].index, inplace=True)

# turn protocol column to many protocol columns
df_wednesday1 = pd.get_dummies(df_wednesday1, columns=['Protocol'], drop_first=True)

# pop label column to last column
df_wednesday1.insert(len(df_wednesday1.columns)-1, 'Label', df_wednesday1.pop('Label'))

df_wednesday1.drop(columns=columns_to_drop, inplace=True)

# drop duplicate values
df_wednesday1.drop_duplicates(inplace=True)

# drop missing values
df_wednesday1 = df_wednesday1.dropna()

# take only 54 FTP-BruteForce; 9380 SSH-Bruteforce and 6349 benign
mask_ftp_bruteforce = (df_wednesday1["Label"] == "FTP-BruteForce") 
mask_ssh_bruteforce = (df_wednesday1["Label"] == "SSH-Bruteforce") 
mask_benign8 = (df_wednesday1["Label"] == "Benign") 

df_wednesday1.loc[mask_benign8] = df_wednesday1.loc[mask_benign8].head(6349)
df_wednesday1.loc[mask_ftp_bruteforce] = df_wednesday1.loc[mask_ftp_bruteforce].head(54)
df_wednesday1.loc[mask_ssh_bruteforce] = df_wednesday1.loc[mask_ssh_bruteforce].head(9380)

print(df_wednesday1["Label"].value_counts()[['Benign']].sum())
print(df_wednesday1["Label"].value_counts()[['FTP-BruteForce']].sum())
print(df_wednesday1["Label"].value_counts()[['SSH-Bruteforce']].sum())

# drop rows having nan value
df_wednesday1 = df_wednesday1.dropna()

# replace Brute Force -Web attack label with value 4; Brute Force -XSS with value 5; \
# SQL Injection with value 6 and benign with value 0
df_wednesday1.replace(to_replace=['FTP-BruteForce'], value=11, inplace=True)
df_wednesday1.replace(to_replace=['SSH-Bruteforce'], value=12, inplace=True)
df_wednesday1.replace(to_replace=['Benign'], value=0, inplace=True)

print(df_wednesday1.info())

# check again number of benign and dos slowhhtptest and dos hulk
print(df_wednesday1["Label"].value_counts()[[0]].sum())
print(df_wednesday1["Label"].value_counts()[[11]].sum())
print(df_wednesday1["Label"].value_counts()[[12]].sum())



# 9. 9th day - DDOS attack - LOIC -UDP, DDOS attack - HOIC and benign - 21-02-2018


df_wednesday2 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-21-2018.csv')

# drop rows label = wrong rows
df_wednesday2.drop(df_wednesday2.loc[df_wednesday2["Label"] == "Label"].index, inplace=True)

# turn protocol column to many protocol columns
df_wednesday2 = pd.get_dummies(df_wednesday2, columns=['Protocol'], drop_first=True)

# pop label column to last column
df_wednesday2.insert(len(df_wednesday2.columns)-1, 'Label', df_wednesday2.pop('Label'))

df_wednesday2.drop(columns=columns_to_drop, inplace=True)

# drop duplicate values
df_wednesday2.drop_duplicates(inplace=True)

# drop missing values
df_wednesday2 = df_wednesday2.dropna()

# take only 1730 DDOS attack-LOIC-UDP; 34301 DDOS attack-HOIC and 6349 benign
mask_ddos_loicudp = (df_wednesday2["Label"] == "DDOS attack-LOIC-UDP") 
mask_ddos_hoic = (df_wednesday2["Label"] == "DDOS attack-HOIC") 
mask_benign9 = (df_wednesday2["Label"] == "Benign") 

df_wednesday2.loc[mask_benign9] = df_wednesday2.loc[mask_benign9].head(6349)
df_wednesday2.loc[mask_ddos_loicudp] = df_wednesday2.loc[mask_ddos_loicudp].head(1730)
df_wednesday2.loc[mask_ddos_hoic] = df_wednesday2.loc[mask_ddos_hoic].head(34301)

print(df_wednesday2["Label"].value_counts()[['Benign']].sum())
print(df_wednesday2["Label"].value_counts()[['DDOS attack-LOIC-UDP']].sum())
print(df_wednesday2["Label"].value_counts()[['DDOS attack-HOIC']].sum())

# drop rows having nan value
df_wednesday2 = df_wednesday2.dropna()

# replace Brute Force -Web attack label with value 4; Brute Force -XSS with value 5; \
# SQL Injection with value 6 and benign with value 0
df_wednesday2.replace(to_replace=['DDOS attack-LOIC-UDP'], value=13, inplace=True)
df_wednesday2.replace(to_replace=['DDOS attack-HOIC'], value=14, inplace=True)
df_wednesday2.replace(to_replace=['Benign'], value=0, inplace=True)

print(df_wednesday2.info())

# check again number of benign and dos slowhhtptest and dos hulk
print(df_wednesday2["Label"].value_counts()[[0]].sum())
print(df_wednesday2["Label"].value_counts()[[13]].sum())
print(df_wednesday2["Label"].value_counts()[[14]].sum())


# 10. 10th day - Infilteration and benign - 02-28-2018


df_wednesday3 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-28-2018.csv')

# drop rows label = wrong rows
df_wednesday3.drop(df_wednesday3.loc[df_wednesday3["Label"] == "Label"].index, inplace=True)

# turn protocol column to many protocol columns
df_wednesday3 = pd.get_dummies(df_wednesday3, columns=['Protocol'], drop_first=True)

# pop label column to last column
df_wednesday3.insert(len(df_wednesday3.columns)-1, 'Label', df_wednesday3.pop('Label'))

df_wednesday3.drop(columns=columns_to_drop, inplace=True)

# drop duplicate values
df_wednesday3.drop_duplicates(inplace=True)

# drop missing values
df_wednesday3 = df_wednesday3.dropna()

# take only 4049 Infilteration and 6349 benign
mask_benign10 = (df_wednesday3["Label"] == "Benign") 
mask_infilteration = (df_wednesday3["Label"] == "Infilteration") 

df_wednesday3.loc[mask_benign5] = df_wednesday3.loc[mask_benign10].head(6349)
df_wednesday3.loc[mask_infilteration] = df_wednesday3.loc[mask_infilteration].head(4049)

print(df_wednesday3["Label"].value_counts()[['Benign']].sum())
print(df_wednesday3["Label"].value_counts()[['Infilteration']].sum())

# drop rows having nan value
df_wednesday3 = df_wednesday3.dropna()

# replace Brute Force -Web attack label with value 4; Brute Force -XSS with value 5; \
# SQL Injection with value 6 and benign with value 0
df_wednesday3.replace(to_replace=['Infilteration'], value=8, inplace=True)
df_wednesday3.replace(to_replace=['Benign'], value=0, inplace=True)

print(df_wednesday3.info())

# check again number of benign and dos slowhhtptest and dos hulk
print(df_wednesday3["Label"].value_counts()[[0]].sum())
print(df_wednesday3["Label"].value_counts()[[8]].sum())


# sum data of 10 days into one data frame

df_sum= pd.concat([df_friday1, df_friday2, df_friday3, df_thursday1, df_thursday2,\
                  df_thursday3, df_thursday4, df_wednesday1, \
                   df_wednesday2, df_wednesday3], axis=0, ignore_index=True)

df_sum.shape[0]


df_sum.to_csv("processed_first_final_dataset_benign_malicious_of_10_days.csv", index=False)