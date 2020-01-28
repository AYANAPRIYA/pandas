#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd


# In[31]:


people = {
    "first" : ["corey", "Jane", "John"],
    "last" : ["Schafer", "Doe", "Doe"],
    "email": ["coreyscafer@gmail.com", "janedoe@gmail.com", "JohnDoe@gmail.com"]
}


# In[32]:


people['email']


# In[33]:


df = pd.DataFrame(people)


# In[84]:


df


# In[51]:


df['email']


# In[52]:


#type(df['email'])


# In[53]:


#df.email


# In[55]:


df.columns


# In[76]:


df.iloc[[0, 1],2]


# In[80]:


df.loc[[0,1], ['email', 'last']]


# In[82]:


df.set_index('email')


# In[85]:


df.loc[0]


# In[99]:


filt = (df['last'] == 'Doe') & (df['first']== 'John')


# In[101]:


df.loc[filt, 'email']


# In[102]:


df[filt]


# In[ ]:




