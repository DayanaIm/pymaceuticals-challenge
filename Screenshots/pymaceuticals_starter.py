#!/usr/bin/env python
# coding: utf-8

# # Pymaceuticals Inc.
# ---
# 
# ### Analysis
# 
# - Add your analysis here.
#  

# In[88]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import numpy as np

# Study data files
mouse_metadata_path = "data/Mouse_metadata.csv"
study_results_path = "data/Study_results.csv"

# Read the mouse data and the study results
mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)

# Combine the data into a single DataFrame
combined_data = pd.merge(study_results,mouse_metadata, how="outer", on="Mouse ID")

# Display the data table for preview
combined_data


# In[89]:


# Checking the number of mice.
number_mice = combined_data["Mouse ID"].nunique()
number_mice


# In[90]:


type(combined_data)


# In[91]:


# Our data should be uniquely identified by Mouse ID and Timepoint
# Get the duplicate mice by ID number that shows up for Mouse ID and Timepoint. 
dupe_mouse_id = combined_data.loc[combined_data.duplicated(subset=["Mouse ID", "Timepoint"]),'Mouse ID'].unique()
dupe_mouse_id


# In[92]:


# Optional: Get all the data for the duplicate mouse ID. 
dupe_mouse_data = combined_data.loc[combined_data["Mouse ID"].isin(dupe_mouse_id)]
dupe_mouse_data


# In[93]:


# Create a clean DataFrame by dropping the duplicate mouse by its ID.

clean_data = combined_data[combined_data['Mouse ID'].isin(dupe_mouse_id)==False]
clean_data


# In[94]:


type(clean_data)


# In[95]:


# Checking the number of mice in the clean DataFrame.
number_of_mice_cleaned = clean_data["Mouse ID"].nunique()
number_of_mice_cleaned


# ## Summary Statistics

# In[96]:


# A more advanced method to generate a summary statistics table of mean, median, variance, standard deviation,
# and SEM of the tumor volume for each regimen (only one method is required in the solution)

# Using the aggregation method, produce the same summary statistics in a single line


summary_aggregation =  clean_data.groupby(['Drug Regimen'])[['Tumor Volume (mm3)']].agg(['mean', 'median', 'var', 'std', 'sem'])
summary_aggregation


# In[97]:


# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen

# Use groupby and summary statistical methods to calculate the following properties of each drug regimen: 
# mean, median, variance, standard deviation, and SEM of the tumor volume. 

mean = clean_data["Tumor Volume (mm3)"].groupby(clean_data["Drug Regimen"]).mean()
median = clean_data["Tumor Volume (mm3)"].groupby(clean_data["Drug Regimen"]).median()
variance = clean_data["Tumor Volume (mm3)"].groupby(clean_data["Drug Regimen"]).var()
standard_deviation = clean_data["Tumor Volume (mm3)"].groupby(clean_data["Drug Regimen"]).std()
standard_erorr = clean_data["Tumor Volume (mm3)"].groupby(clean_data["Drug Regimen"]).sem()

# Assemble the resulting series into a single summary DataFrame.

summary_statistics = pd.DataFrame({"Mean Tumor Volume":mean, 
                             "Median Tumor Volume":median, 
                             "Tumor Volume Variance":variance, 
                             "Tumor Volume Std. Dev.":standard_deviation, 
                             "Tumor Volume Std. Err.":standard_erorr
                            })
summary_statistics


# ## Bar and Pie Charts

# In[125]:


# Generate a bar plot showing the total number of rows (Mouse ID/Timepoints) for each drug regimen using Pandas.

regimen_counts = clean_data['Drug Regimen'].value_counts()
regimen_counts.plot(kind='bar', figsize=(6, 5), color='b', alpha= 0.65, width=.75)

plt.xlabel('Drug Regimen')
plt.ylabel('# of Observed Mouse Timepoints')
plt.tight_layout()
plt.show()


# In[126]:


# Generate a bar plot showing the total number of rows (Mouse ID/Timepoints) for each drug regimen using pyplot.

drug_regimens = regimen_counts.index
number_observed = regimen_counts.values

plt.figure(figsize=(6, 5))
plt.bar(drug_regimens, number_observed, color='b', alpha= 0.65, width=.75)

plt.xlabel('Drug Regimen')
plt.ylabel('# of Observed Mouse Timepoints')
plt.xticks(rotation='vertical')
plt.tight_layout()
plt.show()


# In[141]:


# Generate a pie plot showing the distribution of female versus male mice using Pandas
gender = clean_data['Sex'].value_counts()
explode = (0 , 0.1)
plt.figure(figsize=(5, 5))
gender.plot(kind='pie', autopct='%1.1f%%', colors=['blue', 'orange'],shadow=True, explode = explode)

plt.ylabel('Sex') 
plt.show()


# In[142]:


# Generate a pie plot showing the distribution of female versus male mice using pyplot

plt.pie(gender, labels=gender.index, autopct='%1.1f%%', colors=['blue', 'orange'],shadow=True, explode = explode)

plt.ylabel('Sex') 
plt.show()


# ## Quartiles, Outliers and Boxplots

# In[152]:


# Calculate the final tumor volume of each mouse across four of the treatment regimens:  
# Capomulin, Ramicane, Infubinol, and Ceftamin

selected_regimens = clean_data[clean_data['Drug Regimen'].isin(['Capomulin', 'Ramicane', 'Infubinol', 'Ceftamin'])]

# Start by getting the last (greatest) timepoint for each mouse

greatest_timepoint = selected_regimens.groupby('Mouse ID')['Timepoint'].max().reset_index()

# Merge this group df with the original DataFrame to get the tumor volume at the last timepoint

final_tumor_volume = pd.merge(greatest_timepoint, selected_regimens, on=['Mouse ID', 'Timepoint'], how='left')

#print(final_tumor_volume[['Mouse ID', 'Drug Regimen', 'Tumor Volume (mm3)']])


# In[ ]:





# In[153]:


print(final_tumor_volume[['Mouse ID', 'Drug Regimen', 'Tumor Volume (mm3)']])


# In[14]:


# Put treatments into a list for for loop (and later for plot labels)


# Create empty list to fill with tumor vol data (for plotting)


# Calculate the IQR and quantitatively determine if there are any potential outliers. 

    
    # Locate the rows which contain mice on each drug and get the tumor volumes

    
    # add subset 

    
    # Determine outliers using upper and lower bounds


# In[15]:


# Generate a box plot that shows the distrubution of the tumor volume for each treatment group.


# ## Line and Scatter Plots

# In[16]:


# Generate a line plot of tumor volume vs. time point for a single mouse treated with Capomulin


# In[17]:


# Generate a scatter plot of mouse weight vs. the average observed tumor volume for the entire Capomulin regimen


# ## Correlation and Regression

# In[18]:


# Calculate the correlation coefficient and a linear regression model 
# for mouse weight and average observed tumor volume for the entire Capomulin regimen


# In[ ]:




