#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
# purchase_data['SN'].unique()
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[2]:


purchase_data.dropna(how= 'any')
# numPlayers = len(purchase_data['SN'].value_counts())
numPlayers = purchase_data.drop_duplicates(subset = 'SN')

TotalPl = pd.DataFrame({'Total Players': [len(numPlayers['SN'].value_counts())]})
TotalPl.iloc[0][0]


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:


# ana_df = {
#     'Items' : [len(purchase_data['Item ID'].unique())],
#     'Average Purchase' : [round(purchase_data['Price'].mean(),2)],
#     'Number of Purchase' :  [purchase_data['Purchase ID'].count()],
#     'Revenue' :  [purchase_data['Price'].sum()]
# }
# type(ana_df['Items'])
# Purchasing_Analysis = pd.DataFrame(data=ana_df)
# Purchasing_Analysis.head()
Purchasing_Analysis = pd.DataFrame()
Purchasing_Analysis['Items'] = [len(purchase_data['Item ID'].unique())]
Purchasing_Analysis['Average Purchase'] =[round(purchase_data['Price'].mean(),2)]
Purchasing_Analysis['Number of Purchase'] = [purchase_data['Purchase ID'].count()]
Purchasing_Analysis['Revenue'] = [purchase_data['Price'].sum()]
Purchasing_Analysis['Revenue'] = Purchasing_Analysis['Revenue'].map("${:.2f}".format)
Purchasing_Analysis['Average Purchase'] = Purchasing_Analysis['Average Purchase'].map("${:.2f}".format)
Purchasing_Analysis.head()


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[4]:


GenDemo_df = pd.DataFrame(numPlayers['Gender'].value_counts())
GenDemo_df['Percentage Players'] = GenDemo_df['Gender']/TotalPl.iloc[0][0]
GenDemo_df['Percentage Players'] = GenDemo_df['Percentage Players'].map("{:.2%}".format)
# percentage = {[]}
# GenDemo_df['Gender'].value_counts()
# GenDemo_df['test'] = round(purchase_data['Price'].mean())
# GenDemo_df['SN'].count()/numPlayers*100
GenDemo_df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[5]:


# GenPurch = pd.DataFrame(purchase_data['Gender'].value_counts())
GenPurch = purchase_data.groupby(['Gender']).count()
GenPurch = GenPurch.rename(columns = {'Purchase ID':'Purchase Count'})
GenPurch = GenPurch.drop(GenPurch.columns[1:], axis = 1)
GenPurch['Total Purchase Value'] = purchase_data.groupby(['Gender'])['Price'].sum()
GenPurch['Average Purchase Price'] =  purchase_data.groupby(['Gender'])['Price'].mean()
GenPurch['Avg Total Purchase per Person'] = GenPurch['Total Purchase Value']/GenDemo_df['Gender']
GenPurch['Avg Total Purchase per Person'] = GenPurch['Avg Total Purchase per Person'].map("${:.2f}".format)
GenPurch['Average Purchase Price'] = GenPurch['Average Purchase Price'].map("${:.2f}".format)
GenPurch['Total Purchase Value'] = GenPurch['Total Purchase Value'].map("${:.2f}".format)
GenPurch.head()


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[6]:


# numPlayers['Age'].max()
ageGrp = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']
bins = [0,9.9,14.9,19.9,24.9,29.9,34.9,39.9,50]
numPlayers['Age Group'] = pd.cut(numPlayers['Age'], bins , labels = ageGrp, include_lowest = True)
numPlayers.head()
AgeDemo = numPlayers.groupby(['Age Group']).count()
AgeDemo = AgeDemo.rename(columns = {'Purchase ID': 'Total Count'})
AgeDemo = AgeDemo.drop(AgeDemo.columns[1:], axis = 1)
AgeDemo['Percentage of Players'] = AgeDemo['Total Count']/TotalPl.iloc[0][0]
AgeDemo['Percentage of Players'] = AgeDemo['Percentage of Players'].map("{:.2%}".format)
# AgeDemo = AgeDemo.set_index('Age Group')
AgeDemo


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[7]:


purchase_data['Age Group'] = pd.cut(purchase_data['Age'], bins , labels = ageGrp, include_lowest = True)
purchase_data.head()
agePurch = purchase_data.groupby(['Age Group']).count()
agePurch = agePurch.rename(columns = {'Purchase ID':'Purchase Count'})
agePurch = agePurch.drop(agePurch.columns[1:], axis = 1)
agePurch['Total Purchase Value'] = purchase_data.groupby(['Age Group'])['Price'].sum()
agePurch['Average Purchase Price'] =  purchase_data.groupby(['Age Group'])['Price'].mean()
agePurch['Avg Total Purchase per Person'] = agePurch['Total Purchase Value']/agePurch['Purchase Count']
agePurch['Avg Total Purchase per Person'] = agePurch['Avg Total Purchase per Person'].map("${:.2f}".format)
agePurch['Average Purchase Price'] = agePurch['Average Purchase Price'].map("${:.2f}".format)
agePurch['Total Purchase Value'] = agePurch['Total Purchase Value'].map("${:.2f}".format)
agePurch


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[14]:


topSpend = purchase_data
topSpend = purchase_data.groupby(['SN']).count()
topSpend = topSpend.reset_index()
topSpend = topSpend.rename(columns = {'Purchase ID':'Purchase Count'})

topSpend = topSpend.sort_values('Purchase Count',ascending = False)

topSpend = topSpend.set_index('SN')
topSpend['Average Purchase Price'] = purchase_data.groupby(['SN'])['Price'].mean()
topSpend['Total Purchase Price'] = purchase_data.groupby(['SN'])['Price'].sum()
topSpend = topSpend[['Purchase Count', 'Average Purchase Price', 'Total Purchase Price']]
topSpend = topSpend.sort_values('Total Purchase Price',ascending = False)
topSpend['Average Purchase Price'] = topSpend['Average Purchase Price'].map("${:.2f}".format)
topSpend['Total Purchase Price'] = topSpend['Total Purchase Price'].map("${:.2f}".format)
topSpend.head()
# topSpend


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[9]:


mostPop = purchase_data[['Item ID', 'Item Name', 'Price']]
mostPop = mostPop.groupby(['Item ID']).count()
mostPop = mostPop.reset_index()
# mostPop['Purchase Count'] = mostPop['Item Name'].count()
mostPop.head()


# In[26]:


mp_gp = purchase_data.groupby(['Item ID','Item Name'])
mp_df = mp_gp.agg({'Item Name': 'first', 'Price': ['count', 'mean', 'sum']})
mp_df.head()
mp_df1 = pd.DataFrame({
                      'Purchase Count': mp_gp['Price'].count(),
                      'Item Price': mp_gp['Price'].mean(),
                      'Total Purchase Value': mp_gp['Price'].sum()})
mpitem_df1 = mp_df1.sort_values('Purchase Count', ascending = False)
mpitem_df1['Item Price'] = mpitem_df1['Item Price'].map("${:.2f}".format)
mpitem_df1['Total Purchase Value'] = mpitem_df1['Total Purchase Value'].map("${:.2f}".format)
mpitem_df1.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[28]:


mpitem_df2 = mp_df1.sort_values('Total Purchase Value', ascending = False)
mpitem_df2['Item Price'] = mpitem_df2['Item Price'].map("${:.2f}".format)
mpitem_df2['Total Purchase Value'] = mpitem_df2['Total Purchase Value'].map("${:.2f}".format)
mpitem_df2.head()


# In[ ]:




