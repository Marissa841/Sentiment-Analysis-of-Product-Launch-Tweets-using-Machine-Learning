# Business Case

Apple is hosting a tech conference and they have asked for a  machine learning model to determine whether tweets have a positive or negative sentiment when introducing a new product.

![positive and negative tweets](https://raw.githubusercontent.com/Marissa841/phase_4_project/main/img/pos_neg_tweets.PNG)

# Data:

| Models                   | Bag-of-words | TF-IDF |
|--------------------------|--------------|--------|
| Logistic Regression      | 0.924        | 0.914  |
| Decision Tree Classifier | 0.921        | 0.901  |
| Random Forest Classifier | 0.931        | 0.923  |

The data used in this project is from CrowdFlower and data.world. The dataset contains 3 columns with 9,093 rows. The dataset can be found [here](https://data.world/crowdflower/brands-and-product-emotions). Below is a snippet of the data: 

![view dataframe](https://raw.githubusercontent.com/Marissa841/phase_4_project/main/img/.head().png)

# Methods:

The methods used for this project were based on the OSEMN method and iterative modeling. For processing the text data, I used Bag-of-words and Term frequency - inverse document frequency(TF-IDF). For the modeling portion, I used Logistic Regression models, Decision Tree Classifiers, and Random Forest Classifers taken from the Sci-kit Learn library. 

# Conclusion:

From the above-mentioned methods, I was able to obtain an overall f1 score of 0.93 using the RandomForestClassifer. This shows it was able to predict whether a tweet was positive or negative. Additionally, negative tweets had more strongly negative words and positive tweets had less distinctive words that indicated positivity.


Below is a bar graph illustrating which words were most important and whether the word appeared more in positive or negative tweets:

![most important words for final random forest classifier model](https://raw.githubusercontent.com/Marissa841/phase_4_project/main/img/most_important_words.PNG) 

The words that appeared in negative tweets were more typically negative while the positive tweets were more neutral. 

Below is a confusion matrix that shows the performance of the model: 

![confusion matrix of final random forest classifier model](https://raw.githubusercontent.com/Marissa841/phase_4_project/main/img/confusion_matrix_phase_4.png)

There were 589 true positives, 2 false negatives, 35 true positives, and 84 false positives.


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
