#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('E:\Smester 3\IDS_Theory/Dummy_Sales_Data_v1.csv')
## by using this function we will get first 5 rows fo our dataset
df.head()


# In[2]:


##we can take as required rows by giving an integer in head function
df.head(7)


# In[3]:


## by using this function we will get last 5 rows fo our dataset and giving an integer in this function we can get specific last rows of our data
df.tail()


# In[4]:


##this function will slect a random row from our data set
df.sample()


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.loc[75,'Quantity']


# In[8]:


df["Quantity"].unique()


# In[9]:


##as same like database wo can access the required value tha we need as i did i want to see all the columns which valueis greater than 100
df.query("Quantity < 100")


# In[10]:


##this fumction will give all tha values that are not diffrent in table
df["Shipping_Cost(USD)"].nunique()


# In[11]:


##this funtion write the all negative value of the table or a one or more column
df.isnull()


# In[12]:


## we can write any value where isnull
df.fillna("10_	Quantity")


# In[13]:


##we can sort values the whole table on base of a attribute
df.sort_values(by= 'Quantity' , ascending = True)


# In[17]:


##this function write the unique values
df.value_counts('Quantity')


# In[18]:


## by using this function we can print the biigest value of column
df.nlargest(3 , 'Quantity')


# In[ ]:




