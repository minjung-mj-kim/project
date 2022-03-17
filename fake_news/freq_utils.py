#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

import tensorflow as tf
import tensorflow.keras.layers as tfl

from matplotlib import pyplot as plt


def split_dataframe_class(df, class_column='label'):
    
    # drop invalid entries
    df = df.dropna()    
    
    # get unique classification labels
    class_labels = df[class_column].unique()    
    
    # number of classes
    n_class = len(class_labels)
    
    # seperate dataset for each classification
    df_list = [df[df[class_column] == class_labels[i]] for i in range(n_class)]
    
    # return list of dataframe grouped by classification label
    return df_list

def train_dev_test_split(df_list, m, class_column='label', class_balance=True, r_dev=0.2, r_test=0.2, rand_state=42):
    '''
    train_dev_test_split
    Pass a list of dataframe, # samples
    Return train, dev, test (if r_dev>0) or train, test
    Split train/dev/test as 1-r_dev-r_test/r_dev/r_test ratio.
    For classification, set split_class=True if you want to keep every class has same statistics.
    
    If split_class = False, combines all rows of all dataframes, then samples m rows randomly.
    If split_class = True, combines m/n_class rows from each dataframe, then samples m rows randomly.
    '''
    
    # Data frame to sample m examples
    df = pd.DataFrame()
    
    # Drop invalid entries
    df_list = [temp_df.dropna() for temp_df in df_list]

    # When you don't care statistical balance between classes
    if not class_balance:
        
        # Concat all dataframe
        df = pd.concat(df_list)

    # When you care
    else:
        
        classified=1
        classes=set()
        
        for i in range(len(df_list)):
            temp_df = df_list[i]
            for element in temp_df[class_column].unique():
                classes.add(element)
                        
            if temp_df[class_column].nunique()!=1:
                classified*=0
        
        # You can tell the data frame is classified when:
        if (not classified) or not (len(classes)==len(df_list)):
            
            # Classified data frame list
            df_list = split_dataframe_class(pd.concat(df_list), class_column)
        
        n_class = len(df_list)
        
        # number of samples per each class
        m_each_class = int(m/n_class)
        
        # Sample equaly from each class then concat
        concat_df_list = [df_list[i].sample(n=m_each_class, random_state=rand_state) for i in range(n_class)]
        
        # VERY IMPORTANT TO RESET INDEX
        df = pd.concat(concat_df_list).reset_index(drop=True)

        

    train, test = train_test_split(df, test_size=r_test, random_state=rand_state+3)
    if r_dev>0:
        train, dev  = train_test_split(train, test_size=r_dev/(1-r_test), random_state=rand_state+5)
        return train, dev, test
    else:
        return train, test

def plot_confusion_matrix(y_actu, y_pred, title='Confusion matrix', cmap=plt.cm.gray_r):
    
    df_confusion = pd.crosstab(y_actu, y_pred.reshape(y_pred.shape[0],), rownames=['Actual'], colnames=['Predicted'], margins=True)
    
    df_conf_norm = df_confusion / df_confusion.sum(axis=1)
    
    plt.matshow(df_confusion, cmap=cmap) # imshow
    #plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(df_confusion.columns))
    plt.xticks(tick_marks, df_confusion.columns, rotation=45)
    plt.yticks(tick_marks, df_confusion.index)
    #plt.tight_layout()
    plt.ylabel(df_confusion.index.name)
    plt.xlabel(df_confusion.columns.name)

def plot_learning_curve(history):
    df_loss_acc = pd.DataFrame(history.history)
    df_loss= df_loss_acc[['loss','val_loss']]
    df_loss.rename(columns={'loss':'train','val_loss':'validation'},inplace=True)
    df_acc= df_loss_acc[['accuracy','val_accuracy']]
    df_acc.rename(columns={'accuracy':'train','val_accuracy':'validation'},inplace=True)
    df_loss.plot(title='Model loss',figsize=(12,8)).set(xlabel='Epoch',ylabel='Loss')
    df_acc.plot(title='Model Accuracy',figsize=(12,8)).set(xlabel='Epoch',ylabel='Accuracy')


# # Sequential

def pretrained_embedding_layer(word_to_vec_map, word_to_index, trainable = False):

    vocab_size = len(word_to_index) + 1              # adding 1 to fit Keras embedding
    any_word = list(word_to_vec_map.keys())[0]
    emb_dim = word_to_vec_map[any_word].shape[0]    # embedding vector size (= 50)
      
    # Initialize embedding matrix
    emb_matrix = np.zeros((vocab_size,emb_dim))

    # Set embedding matrix element with pretrained data
    for word, idx in word_to_index.items():
        emb_matrix[idx, :] = word_to_vec_map[word]

    # Embedding layer
    embedding_layer = tfl.Embedding(vocab_size,emb_dim,trainable = trainable)

    # Build the embedding layer before setting the weights
    embedding_layer.build((None,))
    
    # Set the weight with pretrained embedding matrix 
    embedding_layer.set_weights([emb_matrix])
    
    return embedding_layer

def get_pretrained_embedding(): # Get pretrained word embedding info
    # index: 1-400,000
    word_to_index = {} 
    index_to_word = {} 
    word_to_vec_map = {}
    
    with open('data/glove.6B.50d.txt', 'r') as f:
        words = set()
        for line in f:
            line = line.strip().split()
            curr_word = line[0]
            words.add(curr_word)
            word_to_vec_map[curr_word] = np.array(line[1:], dtype=np.float64)
        
        i = 1
        for w in sorted(words):
            word_to_index[w] = i
            index_to_word[i] = w
            i = i + 1
            
    return word_to_index, index_to_word, word_to_vec_map

def sentences_to_indices(X, word_to_index, max_len):
    '''
    - X: (m, 1) text input
    - word_to_index: glove
    - max_len: max sentence length in number of words

    return 
    - X_indices: tokenzed and indexed input (m, max_len)  
    '''
    
    m = X.shape[0]                                 

    X_indices = np.zeros((m, max_len))
    
    for i in range(m):                             
        
        # Lower & Tokenize
        tokenized_sentence = X[i].lower().split()
        
        # Word/token position, from 0 to max_len-1
        j = 0
        
        # Word to index & Zero padding
        for word in tokenized_sentence:
            if word in word_to_index.keys():

                X_indices[i, j] = word_to_index[word]
                j =  j+1
                
                if j > max_len-1:
                    break
                
    return X_indices

def dataframe_to_arrays(df, word_to_index, max_len, Xname='title', Yname='label'):
    
    #X = df.title.str.replace(r'[^\s\w]', '',regex=True).to_numpy()
    index = df.index.to_numpy() 
    X = df[Xname].to_numpy()
    Y = df[Yname] #.to_numpy() -> commented out to keep dataframe index
    X_indices = sentences_to_indices(X, word_to_index, max_len)
    Y_oh = pd.get_dummies(df[Yname]).to_numpy()
    
    return index, X, X_indices, Y, Y_oh