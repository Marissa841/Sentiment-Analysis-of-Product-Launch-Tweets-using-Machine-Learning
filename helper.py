from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


def model_helper(X, y, model, bow=True):
    """
    Helper function to run sklearn models.  
    
    Args:
        X (dataframe): Features to train on. 
        y (series): Target variable
        model (sklearn): Model to train on.
        bow (boolean): Whether to do bow or tfidf
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 11)
    # bag of words 
    if bow:
        vectorizer = CountVectorizer()
        X_train = vectorizer.fit_transform(X_train)
        X_test = vectorizer.transform(X_test)
    else:
    # tfidf 
        tfidf_vectorizer = TfidfVectorizer()
        X_train = tfidf_vectorizer.fit_transform(X_train)
        X_test = tfidf_vectorizer.transform(X_test)
    model.fit(X_train, y_train)

    print(f"Training Score: {f1_score(y_train, model.predict(X_train))}")
    print(f"Testing Score: {f1_score(y_test, model.predict(X_test))}")

    return model

def word_count_by_class(word, df):
    """
    Function to count words in positive and negative tweets. 

    Args:
        word (string): word to count from tweet.
        df (dataframe): dataframe with target and tweets.
    """
    try:
        positive = df[df['target'] == 1]['tweets_without_stopwords'].str.split(expand=True).stack().value_counts()[word]
    except KeyError:
        positive = 0
    try:
        negative =   df[df['target'] == 0]['tweets_without_stopwords'].str.split(expand=True).stack().value_counts()[word]
    except KeyError:
        negative = 0
    print(f"postive count: {positive}")
    print(f"negative count: {negative}")

def tweet_finder_by_word(word, df):
    """
    Function to find tweets with specific key word.

    Args: 
        word (string): word to find in tweet. 
        df (dataframe): dataframe with target and tweets. 
    """
    for index, row in df.iterrows():
        if word in row["tweets_without_stopwords"]:
            if row["target"] == 0:
                print(f"negative - {row['tweet_text']}")
            else:
                print(f"positive - {row['tweet_text']}")