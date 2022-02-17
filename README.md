## PROJECT BACKGROUND & REQUIREMENTS: 

Pymaceutical studying specializes in anti-cancer pharmaceuticals. In its most recent efforts, it began screening for potential treatments for squamous cell carcinoma (SCC), a commonly occurring form of skin cancer.

As a senior data analyst, I've been given access to the complete data from their most recent animal study. In this study, 249 mice identified with SCC tumor growth were treated through a variety of drug regimens. Over the course of 45 days, tumor development was observed and measured. The purpose of this study was to compare the performance of Pymaceuticals' drug of interest, Capomulin, versus the other treatment regimens. the task here is to generate all of the tables and figures needed for the technical report of the study. The executive team also has asked for a top-level summary of the study results.


## FILE STRUCTURE

i) the jupiternotebook is containing all my codes in Python languages to call for all neccessary data sets and followed with the results

ii) the .py file is containing all my codes without outputs as a shortage to view

iii) the Data folder is to locate all raw data and png chart images

iv) the Readme.md file is to explain about this project and my findings



## LANGUAGES, SOURCES & TOOLS USED: 

i) Python | Pandas

ii) Matplotlib

iii) Statistical Maths

iv) (https://matplotlib.org/gallery/pyplots/boxplot_demo_pyplot.html#sphx-glr-gallery-pyplots-boxplot-demo-pyplot-py)



## FINDINGS AND ANALYSIS

- Let's take a look at the overall study with 248 mouses were observed after finished the maximum timepoint of treatments which were 51% of Male and 49% of Female participated in the treatments. 

- The total mouses remained in Capomulin regimen was highest, next is Ramicane regimen. 



![Mice_per_drug](https://user-images.githubusercontent.com/93897775/154182425-689f6ba0-4ae6-46d3-8263-46eff1933936.png)




![Pie_test](https://user-images.githubusercontent.com/93897775/154182444-6986a261-f572-4174-baa5-02737a9d9769.png)


- The boxplot was shown the range of tumor volume (mm3) observed after treatment. 

- The medium size of tumor volume is 59.85 mm3 with the lower quartile of tumor volume was 48.72 mm3 and the upper quartile of tumor volume was 64.29 mm3.

- With the iqr ~ around 6; we found that the outlier values could be >= 87.66 m3 or <= 25.35 mm3; in another saying, for the Drug regimen that made tumor volume get bigger over 87.66 mm3 is considered not good and in the contrary, the treatment that made the tumor volume down to < 25.35mm3 can be considered as effective treatment. 

![box_plot_tumorvolume](https://user-images.githubusercontent.com/93897775/154182479-c1ee4014-5ed9-45e8-b448-b40f190677e6.png)


- Zooming into Capomulin regimen, picked out one mice with ID I509 to analyse, we found that the tumor volume was increasing in the first 20 days from around 45mm3 to 48mm3 but then went down very fast after that. From around 48 mm3 down to about 40.5mm3 in the next 15 days that could tell a good result for this I509 mice. 


![line_Capo_tumor](https://user-images.githubusercontent.com/93897775/154182505-6782c530-241d-4b19-bf65-41c21ea456ff.png)



- Still zooming in Capomulin regimen, we calculated the correlation between the tumor volume vs the weight of the mouses and the figure is: 0.87 shown the very close relationship between those two factors. 

- The uphill patern as you move from the left to the right, or, we call positive linear, indicated that the higher the weight of mouses, the bigger the size of tumors.


![linear_scatterplots](https://user-images.githubusercontent.com/93897775/154182516-356a66da-d030-467a-bff3-a1ab9c9266fb.png)


## Final conclusion: 

the Capomulin and Ramicane were the top 2 regimens that brought high effectiveness in cancer treatment in which Capomulin survived 230 mouses and Ramicane did 228 mouses respectively after 45 days of treatment. The Capomulin, specifically, was a little higher effective drug regimen in cancer treatment. 

## AUTHOR

Tracie Diep Bautista (Tracie B.)


