
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **sports or athletics** (see below) for the region of **Woodford Green, Redbridge, United Kingdom**, or **United Kingdom** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Woodford Green, Redbridge, United Kingdom** to Ann Arbor, USA. In that case at least one source file must be about **Woodford Green, Redbridge, United Kingdom**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Woodford Green, Redbridge, United Kingdom** and **sports or athletics**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **sports or athletics**?  For this category we are interested in sporting events or athletics broadly, please feel free to creatively interpret the category when building your research question!
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# 
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[45]:

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_num_fitness_facilities = pd.DataFrame([1611,1572,1540,1642,1595,1833,2024,2444,2642,3083,3419], 
                                         index=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])

df_turnover_fitness_facilities = pd.DataFrame([687,937,931,1226,1300,1370,1496,1675,1684,1887,2003], 
                                         index=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])

plt.style.use('seaborn-colorblind')

f = plt.figure(figsize=(10,3))
ax = f.add_subplot(121)

ax.plot(df_num_fitness_facilities,'-', alpha = 0.75, label = 'Number of Fitness Facilities in UK')
ax.plot(df_turnover_fitness_facilities, '-', alpha=0.75, label = 'Turnover (in billions) for Fitness Facilities in UK')
ax.legend(loc = 'best', frameon=False, fontsize=8)
ax.set_xlabel('Year')
ax2 = f.add_subplot(122)
ax2.scatter(df_num_fitness_facilities, df_turnover_fitness_facilities)
ax2.set_xlabel('Number of Fitness Facilities')
ax2.set_ylabel('Turnover (in billion) for Fitness Facilities')
plt.show()


# In[28]:

from scipy.stats import pearsonr
corr, _ = pearsonr(df_num_fitness_facilities, df_turnover_fitness_facilities)
print('Pearsons correlation: %.3f' % corr)


# In[ ]:



