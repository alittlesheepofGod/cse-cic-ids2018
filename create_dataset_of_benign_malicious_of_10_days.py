import pandas as pd

# first day - fridat - 02-03-2018

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

