import pandas as pd

df_friday1 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/03-02-2018.csv')

df_friday1

df_friday1.columns

df_friday1["Label"].unique()

print(df_friday1["Label"].value_counts()[['Benign']].sum())
print(df_friday1["Label"].value_counts()[['Bot']].sum())

# Remove erroneous 'Label' row
df_friday1.drop(df_friday1.loc[df_friday1["Label"] == "Label"].index, inplace=True)

df_friday1

df_friday1.replace(to_replace=['Bot'], value="Malicious", inplace=True)

df_friday1

df_friday1["Label"].unique()

print(df_friday1["Label"].value_counts()[['Benign']].sum())
print(df_friday1["Label"].value_counts()[['Malicious']].sum())

df_friday1.columns

df_friday1["Protocol"].unique()

df_friday1 = pd.get_dummies(df_friday1, columns=['Protocol'], drop_first=True)
df_friday1

# making Label column the last column again
df_friday1.insert(len(df_friday1.columns)-1, 'Label', df_friday1.pop('Label'))

df_friday1

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

df_friday1

df_friday1["Label"].unique()

df_friday1["Label"].unique()

df_friday1

df_friday1["Label"].unique()

df_friday1.drop_duplicates(inplace=True)

df_friday1

print(df_friday1["Label"].value_counts()[['Benign']].sum())
print(df_friday1["Label"].value_counts()[['Malicious']].sum())

df_friday1.replace(to_replace="Benign", value=0, inplace=True)
df_friday1.replace(to_replace="Malicious", value=1, inplace=True)

df_friday1

print(df_friday1["Label"].value_counts()[[0]].sum())
print(df_friday1["Label"].value_counts()[[1]].sum())

df_friday1.info()

print(df_friday1["Label"].value_counts()[[0]].sum())
print(df_friday1["Label"].value_counts()[[1]].sum())

# take dataframe of benign of the first day
df_friday1_benign =  df_friday1[df_friday1["Label"]==0]
df_friday1_benign

# take datafram of malicious of the first day
df_friday1_malicious = df_friday1[df_friday1["Label"]==1]
df_friday1_malicious

df_friday2 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-16-2018.csv', low_memory=False)

df_friday2

df_friday2.columns

df_friday2["Label"].unique()

print(df_friday2["Label"].value_counts()[['Benign']].sum())
print(df_friday2["Label"].value_counts()[['DoS attacks-SlowHTTPTest']].sum())
print(df_friday2["Label"].value_counts()[['DoS attacks-Hulk']].sum())
print(df_friday2["Label"].value_counts()[['Label']].sum())

# Remove erroneous 'Label' row
df_friday2.drop(df_friday2.loc[df_friday2["Label"] == "Label"].index, inplace=True)

df_friday2

df_friday2.replace(to_replace=['DoS attacks-SlowHTTPTest'], value="Malicious", inplace=True)
df_friday2.replace(to_replace=['DoS attacks-Hulk'], value="Malicious", inplace=True)

df_friday2

df_friday2["Label"].unique()

print(df_friday2["Label"].value_counts()[['Benign']].sum())
print(df_friday2["Label"].value_counts()[['Malicious']].sum())

df_friday2.columns

df_friday2["Protocol"].unique()

df_friday2 = pd.get_dummies(df_friday2, columns=['Protocol'], drop_first=True)
df_friday2

# making Label column the last column again
df_friday2.insert(len(df_friday2.columns)-1, 'Label', df_friday2.pop('Label'))

df_friday2

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

df_friday2.drop(columns=columns_to_drop, inplace=True)

df_friday2

df_friday2["Label"].unique()

df_friday2["Label"].unique()

df_friday2

df_friday2["Label"].unique()

df_friday2.drop_duplicates(inplace=True)

df_friday2

print(df_friday2["Label"].value_counts()[['Benign']].sum())
print(df_friday2["Label"].value_counts()[['Malicious']].sum())


df_friday2.replace(to_replace="Benign", value=0, inplace=True)
df_friday2.replace(to_replace="Malicious", value=1, inplace=True)

df_friday2

print(df_friday2["Label"].value_counts()[[0]].sum())
print(df_friday2["Label"].value_counts()[[1]].sum())


df_friday2.info()

print(df_friday2["Label"].value_counts()[[0]].sum())
print(df_friday2["Label"].value_counts()[[1]].sum())


# take dataframe of benign of the first day
df_friday2_benign =  df_friday2[df_friday2["Label"]==0]
df_friday2_benign

# take datafram of malicious of the first day
df_friday2_malicious = df_friday2[df_friday2["Label"]==1]
df_friday2_malicious

df_friday3 = pd.read_csv('/mnt/d/project-chau/dataset/\
cse-cic-ids108/dataset/02-23-2018.csv')

df_friday3

df_friday3.columns

df_friday3["Label"].unique()

print(df_friday3["Label"].value_counts()[['Benign']].sum())
print(df_friday3["Label"].value_counts()[['Brute Force -Web']].sum())
print(df_friday3["Label"].value_counts()[['Brute Force -XSS']].sum())
print(df_friday3["Label"].value_counts()[['SQL Injection']].sum())

# Remove erroneous 'Label' row
df_friday3.drop(df_friday3.loc[df_friday3["Label"] == "Label"].index, inplace=True)

df_friday3

df_friday3.replace(to_replace=['Brute Force -Web'], value="Malicious", inplace=True)
df_friday3.replace(to_replace=['Brute Force -XSS'], value="Malicious", inplace=True)
df_friday3.replace(to_replace=['SQL Injection'], value="Malicious", inplace=True)

df_friday3

df_friday3["Label"].unique()

print(df_friday3["Label"].value_counts()[['Benign']].sum())
print(df_friday3["Label"].value_counts()[['Malicious']].sum())

df_friday3.columns

df_friday3["Protocol"].unique()

df_friday3 = pd.get_dummies(df_friday3, columns=['Protocol'], drop_first=True)
df_friday3

# making Label column the last column again
df_friday3.insert(len(df_friday3.columns)-1, 'Label', df_friday3.pop('Label'))

df_friday3

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

df_friday3.drop(columns=columns_to_drop, inplace=True)

df_friday3

df_friday3["Label"].unique()

df_friday3

df_friday3["Label"].unique()

df_friday3.drop_duplicates(inplace=True)

df_friday3

print(df_friday3["Label"].value_counts()[['Benign']].sum())
print(df_friday3["Label"].value_counts()[['Malicious']].sum())

df_friday3.replace(to_replace="Benign", value=0, inplace=True)
df_friday3.replace(to_replace="Malicious", value=1, inplace=True)

df_friday3


print(df_friday3["Label"].value_counts()[[0]].sum())
print(df_friday3["Label"].value_counts()[[1]].sum())


df_friday3.info()


print(df_friday3["Label"].value_counts()[[0]].sum())
print(df_friday3["Label"].value_counts()[[1]].sum())

# take dataframe of benign of the first day
df_friday3_benign =  df_friday3[df_friday3["Label"]==0]
df_friday3_benign

# take datafram of malicious of the first day
df_friday3_malicious = df_friday3[df_friday3["Label"]==1]
df_friday3_malicious

df_thursday1 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-20-2018.csv', low_memory=False)

# Remove erroneous 'Label' row
df_thursday1.drop(df_thursday1.loc[df_thursday1["Label"] == "Label"].index, inplace=True)

df_thursday1.replace(to_replace=['DDoS attacks-LOIC-HTTP'], value="Malicious", inplace=True)

print(df_thursday1["Label"].value_counts()[['Benign']].sum())
print(df_thursday1["Label"].value_counts()[['Malicious']].sum())

df_thursday1 = pd.get_dummies(df_thursday1, columns=['Protocol'], drop_first=True)
df_thursday1

# making Label column the last column again
df_thursday1.insert(len(df_thursday1.columns)-1, 'Label', df_thursday1.pop('Label'))

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

df_thursday1.drop(columns=columns_to_drop, inplace=True)

df_thursday1.drop_duplicates(inplace=True)

df_thursday1.replace(to_replace="Benign", value=0, inplace=True)
df_thursday1.replace(to_replace="Malicious", value=1, inplace=True)

print(df_thursday1["Label"].value_counts()[[0]].sum())
print(df_thursday1["Label"].value_counts()[[1]].sum())

# take dataframe of benign of the first day
df_friday4_benign =  df_thursday1[df_thursday1["Label"]==0]
df_friday4_benign

# take datafram of malicious of the first day
df_friday4_malicious = df_thursday1[df_thursday1["Label"]==1]
df_friday4_malicious

df_thursday2 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/03-01-2018.csv')

# Remove erroneous 'Label' row
df_thursday2.drop(df_thursday2.loc[df_thursday1["Label"] == "Label"].index, inplace=True)

df_thursday2.replace(to_replace=['Infilteration'], value="Malicious", inplace=True)

df_thursday2 = pd.get_dummies(df_thursday2, columns=['Protocol'], drop_first=True)
df_thursday2

# making Label column the last column again
df_thursday2.insert(len(df_thursday2.columns)-1, 'Label', df_thursday2.pop('Label'))

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

df_thursday2.drop(columns=columns_to_drop, inplace=True)

df_thursday2["Label"].unique()

df_thursday2.drop_duplicates(inplace=True)

df_thursday2.replace(to_replace="Benign", value=0, inplace=True)
df_thursday2.replace(to_replace="Malicious", value=1, inplace=True)

print(df_thursday2["Label"].value_counts()[[0]].sum())
print(df_thursday2["Label"].value_counts()[[1]].sum())

# take dataframe of benign of the first day
df_friday5_benign =  df_thursday2[df_thursday2["Label"]==0]
df_friday5_benign

# take datafram of malicious of the first day
df_friday5_malicious = df_thursday2[df_thursday2["Label"]==1]
df_friday5_malicious

df_thursday3 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-15-2018.csv')

print(df_thursday3["Label"].value_counts()[['Benign']].sum())
print(df_thursday3["Label"].value_counts()[['DoS attacks-GoldenEye']].sum())
print(df_thursday3["Label"].value_counts()[['DoS attacks-Slowloris']].sum())

# Remove erroneous 'Label' row
df_thursday3.drop(df_thursday3.loc[df_thursday3["Label"] == "Label"].index, inplace=True)

df_thursday3.replace(to_replace=['DoS attacks-GoldenEye'], value="Malicious", inplace=True)
df_thursday3.replace(to_replace=['DoS attacks-Slowloris'], value="Malicious", inplace=True)

print(df_thursday3["Label"].value_counts()[['Benign']].sum())
print(df_thursday3["Label"].value_counts()[['Malicious']].sum())

df_thursday3 = pd.get_dummies(df_thursday3, columns=['Protocol'], drop_first=True)
df_thursday3

# making Label column the last column again
df_thursday3.insert(len(df_thursday3.columns)-1, 'Label', df_thursday3.pop('Label'))

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

df_thursday3.drop(columns=columns_to_drop, inplace=True)

df_thursday3.drop_duplicates(inplace=True)

df_thursday3.replace(to_replace="Benign", value=0, inplace=True)
df_thursday3.replace(to_replace="Malicious", value=1, inplace=True)

print(df_thursday3["Label"].value_counts()[[0]].sum())
print(df_thursday3["Label"].value_counts()[[1]].sum())

# take dataframe of benign of the first day
df_friday6_benign =  df_thursday3[df_thursday3["Label"]==0]
df_friday6_benign

# take datafram of malicious of the first day
df_friday6_malicious = df_thursday3[df_thursday3["Label"]==1]
df_friday6_malicious

df_thursday4 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-22-2018.csv')

print(df_thursday4["Label"].value_counts()[['Benign']].sum())
print(df_thursday4["Label"].value_counts()[['Brute Force -Web']].sum())
print(df_thursday4["Label"].value_counts()[['Brute Force -XSS']].sum())
print(df_thursday4["Label"].value_counts()[['SQL Injection']].sum())

# Remove erroneous 'Label' row
df_thursday4.drop(df_thursday4.loc[df_thursday4["Label"] == "Label"].index, inplace=True)

df_thursday4.replace(to_replace=['Brute Force -Web'], value="Malicious", inplace=True)
df_thursday4.replace(to_replace=['Brute Force -XSS'], value="Malicious", inplace=True)
df_thursday4.replace(to_replace=['SQL Injection'], value="Malicious", inplace=True)

print(df_thursday4["Label"].value_counts()[['Benign']].sum())
print(df_thursday4["Label"].value_counts()[['Malicious']].sum())

df_thursday4 = pd.get_dummies(df_thursday4, columns=['Protocol'], drop_first=True)
df_thursday4

# making Label column the last column again
df_thursday4.insert(len(df_thursday4.columns)-1, 'Label', df_thursday4.pop('Label'))

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

df_thursday4.drop(columns=columns_to_drop, inplace=True)

df_thursday4.drop_duplicates(inplace=True)

print(df_thursday4["Label"].value_counts()[['Benign']].sum())
print(df_thursday4["Label"].value_counts()[['Malicious']].sum())

df_thursday4.replace(to_replace="Benign", value=0, inplace=True)
df_thursday4.replace(to_replace="Malicious", value=1, inplace=True)

# take dataframe of benign of the first day
df_friday7_benign =  df_thursday4[df_thursday4["Label"]==0]
df_friday7_benign

# take datafram of malicious of the first day
df_friday7_malicious = df_thursday4[df_thursday4["Label"]==1]
df_friday7_malicious

df_wednesday1 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-14-2018.csv')

print(df_wednesday1["Label"].value_counts()[['Benign']].sum())
print(df_wednesday1["Label"].value_counts()[['FTP-BruteForce']].sum())
print(df_wednesday1["Label"].value_counts()[['SSH-Bruteforce']].sum())

# Remove erroneous 'Label' row
df_wednesday1.drop(df_wednesday1.loc[df_wednesday1["Label"] == "Label"].index, inplace=True)

df_wednesday1.replace(to_replace=['FTP-BruteForce'], value="Malicious", inplace=True)
df_wednesday1.replace(to_replace=['SSH-Bruteforce'], value="Malicious", inplace=True)

print(df_wednesday1["Label"].value_counts()[['Benign']].sum())
print(df_wednesday1["Label"].value_counts()[['Malicious']].sum())


df_wednesday1 = pd.get_dummies(df_wednesday1, columns=['Protocol'], drop_first=True)
df_wednesday1

# making Label column the last column again
df_wednesday1.insert(len(df_wednesday1.columns)-1, 'Label', df_wednesday1.pop('Label'))

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

df_wednesday1.drop(columns=columns_to_drop, inplace=True)

df_wednesday1.drop_duplicates(inplace=True)

df_wednesday1.replace(to_replace="Benign", value=0, inplace=True)
df_wednesday1.replace(to_replace="Malicious", value=1, inplace=True)

# take dataframe of benign of the first day
df_friday8_benign =  df_wednesday1[df_wednesday1["Label"]==0]
df_friday8_benign

# take datafram of malicious of the first day
df_friday8_malicious = df_wednesday1[df_wednesday1["Label"]==1]
df_friday8_malicious

df_wednesday2 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-21-2018.csv')

print(df_wednesday2["Label"].value_counts()[['Benign']].sum())
print(df_wednesday2["Label"].value_counts()[['DDOS attack-LOIC-UDP']].sum())
print(df_wednesday2["Label"].value_counts()[['DDOS attack-HOIC']].sum())

# Remove erroneous 'Label' row
df_wednesday2.drop(df_wednesday2.loc[df_wednesday2["Label"] == "Label"].index, inplace=True)

df_wednesday2.replace(to_replace=['DDOS attack-LOIC-UDP'], value="Malicious", inplace=True)
df_wednesday2.replace(to_replace=['DDOS attack-HOIC'], value="Malicious", inplace=True)

print(df_wednesday2["Label"].value_counts()[['Benign']].sum())
print(df_wednesday2["Label"].value_counts()[['Malicious']].sum())

df_wednesday2 = pd.get_dummies(df_wednesday2, columns=['Protocol'], drop_first=True)
df_wednesday2

# making Label column the last column again
df_wednesday2.insert(len(df_wednesday2.columns)-1, 'Label', df_wednesday2.pop('Label'))

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

df_wednesday2.drop(columns=columns_to_drop, inplace=True)

df_wednesday2.drop_duplicates(inplace=True)

df_wednesday2.replace(to_replace="Benign", value=0, inplace=True)
df_wednesday2.replace(to_replace="Malicious", value=1, inplace=True)

# take dataframe of benign of the first day
df_friday9_benign =  df_wednesday2[df_wednesday2["Label"]==0]
df_friday9_benign

# take datafram of malicious of the first day
df_friday9_malicious = df_wednesday2[df_wednesday2["Label"]==1]
df_friday9_malicious

df_wednesday3 = pd.read_csv('/mnt/d/project-chau/dataset/cse-cic-ids108/dataset/02-28-2018.csv', low_memory=False)

print(df_wednesday3["Label"].value_counts()[['Benign']].sum())
# print(df_wednesday3["Label"].value_counts()[['Label']].sum())
print(df_wednesday3["Label"].value_counts()[['Infilteration']].sum())

df_wednesday3.loc[df_wednesday3["Label"] == "Label"]

# Remove erroneous 'Label' row
df_wednesday3.drop(df_wednesday3.loc[df_wednesday3["Label"] == "Label"].index, inplace=True)

df_wednesday3.replace(to_replace=['Infilteration'], value="Malicious", inplace=True)

print(df_wednesday3["Label"].value_counts()[['Benign']].sum())
print(df_wednesday3["Label"].value_counts()[['Malicious']].sum())

df_wednesday3 = pd.get_dummies(df_wednesday3, columns=['Protocol'], drop_first=True)
df_wednesday3

# making Label column the last column again
df_wednesday3.insert(len(df_wednesday3.columns)-1, 'Label', df_wednesday3.pop('Label'))

df_wednesday3.drop(columns=columns_to_drop, inplace=True)

df_wednesday3.drop_duplicates(inplace=True)

df_wednesday3.replace(to_replace="Benign", value=0, inplace=True)
df_wednesday3.replace(to_replace="Malicious", value=1, inplace=True)

# take dataframe of benign of the first day
df_friday10_benign =  df_wednesday3[df_wednesday3["Label"]==0]
df_friday10_benign

# take datafram of malicious of the first day
df_friday10_malicious = df_wednesday3[df_wednesday3["Label"]==1]
df_friday10_malicious

# check again number of each attacks in 10 days

# 1. benign - ...
print("Number of benign in the first day (it must be ... ) : ",df_friday1_benign.shape[0])
print("-----------------------------------------------------------------------------------------------")

# 1. attack - ...
print("Number of attacks in the first day (it must be ...) : ",df_friday1_malicious.shape[0])
print("-----------------------------------------------------------------------------------------------\n")

# 2. benign - ....
print("Number of benign in the 2nd day (it must be ...) : ",df_friday2_benign.shape[0])
print("-----------------------------------------------------------------------------------------------")

# 2. attack - ...
print("Number of attack in the 2nd day (it must be ...) : ",df_friday2_malicious.shape[0])
print("-----------------------------------------------------------------------------------------------\n")

# 3. benign - ...
print("Number of benign in the 3rd day (it must be ...) : ",df_friday3_benign.shape[0])
print("-----------------------------------------------------------------------------------------------")

# 3. attack - ...
print("Number of attack in the 3rd day (it must be ...) : ",df_friday3_malicious.shape[0])
print("-----------------------------------------------------------------------------------------------\n")

# 4. benign - ...
print("Number of benign in the 4th day (it must be ... ) : ",df_friday4_benign.shape[0])
print("-----------------------------------------------------------------------------------------------")

# 4. attack - ...
print("Number of attacks in the 4th day (it must be ...) : ",df_friday4_malicious.shape[0])
print("-----------------------------------------------------------------------------------------------\n")

# 5. benign - ....
print("Number of benign in the 5th day (it must be ...) : ",df_friday5_benign.shape[0])
print("-----------------------------------------------------------------------------------------------")

# 5. attack - ...
print("Number of attack in the 5th day (it must be ...) : ",df_friday5_malicious.shape[0])
print("-----------------------------------------------------------------------------------------------\n")

# 6. benign - ...
print("Number of benign in the 6th day (it must be ...) : ",df_friday6_benign.shape[0])
print("-----------------------------------------------------------------------------------------------")

# 6. attack - ...
print("Number of attack in the 6th day (it must be ...) : ",df_friday6_malicious.shape[0])
print("-----------------------------------------------------------------------------------------------\n")

# 7. benign - ...
print("Number of benign in the 7th day (it must be ... ) : ",df_friday7_benign.shape[0])
print("-----------------------------------------------------------------------------------------------")

# 7. attack - ...
print("Number of attacks in the 7th day (it must be ...) : ",df_friday7_malicious.shape[0])
print("-----------------------------------------------------------------------------------------------\n")

# 8. benign - ....
print("Number of benign in the 8th day (it must be ...) : ",df_friday8_benign.shape[0])
print("-----------------------------------------------------------------------------------------------")

# 8. attack - ...
print("Number of attack in the 8th day (it must be ...) : ",df_friday8_malicious.shape[0])
print("-----------------------------------------------------------------------------------------------\n")

# 9. benign - ...
print("Number of benign in the 9th day (it must be ...) : ",df_friday9_benign.shape[0])
print("-----------------------------------------------------------------------------------------------")

# 9. attack - ...
print("Number of attack in the 9th day (it must be ...) : ",df_friday9_malicious.shape[0])
print("-----------------------------------------------------------------------------------------------\n")

# 10. benign - ...
print("Number of benign in the 10th day (it must be ... ) : ",df_friday10_benign.shape[0])
print("-----------------------------------------------------------------------------------------------")

# 10. attack - ...
print("Number of attack in the 10th day (it must be ...) : ",df_friday10_malicious.shape[0])
print("-----------------------------------------------------------------------------------------------\n")


# in total : benign 

df_total_10_days_benign = pd.concat([df_friday1_benign, df_friday2_benign, df_friday3_benign, df_friday4_benign,\
    df_friday5_benign, df_friday6_benign,df_friday7_benign,df_friday8_benign,df_friday9_benign\
        ,df_friday10_benign], axis=0, ignore_index=True)

df_total_10_days_benign


# in total : attack 

df_total_10_days_malicious = pd.concat([df_friday1_malicious, df_friday2_malicious, df_friday3_malicious,\
    df_friday4_malicious, df_friday5_malicious, df_friday6_malicious, \
        df_friday7_malicious, df_friday8_malicious, df_friday9_malicious\
        , df_friday10_malicious], axis=0, ignore_index=True)

df_total_10_days_malicious


print("Number of benign in 10 days (it must be ... ) : ",df_total_10_days_benign.shape[0])
print("-----------------------------------------------------------------------------------------------")

print("Number of attacks in 10 days (it must be ...) : ",df_total_10_days_malicious.shape[0])
print("-----------------------------------------------------------------------------------------------\n")


# sum data of 10 days into one data frame

df_sum= pd.concat([df_friday1, df_friday2, df_friday3, df_wednesday1, df_wednesday2,\
                  df_wednesday3, df_thursday1, df_thursday2, \
                   df_thursday3, df_thursday4,], axis=0, ignore_index=True)
df_sum.shape[0]


df_sum.to_csv("processed_first_final_dataset_benign_malicious_of_10_days.csv", index=False)