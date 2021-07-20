# Strategy

1. Feature engineering

    1. Data cleaning

        - Text preprocessing (noise removal, lemmatize, etc)

        - Part of speech tagging

    2. Exploration
    
        - Get average, distribution, outlier of potential features
       
        - Statistics for the whole corpus and/or per article

        - Items to compare between Real and Fake news 
    
            - Number of vocavularies in the corpus/per article
    
            - Most frequent words and grammar in the corpus
    
            - Number of inappropriate keywords (agitative, hateful, derogative tones; clickbait; slang) per title/artices
    
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
    
        - Whole text/grammar: CNN, RNN (LSTM), Naive bayes
        
        - Keyword/grammar counts: MLP, SVM, kNN
        
    - For each model, include followings:
    
        - Score(s)
        
        - True/False classification cases analysis
        
        - Improvement idea
        
        - Take away for the final model
        

3. Finial modeling and test


    - Integrating the findings from the above, build a better performing model and test.


# Known characteristics of fake news


I summarized the judging criteria about credibility of news into three categories.
Among the below, utilizable features are tested and used in this analysis.

1. Information-wise

    1. Lack of information
        
        1. Lack of necessary information, like 5W1H
        2. Lack of context, not the whole truth

    2. Not a NEWs
    
        1. Outdated
        
    3. Not valuable
    
        1. Not impactful/important socially
        2. Not a rare event
        3. Nothing to do with the area where news provider cover
        
2. Tone

    1. Doesn't sounds professional
    
        1. Contain slangs
        2. Vocabularies are not specific
    
    2. Hateful
    
        1. Enhance bias or discrimination
        2. Provocative
        
    3. Urgent and Agitative
    
        1. Make readers to spread this news as much as you can
        2. Make reader to act promptly
        
    4. Joke (or pretend to be a joke)
    
        1. Make fun of someone/organization/policy
        
    5. Clickbait

        1. The title contains the above

3. Source-wise

    1. Author
    
        1. Cannot find the name of author
        2. The author is fake
        3. The author is not a reliable person/organization
        
    2. Media/Publishing organizatio
    
        1. The media is not reliable of fishy

    3. Supporting evidence
    
        1. The evidence that support the news is not adequate
        2. Not provided by a relavant expert or organization


