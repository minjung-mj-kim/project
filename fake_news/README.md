# Flow

1. Test of simple naive bayse and LSTM models -> they work
    - simple_NaiveBayse.ipynb
    - simple_LSTM.ipynb

2. EDA and check preprocess items and potential bias
    - eda_raw.ipynb

3. Preprocess text data
    - organize_data.ipynb


4. EDA preprocessed data
    
5. Modeling







# To do, if have more time

- LSTM with grammar tags
    - Grammar structures between real and fake news are definetly different, but hard to describe how it is. LSTM should be proper to identify grammar sequence.

- Take average of embedding vectors then Feedforward NN
    - Everaged embedding migh have prominent feature component that involves fake news

- CNN with title?
    - Is there "image" thing in title in order to catch attention of real/fake news readers?

- Group news with tf-idf, then compare real and fake?
    - Remove potential bias about topics in dataset


# =========== OLD ==================



# Data

The dataset is provide by Information Security and Object Technology (ISOT) research lab, University of Victoria.
https://www.uvic.ca/engineering/ece/isot/datasets/fake-news/index.php

The dataset contains **21k real news** scrapped from "Reuters.com" and **24k fake news** collected from different sources, where all of them are flagged as unreliable by Polififact (a fact-checking organization in the USA) and Wikipedia. The coverage of topics are various, yet mostly about politics.

Provided dataset are **True.csv** (reuter news) and **Fake.csv** (unreliable news), where both contain **title, text, subject, and publication date** columns.


# Strategy

1. Feature engineering

    1. Data cleaning

        - Text preprocessing

        - Part of speech tagging

    2. Exploration
           
        - Statistics for the whole corpus and/or per article

        - Items to compare between Real and Fake news 
    
        - Find keywords of high classifying power
        
        
    3. Data organization
    
        - Raw text
        
        - Processed text
        
        - Grammar of raw text
        
        - Grammar of processed text
        
        - Count of grammar features
        
        - Count of keywords


2. Initial modeling and test

    - Models to test
    
        - Text/grammar: Naive bayes, RNN (LSTM), (Feed forward NN, CNN)
                
    - For each model, include followings:
    
        - Performance score(s)
        
        - Error analysis
        

3. Finial modeling and test


    - Integrating the findings from the above, build a better performing model and test.
    
    
4. Dataset expansion and model improvement
    
    - Test and upgrade this model by including more dataset and features (using other research data, kaggle, web scrapping, etc).
    


# Known characteristics of fake news


I summarized the characteristics of fake news into three categories.
Those characteristics come from the well known judging criteria and my personal impression (1.3., 2.1., and 2.3.).
Among the below, utilizable features are tested and used in this analysis.

1. Information-wise

    1. Lack of information
        
        1. Lack of necessary information, like 5W1H
        2. Lack of context, not the whole truth

    2. Not a NEWs
    
        1. Outdated
        
    3. Not valuable
    
        1. Not impactful/important socially
        2. Not a story around the target reader
        
2. Tone

    1. Doesn't sounds professional
    
        1. Contain improper words
        2. Vocabularies are not specific
    
    2. Hateful
    
        1. Enhance bias or discrimination
        2. Provocative
        
    3. Urgent and Agitative, make the target readers to ...
    
        1. Believe that they are the persecuted week
        2. Believe that they are excluded and unfairly treated
        3. Spread this news as much as you can because this news seemed to be censored
        4. Act promptly against the powerful evil to save themselves from the disaster
        
    4. Joke (or pretend to be a joke)
    
        1. Make fun of someone/organization/policy
        
    5. Clickbait

        1. The title contains the above

3. Source-wise

    1. Author
    
        1. Cannot find the name of author
        2. The author is fake
        3. The author is not a reliable person/organization
        
    2. Media/Publishing organization
    
        1. The media is not reliable of fishy
        2. The organization is biased

    3. Supporting evidence
    
        1. The evidence that support the news is not adequate
        2. Not provided by a relavant expert or organization