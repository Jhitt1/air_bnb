#!/usr/bin/env python
# coding: utf-8

# # AirBnB NY Locations Data Case Study
# 
# Your task will be to take the data provided and find evidence to answer the following questions.
# 
# 1. Which hosts are the busiest and why?
# 2. How many neighborhood groups are available and which shows up the most?
# 3. Are private rooms the most popular in manhattan?
# 4. Which hosts are the busiest and based on their reviews?
# 5. Which neighorhood group has the highest average price?
# 6. Which neighborhood group has the highest total price?
# 7. Which top 5 hosts have the highest total price?
# 8. Who currently has no (zero) availability with a review count of 100 or more?
# 9. What host has the highest total of prices and where are they located?
# 10. When did Danielle from Queens last receive a review?
# 
# This is to simulate what you will face when you are out in the wild. 
# 
# Happy Coding!

# In[114]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime


# In[120]:


air_bnb = pd.read_csv('AB_NYC_2019.csv')
air_bnb.head()
air_bnb['last_review'] = pd.to_datetime(air_bnb['last_review']) #Setting the last_review column to a datetime type


# In[179]:


#Whic hosts are the busiest and why?
hosts = air_bnb.groupby('host_id').calculated_host_listings_count.count().nlargest(5)
hosts


# In[180]:


# How many neighborhood groups are available and which shows up the most?
air_bnb.neighbourhood_group.unique() # 5
air_bnb.groupby('neighbourhood_group').neighbourhood_group.count().nlargest(5) # Manhattan


# In[30]:


# Are private rooms the most popular in manhattan? Nah. It's Entire home/apt
manhattan_query = air_bnb.query("neighbourhood_group == 'Manhattan'")
manhattan_query.room_type.value_counts()


# In[181]:


# Which hosts are the busiest and based on their reviews? Michael getting big checks with 417 reviews
by_host = air_bnb.groupby('host_id').count()
by_host.sort_values(by=['number_of_reviews'], ascending=False).head(5)


# In[187]:


#Which neighorhood group has the highest average price? Manhattan
neighbor = air_bnb.groupby('neighbourhood_group').mean()
neighbor['price'].nlargest(5)


# In[188]:


# Which neighbor hood group has the highest total price? Manhattan with $4,264,527
# air_bnb.sort_values(by=['price'], ascending=False)
neighborhood_total = air_bnb.groupby('neighbourhood_group').sum()
neighborhood_total['price'].nlargest(5)


# In[184]:


#Which 5 hosts have the highest total price?
host_total_price = air_bnb.groupby('host_id').sum()
host_total_price.sort_values(by=['price'], ascending=False).head(5)


# In[190]:


# Who currently has no (zero) availability with a review count of 100 or more?
no_availability = air_bnb.loc[(air_bnb['availability_365'] == 0) & (air_bnb['number_of_reviews'] >= 100)] # < All those fools
no_availability


# In[191]:


# What host has the highest total of prices and where are they located? #Sonder in Manhattan - HostID of 219517861
host_and_where = air_bnb.groupby(['host_id', 'neighbourhood_group']).sum()
host_and_where.sort_values(by=['price'], ascending=False).head(5)


# In[121]:


# When did Danielle from Queens last receive a review? # July 8th, 2019
the_danielles = air_bnb.loc[(air_bnb['host_name'] == 'Danielle') & (air_bnb['neighbourhood_group'] == 'Queens')]
the_danielles['last_review'].max()


# ## Further Questions
# 
# 1. Which host has the most listings?

# In[158]:


#Sonder in Manhattan has the most with 327
host_list_sums = air_bnb.groupby(['host_name', 'neighbourhood_group']).max()
host_list_sums.sort_values(by=['calculated_host_listings_count'], ascending=False).head()
#not sure why I am getting an error here


# 2. How many listings have completely open availability?

# In[165]:


# 1295 listings have 365 days of availability
three_six_five_listings = air_bnb.loc[air_bnb['availability_365'] == 365]
three_six_five_listings['availability_365'].count()


# 3. What room_types have the highest review numbers?

# In[176]:


# Entire Home/Apt layouts have the highest number of reviews
rooms = air_bnb.groupby('room_type').sum()
rooms['number_of_reviews']


# # Final Conclusion
# 
# In this cell, write your final conclusion for each of the questions asked.
# 
# Also, if you uncovered some more details that were not asked above, please discribe them here.
# 
# -- Add your conclusion --



