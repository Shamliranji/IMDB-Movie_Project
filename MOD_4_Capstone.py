#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


Imdb=pd.read_csv('C:/Users/dranj/Downloads/IMDBMovie.csv')


# In[3]:


Imdb


# In[12]:


Imdb.describe()


# In[13]:


Imdb.isna().sum()


# In[14]:


Imdb.loc[(Imdb["Revenue_millions"]>75)].count()


# In[15]:


Imdb.loc[(Imdb["Revenue_millions"]>50)&(Imdb["Rating"]<7)].count()


# In[16]:


Year_Group=Imdb.groupby(by=["Year"])
Year_Group["Revenue_millions"].sum()


# In[17]:


Adv_Rating=Imdb.loc[(Imdb["Year"]==2015)&(Imdb["Genre"]=="Adventure")]
Adv_Rating["Rating"].mean()


# In[18]:


Avg_Run=Imdb.loc[75:149,"Runtime_minutes"]
Avg_Run.mean()


# In[19]:


#What is the maximum revenue out of (10,20,30,40,50) rows?
max_revenue=Imdb.loc[0:50:10,"Revenue_millions"]
max_revenue


# In[20]:


Imdb["Genre"].isin(["Action","Adventure","Crime","Horror"]).sum()


# In[21]:


Genre_agg = Imdb.groupby(by=["Genre"]).agg({"Votes":'mean',"Revenue_millions":'mean',"Rating":'mean'})
round(Genre_agg,2)


# In[22]:


Genre_year=Imdb.groupby(by=["Year","Genre"])
Revenue_per_year=Genre_year["Revenue_millions"].sum()
Revenue_per_year


# In[23]:


Total_Revenue = pd.merge(Imdb,Revenue_per_year,left_on=["Year","Genre"],right_on=["Year","Genre"])


# In[5]:


Total_Revenue


# In[86]:


def revenue_byeach_movie(Revenue_millions_x,Revenue_millions_y):
    if Revenue_millions_y == 0:
      return "Division by zero is not allowed"
    Total_rev =  Revenue_millions_x * 100 / (Revenue_millions_y)
    return Total_rev


# In[7]:


Total_Revenue["Total_Revenue"]=Total_Revenue.apply(lambda x:revenue_byeach_movie(x['Revenue_millions_x'],
                                                                                 x['Revenue_millions_y']),axis=1)


# In[8]:


Total_Revenue


# In[82]:


Split_rev =Total_Revenue.loc[Total_Revenue["Title"].isin(["Split"]),:]
round(Split_rev,2)


# In[91]:


Total_Revenue["Votes"].min()


# In[92]:


Total_Revenue["Votes"].max()


# In[95]:


def Vote_norm(Votes):
    Vote =(Votes - 61)*10/(1791916 - 61)
    return Vote


# In[96]:


Total_Revenue["Vote_Norms"]=Total_Revenue.apply(lambda x:Vote_norm(x["Votes"]),axis=1)


# In[97]:


Total_Revenue


# In[101]:


vote_norm=Total_Revenue["Vote_Norms"].mean()
round(vote_norm,2)


# In[103]:


Total_Revenue["Total_rating"]=Total_Revenue.apply(lambda x:x["Rating"]+x["Vote_Norms"],axis=1)


# In[104]:


Total_Revenue


# In[105]:


Total_Revenue["Total_rating"].max()


# In[33]:


def Revenue_bin(Revenue_millions_x):
    if Revenue_millions_x >=0 and Revenue_millions_x< 50:
     return "0-50"
    elif Revenue_millions_x >=50 and Revenue_millions_x < 100:
     return "50-100"
    elif Revenue_millions_x >=100 and Revenue_millions_x <150:
     return "100-150"
    else:
     return  "Above-150"


# In[34]:


Total_Revenue["Revenue_bins"]=Total_Revenue.apply(lambda x:Revenue_bin(x["Revenue_millions_x"]),axis=1)


# In[35]:


Total_Revenue


# In[36]:


Total_Revenue.groupby(by=["Revenue_bins"])["ID"].count()


# In[90]:


director_genre=Total_Revenue.groupby(by=["Director"])["Genre"].nunique()
director_genre


# In[93]:


max_director = director_genre.sort_values(ascending=False)
max_director


# In[ ]:




