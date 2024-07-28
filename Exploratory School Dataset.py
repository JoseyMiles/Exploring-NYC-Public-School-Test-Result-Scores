#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[2]:


schools = pd.read_csv("schools.csv")


# In[3]:


schools.head()


# In[17]:


len(schools)


# In[20]:


schools.info()


# In[4]:


# To print the schools with the best math scores which is 640 and above
best_math_schools = schools[schools["average_math"] >=640][["school_name", "average_math"]].sort_values("average_math", ascending= False)
best_math_schools


# In[5]:


# Plotting the data
plt.figure(figsize=(8, 3))
bars = plt.bar(best_math_schools['school_name'], best_math_schools['average_math'])


# Rotate the x-axis labels
plt.xticks(rotation=35, ha='right')  # Rotate 45 degrees and align to the right

# Adding labels and title
plt.xlabel('School names')
plt.ylabel('Average Math Scores')
plt.title('Schools with math scores above 640')

# Adding values on top of the bars
for bar in bars:
    height = bar.get_height()
    plt.annotate('{}'.format(height),
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom')

# Show the plot
plt.tight_layout()  # Adjust layout to prevent clipping of labels

# Save the plot as a PNG file
plt.savefig('Schools with high math scores.png', format='png')
plt.show()


# In[6]:


# Finding the total scores when the subjects are added together
schools["total_SAT"]= schools["average_math"] + schools["average_reading"] + schools["average_writing"]

# Sort by total_SAT
schools_sorted = schools.sort_values(by="total_SAT", ascending=False)
schools_sorted.head()


# In[7]:


# Finding the top 10 schools
top_10_schools = schools.groupby("school_name", as_index= False)["total_SAT"].mean().sort_values("total_SAT", ascending = False).head(10)
top_10_schools


# In[8]:


# Plotting the data for top 10 schools
plt.figure(figsize=(8, 3))
bars = plt.bar(top_10_schools['school_name'], top_10_schools['total_SAT'])


# Rotate the x-axis labels
plt.xticks(rotation=35, ha='right')  # Rotate 45 degrees and align to the right

# Adding labels and title
plt.xlabel('School names')
plt.ylabel('Total SAT')
plt.title('Top 10 schools based on SAT scores')

# Adding values on top of the bars
for bar in bars:
    height = bar.get_height()
    plt.annotate('{}'.format(height),
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom')

# Show the plot
plt.tight_layout()  # Adjust layout to prevent clipping of labels

# Save the plot as a PNG file
plt.savefig('Top 10 schools with SAT.png', format='png')
plt.show()


# In[9]:


# Finding the bottom 10 schools
bottom_10_schools = schools.groupby("school_name", as_index= False)["total_SAT"].mean().sort_values("total_SAT", ascending = True).head(10)
bottom_10_schools


# In[10]:


# Plotting the data for bottom 10 schools
plt.figure(figsize=(8, 3))
bars = plt.bar(bottom_10_schools['school_name'], bottom_10_schools['total_SAT'])


# Rotate the x-axis labels
plt.xticks(rotation=35, ha='right')  # Rotate 45 degrees and align to the right

# Adding labels and title
plt.xlabel('School names')
plt.ylabel('Total SAT')
plt.title('Bottom 10 schools based on SAT scores')

# Adding values on top of the bars
for bar in bars:
    height = bar.get_height()
    plt.annotate('{}'.format(height),
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom')

# Show the plot
plt.tight_layout()  # Adjust layout to prevent clipping of labels

# Save the plot as a PNG file
plt.savefig('Bottom 10 schools with SAT.png', format='png')
plt.show()


# In[11]:


# Grouping the schools by borough to determine the boroughs that are doing well
boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)
boroughs = boroughs.rename(columns = {"count":"num_schools", "mean": "average_SAT", "std": "std_SAT"})
boroughs


# In[12]:


# Visualizing the data without value labels
fig, ax = plt.subplots(1, 3, figsize=(18, 6))

# Bar chart for count_SAT
boroughs['num_schools'].plot(kind='bar', ax=ax[0], color='skyblue')
ax[0].set_title('Number of Schools by Borough')
ax[0].set_xlabel('Borough')
ax[0].set_ylabel('Count of Schools')

# Bar chart for average_SAT
boroughs['average_SAT'].plot(kind='bar', ax=ax[1], color='lightgreen')
ax[1].set_title('Average SAT Scores by Borough')
ax[1].set_xlabel('Borough')
ax[1].set_ylabel('Average SAT Score')

# Bar chart for std_SAT
boroughs['std_SAT'].plot(kind='bar', ax=ax[2], color='salmon')
ax[2].set_title('Standard Deviation of SAT Scores by Borough')
ax[2].set_xlabel('Borough')
ax[2].set_ylabel('Standard Deviation of SAT Scores')

plt.tight_layout()
plt.show()


# In[13]:


# Visualizing the data with value labels
fig, ax = plt.subplots(1, 3, figsize=(18, 6))

# Plotting and adding labels
for i, col in enumerate(['num_schools', 'average_SAT', 'std_SAT']):
    bars = boroughs[col].plot(kind='bar', ax=ax[i], color=['blue', 'green', 'orange'][i])
    ax[i].set_title(f'{col.replace("_", " ").title()} by Borough')
    ax[i].set_xlabel('Borough')
    ax[i].set_ylabel(col.replace("_", " ").title())
    ax[i].tick_params(axis='x', rotation=45)
    
    # Adding value labels on the bars
    for bar in bars.containers[0]:
        height = bar.get_height()
        ax[i].annotate('{}'.format(height),
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3),  # 3 points vertical offset
                       textcoords="offset points",
                       ha='center', va='bottom')

plt.tight_layout()
plt.show()


# In[14]:


# Getting the boroughs with the largest standard deviation
largest_std_dev = boroughs[boroughs["std_SAT"] == boroughs["std_SAT"].max()]
largest_std_dev


# In[15]:


# To rename the columns according to interest
largest_std_dev= largest_std_dev.rename(columns = {"num_schools":"num_schools", "average_SAT": "average_SAT", "std_SAT": "std_SAT"})
largest_std_dev


# In[ ]:




