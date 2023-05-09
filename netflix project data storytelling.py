#!/usr/bin/env python
# coding: utf-8

# # Netflix Project
# 

# Import Pandas as pd and read the file into a Pandas DataFrame.

# In[13]:


import pandas as pd
df = pd.read_csv('ViewingActivity.csv')


# First, let's understand how many rows & columns we have using 

# In[14]:


#returns the number of rows and columns
df.shape     


# Let's have a closer look at the first rows of the dataset

# In[15]:


#returns the first 5 rows
df.head() 


# Additionally, let's get some random sample rows for a further first understanding of the data.

# In[16]:


#returns a random sample of 10 rows
df.sample(n=10)


# In[17]:


df["Profile Name"].unique()


# In[18]:


df["Device Type"].unique()


# In[19]:


df["Title"].unique()


# In[20]:


df["Start Time"].unique()


# In[21]:


df["Duration"].unique()


# In[22]:


df.dtypes


# In[23]:


df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
df['Duration'] = pd.to_timedelta(df['Duration'])
df.dtypes


# In[29]:


df.sort_values('Start Time')


# In[24]:


df.sample(n=10)     #returns a random sample of 10 rows

