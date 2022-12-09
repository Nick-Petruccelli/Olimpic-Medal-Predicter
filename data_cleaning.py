import pandas as pd

df_dict = pd.read_csv('dictionary.csv')
df_summer = pd.read_csv('summer.csv')
df_winter = pd.read_csv('winter.csv')

#concatanate sumer and winter dataframes
df_sum_win = pd.concat([df_summer, df_winter], axis=0)

#Merge dictinary data frame onto Summer and Winter dataframe
df = df_sum_win.merge(df_dict, how='left', left_on='Country', right_on='Code')
df = df.rename(columns={'Country_x':'Country'})
df = df.drop(['Code', 'Country_y'], axis=1)

#fix Athlete Names
df['Athlete'] = df['Athlete'].apply(lambda x: x.replace(', ', '_'))

#Create feild that showes if athelete won Gold
gold = df['Medal'].str.contains('Gold')
df['Gold'] = gold.apply(lambda x: 1 if x is True else 0)

#Create feild that showes if athelete won Silver
silver = df['Medal'].str.contains('Silver')
df['Silver'] = silver.apply(lambda x: 1 if x is True else 0)

#Create feild that showes if athelete won Bronze
bronze = df['Medal'].str.contains('Bronze')
df['Bronze'] = bronze.apply(lambda x: 1 if x is True else 0)

#Create feilds that show number of meadles previosly won
#total Medals
df['Prev_Medals_Won'] = df.groupby(['Athlete']).cumcount(ascending=True)

#Gold Medals
df['Prev_Gold_Medals_Won'] = df.groupby(['Athlete', 'Gold']).cumcount(ascending=True)
df['Prev_Gold_Medals_Won'] = df.apply(lambda x: x['Prev_Gold_Medals_Won'] if x['Medal'] == 'Gold' else int(x['Prev_Medals_Won'] - x['Prev_Gold_Medals_Won']), axis=1)

#Silver Medals  
df['Prev_Silver_Medals_Won'] = df.groupby(['Athlete','Silver']).cumcount(ascending=True)
df['Prev_Silver_Medals_Won'] = df.apply(lambda x: x['Prev_Silver_Medals_Won'] if x['Medal'] == 'Silver' else int(x['Prev_Medals_Won'] - x['Prev_Silver_Medals_Won']), axis=1)

#Bronze Medals  
df['Prev_Bronze_Medals_Won'] = df.groupby(['Athlete','Bronze']).cumcount(ascending=True)
df['Prev_Bronze_Medals_Won'] = df.apply(lambda x: x['Prev_Bronze_Medals_Won'] if x['Medal'] == 'Bronze' else int(x['Prev_Medals_Won'] - x['Prev_Bronze_Medals_Won']), axis=1)

#save df as csv
df_out = df
df_out.to_csv('data_cleaned.csv', index=False)