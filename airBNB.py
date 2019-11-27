#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


# In[6]:


#reading data
df = pd.read_csv("/Users/vidhi/Documents/College/7th_sem/DONE/Data_Science/new-york-city-airbnb-open-data/AB_NYC_2019.csv")
df.head()


# In[7]:


#check for null values
df.isnull().sum()


# In[8]:


df.describe()


# In[9]:


df.info()


# In[10]:


df['reviews_per_month'].fillna(0,inplace = True)


# In[11]:


df['name'].fillna("$",inplace=True)
df['host_name'].fillna("#",inplace=True)


# In[12]:


df.drop(['last_review'],axis=1,inplace=True)


# In[13]:


df.head()


# In[14]:


df.neighbourhood.unique()


# In[20]:


f,ax = plt.subplots(figsize=(15,6))
ax = sns.countplot(df.neighbourhood_group,palette="muted")
ax.set_title("Different neighbourhood groups")  
plt.show()


# In[45]:


df1 = df.host_id.value_counts()[:11]
f,ax = plt.subplots(figsize=(16,5))
ax = sns.barplot(x = df1.index,y=df1.values,palette="muted")
ax.set_title("Top 10 hosts (ID)")
plt.show()


# In[28]:


df1 = df[df.neighbourhood_group == "Brooklyn"][["neighbourhood","price"]]
f,ax = plt.subplots(figsize=(10,5))
d = df1.groupby("neighbourhood").mean()
sns.distplot(d)
ax.set_title("Price Distribution in Brooklyn")
plt.show()


# In[29]:


df1 = df[df.neighbourhood_group == "Manhattan"][["neighbourhood","price"]]
f,ax = plt.subplots(figsize=(10,5))
d = df1.groupby("neighbourhood").mean()
sns.distplot(d)
ax.set_title("Price Distribution in Manhattan")
plt.show()


# In[31]:


df1 = df[df.neighbourhood_group == "Queens"][["neighbourhood","price"]]
f,ax = plt.subplots(figsize=(10,5))
d = df1.groupby("neighbourhood").mean()
sns.distplot(d)
ax.set_title("Price Distribution in Queens")
plt.show()


# In[32]:


df1 = df[df.neighbourhood_group == "Staten Island"][["neighbourhood","price"]]
f,ax = plt.subplots(figsize=(10,5))
d = df1.groupby("neighbourhood").mean()
sns.distplot(d)
ax.set_title("Price Distribution in Staten Island")
plt.show()


# In[33]:


df1 = df[df.neighbourhood_group == "Bronx"][["neighbourhood","price"]]
f,ax = plt.subplots(figsize=(10,5))
d = df1.groupby("neighbourhood").mean()
sns.distplot(d)
ax.set_title("Price Distribution in Bronx")
plt.show()


# In[34]:


f,ax = plt.subplots(figsize=(12,5))
ax = sns.countplot(df.room_type,palette="muted")
ax.set_title("Number of dfferent types of rooms")
plt.show()


# In[41]:


df1 = df[df.room_type=='Private room']['price']
f,ax = plt.subplots(figsize=(15,5))
ax.set_title("Price of a private room")
ax = sns.distplot(df1)
plt.show()


# In[47]:


df1 = df[df.room_type=='Shared room']['price']
f,ax = plt.subplots(figsize=(15,5))
ax.set_title("Price of a shared room")
ax = sns.distplot(df1)
plt.show()


# In[50]:


df1 = df[df.room_type=='Entire home/apt room_type']['price']
f,ax = plt.subplots(figsize=(15,5))
ax.set_title("Price of a entire home/apartment")
ax = sns.distplot(df1)
plt.show()


# In[40]:


df1 = df[df.room_type == "Private room"][["neighbourhood_group","price"]]
f,ax = plt.subplots(figsize=(7,5))
ax.set_title("Price of a private room in a neighbourhood")
d = df1.groupby("neighbourhood_group").mean()
sns.distplot(d)
plt.show()


# In[51]:


df1 = df[df.room_type == "Shared room"][["neighbourhood_group","price"]]
f,ax = plt.subplots(figsize=(7,5))
ax.set_title("Price of a shared room in a neighbourhood")
d = df1.groupby("neighbourhood_group").mean()
sns.distplot(d)
plt.show()


# In[52]:


df1 = df[df.room_type == "Entire home/apt room_type"][["neighbourhood_group","price"]]
f,ax = plt.subplots(figsize=(7,5))
ax.set_title("Price of a entire home/apartment in a neighbourhood")
d = df1.groupby("neighbourhood_group").mean()
sns.distplot(d)
plt.show()


# In[42]:


f,ax = plt.subplots(figsize=(15,5))
ax.set_title("Duration of availability of room")
ax = sns.distplot(df.availability_365)
plt.show()


# In[43]:


f,ax = plt.subplots(figsize=(16,8))
ax.set_title("Scatter Plot of Longitude vs Latitude (representing different neighbourhood groups)")
ax = sns.scatterplot(y=df.latitude,x=df.longitude,hue=df.neighbourhood_group,palette="coolwarm")
plt.show()


# In[46]:


f,ax = plt.subplots(figsize=(16,8))
ax.set_title("Longitude vs Latitude (representing availability of rooms)")
ax = sns.scatterplot(y=df.latitude,x=df.longitude,hue=df.availability_365,palette="coolwarm")
plt.show()


# In[ ]:




