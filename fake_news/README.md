
# Fake news classification

## Dataset

- Source
    - Information Security and Object Technology (ISOT) research lab, University of Victoria.
    - https://www.uvic.ca/engineering/ece/isot/datasets/fake-news/index.php
    - Real news scrapped from "Reuters.com"
    - Fake news collected from different sources
    - Fack-checked by Polififact (a fact-checking organization in the USA) or Wikipedia

- Data spec
    - Size: about 20k for each of the real and fake news
    - Containts news title


## Analysis procedure

1. Develop quick and easy models with raw text data to estimate feasibility and baseline scores.
    - Tested machine learning models:
        - Naive Bayes (based on word count)
        - LSTM with glove word embedding
        - Feedforward neural network (FNN) with averaged glove word embedding
    - Results: all models showed about 90% or higher accuracy with balanced dataset
    
2. EDA and organize raw data 
    - Treatment done:
        - Unified abbreviation (e.g. U.S., US, U.S.A to U.S.)
        - Clickbait taggings
        - Swearing taggins
        - Noise removal or taggings
        - Lemmatize
        - PoS (Part-of-Speech) taggings
    - Findings from EDA:
        - Fake news have redundunt longer titles in average
        - Generally, fake news have different in format, some are clear (like length of title, irregular abbreviation/formatting, etc), but some are subtle (grammar seemed odd, but hard to tell how)
        - Some fake news have more noise (special characters) or swearing words
        - Some fake news have clickbait (e.g. "Video", "Watch", "Detail")
        - First name appears in the title only in fake news (e.g. Donald, Hilary)
        - Fake news sound more emotinal, with more exclamation marks (!, ?)
        - Words with international topic (North Korea, UN, EU, etc) appeared nearly only for real news
    - See details at "2. EDA of raw data under" under "A. Explanation of files"
        
3. Through test of modeling idea
    - Tested 15 (= 5 inputs x 3 machine learning architectures) models
        - Input
            - Glove word embeddings with
                - original text
                - all lower cased text
                - cleaned text
                - cleaned & lemmatized & stopword removed text
            - One-hot encodings with
                - PoS tags (instead of text)
        - Machine learning architectures
            - Naive Bayes
            - LSTM
            - FNN
    - Tested a manual model composed with EDA findings to see how much machine learning excel logic that human found

4. Build a final model
    - Tune hyperparameters
    - Combine models with good performance to build a final prediction model using bagging ensemble learning method
    
## Result
- Final model showed **99% accuracy/precision/recall**, better than any of single quick and easy model at analysis step 1.
- **LSTM with PoS tag input** showed the **best performance**.
- Both **FNN and LSTM** showed **much batter performance with PoS tags**, which implies **grammar structure is the strongest feature of classification** in this dataset.
- Naive bayes showed less dependency on input data, on the other hand.  
- **Text cleaning improved** performance, however, **lemmatization and stopword removal didn't improve** performance. It implies **including noise of text improves fake news classification**.


## Explanation of files


1. Test simple models
    - simple_NaiveBayes.ipynb 
        - Naive bayes model with news title tokens. 
        - Too good accuracy. Potential biased feature(s) in this dataset is suspected.
    - simple_LSTM.ipynb
        - LSTM model with pretrained embeddings of title tokens. 
        - Some words might not have corresponding pretrained embeddings
        - Better accuracy with trainable embedding layer.
    - simple_FNN.ipynb
        - Feedforward NN model with averaged pretrained embedding vectors of title. 
        - Some words might not have corresponding pretrained embeddings
        - Better accuracy with trainable embedding layer.

2. EDA of raw data
    - Findings from selected examples
        - Real news title is **shorter** than fake news.
        - Real news have **informative and concise** tone.
        - Fake news sounds **gossip, emotilnal, redundunt,** and awkward in **grammar structure**
        - Fake news contains **click bait** (e.g. "DETAILS", "VIDEO", full name of a person, exclamation).
        - **First names** occurs in title frequently in fake news, which is not preferred in real news to be concise. 
        - Fake news has irregular text format:
            - Extra **upper cases**, probably to catch attention.
            - Text is **noisier** with various special characters and links.
        - Some fake news title has a **slang** word, where its partial characters are replaced with special characters (e.g. "sh\*t", "a@@")
        - Fake news quote social media or website much more frequently.
        - Fake news with empty/short titles have web addresses as their titles. It looks like an impropper cleaning of web scrapping data.
        
    - Findings from statistics
        - **"Video"** is one of the most frequent title words for fake news
        - **Various special charactors** in title
        - **Exclamation** marks (!, ?) are frequently used, which make fake news sounds **emotional**.
        - A lot of **"@"** in text, probably they spread fake news by **quoting social media**, like a **rumor** is generated by quoting other person.
        - **Title words are surprisingly polarized**, i.e. 89% of words are not overlapping, which explains **why our simple models perform with surprisingly high accuracy**. It turned out that **classification power** mostly comes from **different capitalization rules between real and fake news**. Fake news have too much capitalization, probably to catch attention. We should check this point again after preprocess text.
        - Some **international** issues words appear only in real news. However, you can't tell if that's because fake news care more about **domestic politics** or this dataset is **biased**.

    
    - Note for preprocessings
        - Real news starts with source, **"Location (Reuters)"**. This part should be removed in order not to introduce bias when genalize this model out of Reuter news.
        - Unifying or distinguishing words with **Upper** case and **abbreviation** would be tricky for fake news.
            - "US", "us", "U.S.", "U.S", "U.S.A."
            - "IS" and "is"
            - "PM", "P.M.", and "p.m."
        - Some capital letter headache (e.g. distinguish "House" and "house") can be solved by using **bigram**. Bigram can select some of proper nouns combined by two common nouns, such as **White House, North Korea**. 
        - Consider taging or removing **click bait words** (e.g. "[Watch]", "[Image]", "[Details]) to avoid bias
        - Tag or remove words with **"\*"** charactor (probably a slang, which is not used in real news)
        
3. Text preprocessing and EDA
    - examine_organization_item.ipynb
        - Enhanced EDA to test text organization result
    - organize_text_data.ipynb
        - Cleaned and wrangled text data
        - Tag POS and lemmatize
        - Prepared for both Naybe Bayes and Word Embedding models
        
4. Make and test a manual model
    - sample_Manual.ipynb
        - To verify machine learning models are better than manual data selection
        - Utilize findings from EDA for fake news detection
            - Long title size
            - Too many special characters
            - Contains click bait
            - Contains first name
            - Contains slang
        - Overall bad accuracy (50%, not better than random selection), but good precision.

5. Course hyperparameter tuning
    - Models to test
        - Added variations to simple models
        - Ran FNN and LSTM on various organized data
        - Saved test results to compare performance and interpret
    - Strategy
        - Orthogonalization: tune hyperparameters for train accuracy first, then validation set
    - tune_training_hyperparameters.ipynb
        - Tune hyperparameters of LSTM and FNN
        - Move on once good enough training accuracy is obtained
    - tune_regularization_hyperparameters.ipynb
        - Tune dropout rate
        
6. Regularization hyperparameter tuning
    - tune_reg_hyperparameters.ipynb
        - Tune drop_out rates
        - Get the final model for each version

7. Test all models
    - models_evaluation.ipynb
        - Save prediction and scores of all models with bootstrapping for ensemble learning

8. Final model
    - final_model.ipynb 
        - Build a final model with bagging (strong for overfit)
        - Final model showed **% accuracy/precision/recall, better than any of single simple model
        
        
9. Etc
    - freq_utils.py: frequently used function
    - data: contains all data files 
        - Original raw data files:  **True.csv** (reuter news) and **Fake.csv** (unreliable news)
    - (To do)score_and_interpret.ipynb
        - Compare results and correlation of each model
        - Interpret results of selected models