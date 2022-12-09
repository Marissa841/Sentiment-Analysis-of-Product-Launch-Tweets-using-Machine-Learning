# Overview: 

This project determines which tweets can be correctly identified to contain  either positive sentiments (“Positive emotion”) or negative sentiments (“Negative emotion”) using a binary classifier. 

<br />
<br />

![positive and negative tweets](https://raw.githubusercontent.com/Marissa841/phase_4_project/main/img/pos_neg_tweets.PNG)



# Business Case: 

Find the best model to accurately predict whether a tweet is positive or negative.  

# Data:

The data used in this project is from CrowdFlower and data.world. The dataset contains 3 columns with 9,093 rows. The dataset can be found [here](https://data.world/crowdflower/brands-and-product-emotions).


# Methods:

The methods used for this project were based on the OSEMN method and iterative modeling. For processing the text data, I used Bag-of-words and Term frequency - inverse document frequency(TF-IDF). For the modeling portion, I used Logistic Regression models, Decision Tree Classifiers, and Random Forest Classifers taken from the Sci-kit Learn library. 

# Conclusion:

From the above-mentioned methods, I was able to obtain an overall f1 score of 0.93 using the RandomForestClassifer. This shows it was able to predict whether a tweet was positive or negative. 
![most important words for final random forest classifier model]


# Future Work:

For future work, I’d look at the labels of the tweets. There are some tweets that appeared to be incorrectly labeled in the original dataset.

# For more information:

​​See the full analysis in the [Jupyter Notebook](https://github.com/Marissa841/phase_4_project/blob/main/nlp_project.ipynb) or review this [presentation](https://github.com/Marissa841/phase_4_project/blob/main/phase_4_project_nontechnical.pdf). For additional info, my email is Marissabush.02@gmail.com



# Repository structure:

+ data
+ img
+ nlp_project.ipynb
+ README.md
+ phase_4_project_nontechnical.pdf
+ helper.py
