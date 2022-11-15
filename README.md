# Overview: 

This project determines which tweets can be correctly identified to contain  either positive sentiments (“Positive emotion”) or negative sentiments(“Negative emotion”) using a binary classifier. 

<br />
<br />

![positive and negative tweets](https://raw.githubusercontent.com/Marissa841/phase_4_project/main/img/pos_neg_tweets.PNG)



# Business Case: 

Find the best model to accurately predict whether a tweet is positive or negative.  

# Data:

The data used in this project is from CrowdFlower and the data.world. The dataset contains 3 columns with 9,093 rows. 


# Methods:

The methods used for the project were based on the OSEMN method iterative modeling. For processing the text data I used bag of words and tfidf. For the modeling portion, I used LogisticRegression, DecisionTreeClassifier, and RandomForestClassifer taken from the Sci-kit Learn library. 

# Conclusions + Future Work:

From the above-mentioned methods, I was able to obtain an overall f1 score of 0.93 using the RandomForestClassifer. This shows it was able to predict whether a tweet was positive or negative accurately. 

# For more information:

​​See the full analysis in the [Jupyter Notebook](https://github.com/Marissa841/phase_4_project/blob/main/nlp_project.ipynb) or review this [presentation](https://github.com/Marissa841/phase_3_project/blob/main/phase_4_project_nontechnical.pdf). For additional info, contact Marissa Bush at Marissabush.02@gmail.com



# Repository structure:

+ data
+ img
+ main_notebook.ipynb
+ README.md
+ phase_4_project_nontechnical.pdf
+ helper.py
