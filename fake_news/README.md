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







