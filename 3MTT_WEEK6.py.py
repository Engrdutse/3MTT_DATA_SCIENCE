
# coding: utf-8

# # importing Pandas library

# In[ ]:


import pandas as pd


# In[ ]:


messy_data = pd.read_csv('Airbnb_India_Top_500.csv')


# In[83]:


messy_data.head(5)


# In[ ]:


#Check for missing values:


# In[53]:


print(messy_data.isnull().sum())


# In[16]:


messy_data.tail(5)


# In[19]:


list(messy_data.columns)


# In[ ]:


#Creating a copy of the messy data for cleaning


# In[84]:


data1 = messy_data.copy()


# In[85]:


data1.head(5)


# #Renaming Columns Names

# In[86]:


data1 = data1.rename(columns={'numberOfGuests': 'Accommodation capacity'})


# In[87]:


clean_data1.head(3)


# In[88]:


data1 = data1.rename(columns={'name': 'Title of the Listing'})


# In[89]:


data1.head(3)


# In[90]:


data1 = data1.rename(columns={'stars': 'Rating', 'address': 'Address'})


# In[93]:


data1.head(5)


# In[ ]:


#Remove irrelevant columns:


# In[95]:


data1.drop(['isHostedBySuperhost'], axis=1, inplace=True)


# In[96]:


data1.head(3)


# # Filling the missing data in Rating Column

# In[101]:


data1['Rating'].head(5)


# In[ ]:


#To calculate the average Star rating we import Numerical python 'Numpy'


# In[99]:


import numpy as np


# In[102]:


data1["Rating"].mean()


# In[103]:


avr_rating = data1["Rating"].mean()


# In[ ]:


#Using average to fill the missing Rating column data


# In[104]:


avr_rating


# In[110]:


data1['Rating'].fillna(value=avr_rating, inplace=True)


# In[111]:


data1.head(3)


# In[112]:


print(data1.isnull().sum())


# In[ ]:


#Now our data1 is clean


# In[ ]:


# hence lets copy the data to clean container


# In[113]:


clean_data = data1.copy()


# In[114]:


clean_data.head(20)

