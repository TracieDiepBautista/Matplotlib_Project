# %% [markdown]
# # Pymaceuticals Inc.
# ---
# 
# ### Analysis
# * Your analysis here ...

# %%
# Dependencies and Setup

import os
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
from matplotlib import style
from matplotlib import pyplot as plt
from scipy.stats import linregress
from sklearn import datasets
from jupyterthemes import jtplot

#import seaborn as sns
#plt.style.use('seaborn-notebook')

# Study data files
mouse_metadata_path = "data/Mouse_metadata.csv"
study_results_path = "data/Study_results.csv"

# Read the mouse data and the study results
mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)

# Combine the data into a single dataset
mouse_study = pd.merge(study_results,mouse_metadata, how="left", on=["Mouse ID"])
mouse_study.head(20)

# %%
mouse_study.count()

# %%
# Display the data table for preview
organized_mouse_study = mouse_study[["Mouse ID","Timepoint","Tumor Volume (mm3)","Metastatic Sites","Drug Regimen",
                                     "Sex","Age_months","Weight (g)"]]
organized_mouse_study.head()
#organized_mouse_study.count()

# %%
# find out what is the duplciated item first: 
duplicate_mouse_id= organized_mouse_study.loc[organized_mouse_study.duplicated(subset=['Mouse ID', 'Timepoint']),'Mouse ID'].unique()
duplicate_mouse_id

# %%
# drop the duplicated mouse by isin function to have clean df | or can do: organized_mouse_study.loc[organized_mouse_study["Mouse ID"] !== "g989"]
# or: mouse_df = organized_mouse_study.drop_duplicates(subset=["Mouse ID"]): this is to drop all duplicated rows in df
mouse_df = organized_mouse_study[organized_mouse_study['Mouse ID'].isin(duplicate_mouse_id)==False]
mouse_df.head()

# %%
# Checking the number of mice.
mouse_unique = mouse_df["Mouse ID"].unique()
mouse_unique_number = len(mouse_unique)
mouse_unique_number

# %%
# Get all the data for the duplicate mouse ID. 

dupli_mouse_df = organized_mouse_study.loc[organized_mouse_study["Mouse ID"]== "g989"]
dupli_mouse_df.head()

# %% [markdown]
# ## Summary Statistics

# %%
# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen

# Use groupby and summary statistical methods to calculate the following properties of each drug regimen: 
# mean, median, variance, standard deviation, and SEM of the tumor volume. 
# Assemble the resulting series into a single summary dataframe.


# %%
means = mouse_df.groupby('Drug Regimen').mean()['Tumor Volume (mm3)']
medians = mouse_df.groupby('Drug Regimen').median()['Tumor Volume (mm3)']
var = mouse_df.groupby('Drug Regimen').var()['Tumor Volume (mm3)']
Dev = mouse_df.groupby('Drug Regimen').std()['Tumor Volume (mm3)']
SEMs = mouse_df.groupby('Drug Regimen').sem()['Tumor Volume (mm3)']

# %%
summary_table = pd.DataFrame({"Mean Tumor Volume":means, "Median Tumor Volume":medians, "Tumor Volume Variance":var,
                              "Tumor Volume Std":Dev, "Tumor Volume Std. Err.":SEMs})
summary_table.head(20)

# %%
# Generate a summary statistics table of mean, median, variance, standard deviation, 
# and SEM of the tumor volume for each regimen

# Using the aggregation method, produce the same summary statistics in a single line
summary_table_agg = summary_table.describe()
summary_table_agg.head()

# %% [markdown]
# ## Bar and Pie Charts

# %%
# Generate a bar plot showing the total number of unique mice tested on each drug regimen using pandas.
    #fig,ax = plt.subplot()
# Extract the neccessary values first:    

mice_plot_df = mouse_df.groupby("Drug Regimen").agg({"Tumor Volume (mm3)":["mean","median","var","std","sem"]})


mice_plot_df

# %%
mice_plot = mouse_df.groupby('Drug Regimen')["Mouse ID"].count()
mice_plot.head(15)

# %%
# create a bar plot using pandas showing the number of unique mice tested on each drug regimen
jtplot.style(theme = 'grade3', context='notebook', ticks=True, grid=False)
mice_plot.plot(kind = "bar")

# %%
mice_mouse = mouse_df[["Drug Regimen","Mouse ID","Sex"]]
mice_mouse.head()

# %%
# create a bar plot using pyplot showing the number of unique mice tested on each drug regimen

mice_mouse = mouse_df.groupby(["Drug Regimen"])["Mouse ID"].count()
mice_mouse.head()



# %%
# use .agg to get a df but same value output
mice_mousedf = mouse_df.groupby("Drug Regimen").agg({"Mouse ID":"count"})
mice_mousedf.head()

# %%
# using pyplot
x_Drug = mice_mousedf.index
y_Mice = mice_mousedf["Mouse ID"]
plt.bar(x_Drug, y_Mice, color='red', alpha=0.5, align="center")
plt.xticks(rotation="vertical")
plt.title("Number of Mice tested per each Drug")
#plt.xlabel("Drug")
plt.ylabel("Number of Mice")
plt.figure(figsize=(10,200))
#plt.savefig("Output/Education_states.png")
plt.show()


# %%
# optional: set the data for pandas plotting with mean and Drug
summary_plot_df = summary_table.reset_index()
summary_plot_df.head()


# %%
# Generate a pie plot showing the distribution of female versus male mice using pandas
# find the F and M number each Drug| put into a df | conditional code to sum up | plot

mice_pie = mouse_df.groupby("Sex").agg({"Sex":"value_counts"})
mice_pie

# %%
# ploting using pyplot
#jtplot.style(theme= “grade3”, context="notebook", ticks=True, grid=False)
#matplotlib.style.use('default')
x = ["Female","Male"]
y = [922,958]
colors = ["blue","orange"]
plt.pie(y, labels=x, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=180
       )
plt.show()


# %%
# # Generate a pie plot showing the distribution of female versus male mice using pandas

mice_pie.plot(kind='pie', subplots=True, figsize=(5, 5))
#mouse_df.groupby(['Sex']).values_count().plot(kind='pie', y='Sex')

# %% [markdown]
# ## Quartiles, Outliers and Boxplots

# %%
# Calculate the final tumor volume of each mouse across four of the treatment regimens:  
# Capomulin, Ramicane, Infubinol, and Ceftamin

# Start by getting the last (greatest) timepoint for each mouse


# groupy mouse ID and get .agg with max() in Timepoint

max_timepoint = mouse_df.groupby(mouse_df["Mouse ID"]).agg({"Timepoint":"max"})
max_timepoint

# Merge this group df with the original dataframe to get the tumor volume at the last timepoint
merge_time_mouse = pd.merge(max_timepoint,mouse_df, how="left", on=["Mouse ID","Timepoint"])
merge_time_mouse.head()


# %%
# extract the neccessary values out to a df for further works
extract = merge_time_mouse[["Mouse ID","Timepoint","Tumor Volume (mm3)","Drug Regimen","Weight (g)"]]
extract.head()

# %%
# groupby from extract
Mouse_group = extract.groupby(["Mouse ID"])["Tumor Volume (mm3)"].mean()
Mouse_group.head()


# %%
Drug_summary = extract.loc[(extract["Drug Regimen"] == "Capomulin") & (extract["Drug Regimen"] == "Ramicane") &
                          (extract["Drug Regimen"] == "Infubinol") & (extract["Drug Regimen"] == "Ceftamin")]
Drug_summary.head()

# %%
# extract the lists of tumor Volume per Drug

Capo_tumor = extract.loc[extract["Drug Regimen"]=="Capomulin","Tumor Volume (mm3)"]
Rami_tumor = extract.loc[extract["Drug Regimen"]=="Ramicane","Tumor Volume (mm3)"]
Infu_tumor = extract.loc[extract["Drug Regimen"]=="Infubinol","Tumor Volume (mm3)"]
Cef_tumor = extract.loc[extract["Drug Regimen"]=="Ceftemin","Tumor Volume (mm3)"]


# %%
# we can use the above tumor values to calculate quartiles | iqr | outlier

# %%
# extract mouse weights per Drug

Capo_weight = extract.loc[extract["Drug Regimen"]=="Capomulin","Weight (g)"]
Rami_weight = extract.loc[extract["Drug Regimen"]=="Ramicane","Weight (g)"]
Infu_weight = extract.loc[extract["Drug Regimen"]=="Infubinol","Weight (g)"]
Cef_weight = extract.loc[extract["Drug Regimen"]=="Ceftamin","Weight (g)"]
#print(Capo_weight)

# %%
#extract timepoint per Drug
Capo_timepoint = extract.loc[extract["Drug Regimen"]=="Capomulin","Timepoint"]
Rami_timepoint = extract.loc[extract["Drug Regimen"]=="Ramicane","Timepoint"]
Infu_timepoint = extract.loc[extract["Drug Regimen"]=="Infubinol","Timepoint"]
Cef_timepoint = extract.loc[extract["Drug Regimen"]=="Ceftamin","Timepoint"]
#print(Capo_timepoint)

# %% [markdown]
# 

# %%
#extract the lists of Mouse ID per Drug
Capo_mice = extract.loc[extract["Drug Regimen"]=="Capomulin","Mouse ID"]
Rami_mice = extract.loc[extract["Drug Regimen"]=="Ramicane","Mouse ID"]
Infu_mice = extract.loc[extract["Drug Regimen"]=="Infubinol","Mouse ID"]
Cef_mice = extract.loc[extract["Drug Regimen"]=="Ceftamin","Mouse ID"]
#print(len(Capo_mice) + len(Rami_mice)+ len(Infu_mice)+len(Cef_mice))
#print(Capo_mice)

# %%
# put the results into a df to make it clear to view: 

Capo_summary = pd.DataFrame({"Tumor Volume (mm3)": Capo_tumor,
                                 "Mouse Weights (g)": Capo_weight,
                                  "Mouse ID" : Capo_mice,
                                  "Time point": Capo_timepoint})
Capo_summary.head()

# %%
# another way: apply for loop to get the tumor volume of 4 treatment methods at once:
# Put treatments into a list for for loop (and later for plot labels)
treatment_list = ["Capomulin", "Ramicane", "Infubinol", "Ceftamin"]

# Create empty list to fill with tumor vol data (for plotting)
tumor_vol_list = []

for drug in treatment_list:
    
    tumor_vol = extract.loc[extract["Drug Regimen"]==drug,"Tumor Volume (mm3)"]
    tumor_vol_list.append(tumor_vol)
#print(tumor_vol_list)

# %%
# Put treatments into a list for for loop (and later for plot labels)
treatment_list = ["Capomulin", "Ramicane", "Infubinol", "Ceftamin"]

# Create empty list to fill with tumor vol data (for plotting)
tumor_vol_list = []

# Calculate the IQR and quantitatively determine if there are any potential outliers. 
for drug in treatment_list:
    
    # Locate the rows which contain mice on each drug and get the tumor volumes
    final_tumor_vol = extract.loc[extract["Drug Regimen"] == drug, 'Tumor Volume (mm3)']
    
    # add subset 
    tumor_vol_list.append(final_tumor_vol)
    
    # Determine outliers using upper and lower bounds
    quartiles = final_tumor_vol.quantile([.25,.5,.75])
    print(quartiles)

# %%
quartiles = final_tumor_vol.quantile([.25,.5,.75])
lowerq = quartiles[0.25]
upperq = quartiles[0.75]
iqr = upperq-lowerq

print(f"The lower quartile of tumor volume is: {lowerq}")
print(f"The upper quartile of tumor volume is: {upperq}")
print(f"The interquartile range of tumor volume is: {iqr}")
print(f"The the median of tumor volume is: {quartiles[0.5]} ")

lower_bound = lowerq - (1.5*iqr)  # lower the lower (1.5 times the iqr)|upper the upper () -> ouliers 
upper_bound = upperq + (1.5*iqr)
print(f"Values below {lower_bound} could be outliers.")
print(f"Values above {upper_bound} could be outliers.")

# %%
# Generate a box plot of the final tumor volume of each mouse across four regimens of interest
fig1, ax1 = plt.subplots()

plt.boxplot(tumor_vol_list,labels=treatment_list)

# %% [markdown]
# ## Line and Scatter Plots

# %%
# Generate a line plot of tumor volume vs. time point for A Mouse (01 mouse) treated with Capomulin
capomulin_table = mouse_df.loc[mouse_df['Drug Regimen'] == "Capomulin"]
mousedata = capomulin_table.loc[capomulin_table['Mouse ID']== 'l509']
plt.plot(mousedata['Timepoint'],mousedata['Tumor Volume (mm3)'],linewidth=1, color="blue")
plt.xlabel('Timepoint (days)')
plt.ylabel('Tumor Volume (mm3)')
plt.title('Capomulin treatment of mouse l509')
plt.show()

# %%
mousedata

# %%
# Generate a scatter plot of average tumor volume vs. mouse weight for the Capomulin regimen
x_values = Capo_summary["Tumor Volume (mm3)"]
y_values = Capo_summary["Mouse Weights (g)"]
plt.scatter(x_values,y_values,marker="o", facecolors="blue", edgecolors="red")
plt.title("Tumor volume (mm3) vs Mouse weight (g) from Capomulin treatment")
plt.xlabel("Mouse weight (g)")
plt.ylabel("Tumor Volume (mm3)")

(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))

plt.plot(x_values,regress_values,"r-")
plt.annotate(line_eq,(40,14.5),fontsize=15,color="red")
plt.grid()
plt.show()

# %% [markdown]
# ## Correlation and Regression

# %%
# Calculate the correlation coefficient and linear regression model 
# for mouse weight and average tumor volume for the Capomulin regimen

correlation_coefficient = st.pearsonr(x_values,y_values)
print(f"the correlation between mouse weight and the average tumor volume is {correlation_coefficient}")

# %%
# Findings: 
# the data show an uphill pattern as you move from left to right, 
# this indicates a positive relationship between mouse weight and tumor volume . 
# the higher the mouse_weight, the tumor volume (mm3) tend to be bigger. 


