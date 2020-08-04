#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd


# In[20]:


may2020_path = r"C:\Users\jimkn\Desktop\Trips_by_Distance_May_2020.csv"
May_2020_Travel = pd.read_csv(may2020_path)
May_2020_Travel = May_2020_Travel.drop(["State FIPS", "County FIPS", "Population Staying at Home", "Population Not Staying at Home"], axis=1)
May_2020_Travel.head()


# In[21]:


may2019_path = r"C:\Users\jimkn\Desktop\Trips_by_Distance_May_2019.csv" 
May_2019_Travel = pd.read_csv(may2019_path)
May_2019_Travel = May_2019_Travel.drop(["State FIPS", "County FIPS", "Population Staying at Home", "Population Not Staying at Home"], axis=1)
May_2019_Travel.head()


# In[22]:


June2020_path = r"C:\Users\jimkn\Downloads\Trips_by_Distance (4).csv"
June_2020_Travel = pd.read_csv(June2020_path)
June_2020_Travel = June_2020_Travel.drop(["State FIPS", "County FIPS", "Population Staying at Home", "Population Not Staying at Home"], axis=1)
June_2020_Travel.head()


# In[23]:


April2020_path = r"C:\Users\jimkn\Downloads\Trips_by_Distance (6).csv"
April_2020_Travel = pd.read_csv(April2020_path)
April_2020_Travel = April_2020_Travel.drop(["State FIPS", "County FIPS", "Population Staying at Home", "Population Not Staying at Home"], axis=1)
April_2020_Travel.head()


# In[24]:


April2019_path = r"C:\Users\jimkn\Downloads\Trips_by_Distance (7).csv"
April_2019_Travel = pd.read_csv(April2019_path)
April_2019_Travel = April_2019_Travel.drop(["State FIPS", "County FIPS", "Population Staying at Home", "Population Not Staying at Home"], axis=1)
April_2019_Travel.head()


# In[25]:


June2019_path = r"C:\Users\jimkn\Downloads\Trips_by_Distance (8).csv"
June_2019_Travel = pd.read_csv(June2019_path)
June_2019_Travel = June_2019_Travel.drop(["State FIPS", "County FIPS", "Population Staying at Home", "Population Not Staying at Home"], axis=1)
June_2019_Travel.head()


# In[37]:


last_year_frames = [April_2019_Travel, May_2019_Travel, June_2019_Travel]
last_year_traffic = pd.concat(last_year_frames)
lytraffic = last_year_traffic.drop([88], axis=0)
lytraffic


# In[38]:


current_year_traffic = [April_2020_Travel, May_2020_Travel, June_2020_Travel]
current_year_traffic = pd.concat(last_year_frames)
cytraffic = last_year_traffic.drop([88], axis=0)
cytraffic


# In[ ]:




