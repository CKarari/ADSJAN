#!/usr/bin/env python
# coding: utf-8

# ## Pandas
# 
# ### Instructions
# 
# This assignment will be done completely inside this Jupyter notebook with answers placed in the cell provided.
# 
# All python imports that are needed shown.
# 
# Follow all the instructions in this notebook to complete these tasks.    
# 
# Make sure the CSV data files is in the same folder as this notebook - alumni.csv, groceries.csv

# In[1]:


# Imports needed to complete this assignment
import pandas as pd


# ### Question 1 :  Import CSV file (1 Mark)
# 
# 
# Write code to load the alumni csv dataset into a Pandas DataFrame called 'alumni'.
# 

# In[2]:


#q1 (1)
alumni = pd.read_csv("alumni.csv")


# ### Question 2 :  Understand the data set (5 Marks)
# 
# Use the following pandas commands to understand the data set: a) head, b) tail, c) dtypes, d) info, e) describe 

# In[3]:


#a) (1)
alumni.head()


# In[4]:


#b) (1)
alumni.tail()


# In[5]:


#c) (1)
type(alumni)


# In[6]:


#d) (1)
alumni.info()


# In[7]:


#e) (1)
alumni.describe()


# ### Question 3 :  Cleaning the data set - part A (3 Marks)
# 
# a) Use clean_currency method below to strip out commas and dollar signs from Savings ($) column and put into a new column called 'Savings'.

# In[8]:


def clean_currency(curr):
    return float(curr.replace(",", "").replace("$", ""))

clean_currency("$66,000")
 


# In[9]:


#a) (2)


# b) Uncomment 'alumni.dtypes.Savings' to check that the type change has occurred

# In[10]:


#b) (1)
# alumni.dtypes.Savings


# ### Question 4 :  Cleaning the data set - part B (5 Marks)
# 
# a) Run the 'alumni["Gender"].value_counts()' to see the incorrect 'M' fields that need to be converted to 'Male'

# In[11]:


# a) (1)
alumni.value_counts("Gender")


# b) Now use a '.str.replace' on the 'Gender' column to covert the incorrect 'M' fields. Hint: We must use ^...$ to restrict the pattern to match the whole string. 

# In[12]:


# b) (1)
alumni['Gender'] = alumni['Gender'].replace({'M':'Male'})


# In[13]:


# b) (1)


# c) That didn't the set alumni["Gender"] column however. You will need to update the column when using the replace command 'alumni["Gender"]=<replace command>', show how this is done below

# In[14]:


# c) (1)


# d) You can set it directly by using the df.loc command, show how this can be done by using the 'df.loc[row_indexer,col_indexer] = value' command to convert the 'M' to 'Male'

# In[15]:


# d) (1)


# e) Now run the 'value_counts' for Gender again to see the correct columns - 'Male' and 'Female' 

# In[16]:


# e) (1)


# ### Question 5 :  Working with the data set (4)
# 
# a) get the median, b) mean and c) standard deviation for the 'Salary' column

# In[20]:


# a)(1)
alumni["Salary"].median()


# In[21]:


# b)(1)
alumni["Salary"].mean()


# In[22]:


# c)(1)
alumni["Salary"].std()


# d) identify which alumni paid more than $15000 in fees, using the 'Fee' column

# In[24]:


# d) (1)
paid_above_15000 = alumni[alumni["Fee"] > 15000]
paid_above_15000.count()


# ### Question 6 :  Visualise the data set (4 Marks)
# 
# a) Using the 'Diploma Type' column, plot a bar chart and show its value counts.

# In[25]:


#a) (1)
alumni['Diploma Type'].value_counts().plot(kind='bar')


# b) Now create a box plot comparison between 'Savings' and 'Salary' columns

# In[32]:


#b) (1)
alumni.boxplot("Salary")


# c) Generate a histogram with the 'Salary' column and use 12 bins.

# In[37]:


#c) (1)
alumni.hist(column=["Salary"],bins=12)


# d) Generate a scatter plot comparing 'Salary' and 'Savings' columns.

# In[42]:


#d) (1)
alumni.plot.scatter(x="Salary", y="Fee")


# ### Question 7 :  Contingency Table (2 Marks)
# 
# Using both the 'Martial Status' and 'Defaulted' create a contingency table. Hint: crosstab

# In[56]:


# Q7 (2)
pd.crosstab(alumni['Marital Status'], alumni['Defaulted'])

