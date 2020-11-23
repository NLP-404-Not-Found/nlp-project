import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from numpy.random import choice

import re
import unicodedata
import nltk

# default viz size settings
plt.rc('figure', figsize=(9, 7))
plt.rc('font', size=15)

from wordcloud import WordCloud

def word_cloud_1(all_words, javascript_words, python_words):
    all_cloud = WordCloud(background_color='white', colormap='cividis', height=1000, width=400, margin=2).generate(all_words)
    javascript_cloud = WordCloud(background_color='white', colormap='winter', height=600, width=800, margin=2).generate(javascript_words)
    python_cloud = WordCloud(background_color='white', colormap='cool', height=600, width=800, margin=2).generate(python_words)

    plt.figure(figsize=(10, 8))
    axs = [plt.axes([0, 0, .6, 1]), plt.axes([.5, .5, .45, .45]), plt.axes([.5, 0, .45, .45])]

    axs[0].imshow(all_cloud)
    axs[1].imshow(javascript_cloud)
    axs[2].imshow(python_cloud)

    axs[0].set_title('All Words')
    axs[1].set_title('Javascript')
    axs[2].set_title('Python')

    for ax in axs: ax.axis('off')

    plt.show

def word_cloud_2(html_words, ruby_words, c_plus_plus_words, java_words):
    html_cloud = WordCloud(background_color='white', colormap='cool', height=300, width=400, margin=2).generate(html_words)
    ruby_cloud = WordCloud(background_color='white', colormap='winter', height=300, width=400, margin=2).generate(ruby_words)
    c_plus_plus_cloud = WordCloud(background_color='white', colormap='winter', height=300, width=400, margin=2).generate(c_plus_plus_words)
    java_cloud = WordCloud(background_color='white', colormap='cool', height=300, width=400, margin=2).generate(java_words)

    plt.figure(figsize=(10, 8))
    axs = [plt.axes([0, .5, .45, .45]), plt.axes([0, 0, .45, .45]), plt.axes([.5, .5, .45, .45]), plt.axes([.5, 0, .45, .45])]

    axs[0].imshow(html_cloud)
    axs[1].imshow(ruby_cloud)
    axs[2].imshow(c_plus_plus_cloud)
    axs[3].imshow(java_cloud)

    axs[0].set_title('HTML')
    axs[1].set_title('Ruby')
    axs[2].set_title('C++')
    axs[3].set_title('Java')

    for ax in axs: ax.axis('off')

    plt.show

def js_v_python_props(word_counts):
    # figure out the percentage of javascript vs python
    (word_counts
    .assign(p_javascript=word_counts.javascript / word_counts['all'],
            p_python=word_counts.python / word_counts['all'])
    .sort_values(by='all')
    [['p_javascript', 'p_python']]
    .tail(30)
    .sort_values('p_python')
    .plot.barh(stacked=True))

    plt.title('Proportion of Javascript vs Python for the 30 most common words')

    plt.show

def most_common_words_props(word_counts):
    # figure out the percentage of language
    (word_counts
    .assign(p_javascript=word_counts.javascript / word_counts['all'],
            p_python=word_counts.python / word_counts['all'],
            p_ruby=word_counts.ruby / word_counts['all'],
            p_html=word_counts.html / word_counts['all'],
            p_c_plus_plus=word_counts.c_plus_plus / word_counts['all'],
            p_java=word_counts.java / word_counts['all'])
    .sort_values(by='all')
    [['p_javascript', 'p_python', 'p_ruby', 'p_html', 'p_c_plus_plus', 'p_java']]
    .tail(20)
    .sort_values('p_python')
    .plot.barh(stacked=True))

    plt.title('Proportion of Language for the 20 most common words')

def get_bigrams(words):
    top_10_bigrams = (pd.Series(nltk.ngrams(words, 2))
                      .value_counts()
                      .head(10))

    return top_10_bigrams

def viz_bigrams(top_10_bigrams):
    top_10_bigrams.sort_values().plot.barh(color='pink', width=.9, figsize=(10, 6))

    plt.title('10 Most frequently occuring bigrams')
    plt.ylabel('Bigram')
    plt.xlabel('# Occurances')

    # make the labels pretty
    ticks, _ = plt.yticks()
    labels = top_10_bigrams.reset_index()['index'].apply(lambda t: t[0] + ' ' + t[1])
    _ = plt.yticks(ticks, labels)

def idf(words_df, train):
    '''
    Takes in a dataframe made of a single column where each row is a single word and 
    returns a dataframe containing the top 10 most frequent words,
    the number of documents each word shows up in, and the idf value for each word
    Also requires the train dataframe to be passed in as an argument in order to identify the
    total number of documents
    '''
    
    # Creates a dictionary of the top ten words and their number of counts
    top_10_words = words_df[0].value_counts(dropna=False).head(10).keys().tolist()
    top_10_counts = words_df[0].value_counts(dropna=False).head(10).tolist()
    word_counts = dict(zip(top_10_words, top_10_counts))
    
    # Derives the 10 most common words from the given dataframe of words
    most_common_words = [word[0] for word in list(words_df.value_counts().head(10).index)]
    
    # This dictionary will store how many documents each word appears in 
    appearances_dict = dict.fromkeys(most_common_words)
    
    # The total number of documents is based on the number of rows in the train dataframe
    number_of_documents = train.shape[0]
    
    # This is essentially a list containing the contents of the words column in the dataframe. It is a list of lists.
    list_of_wordlists = list(train.words.values)
    
    # Start iterating through the list of common words. We want to collect information for each one.
    for word in most_common_words:
        
        # Set the initial number of documents that the word appears in to zero
        number_of_appearances = 0
        
        # Start iterating through the list made from the words column in the dataframe 
        for words in list_of_wordlists:
            
            # If the current word is in a document, add 1 to the number of appearances and then move to the next document
            if word in words:
                number_of_appearances += 1
        
        # Once all the documents have been iterated through, add the sum total of all appearances to our appearances dictionary
        appearances_dict[word] = number_of_appearances
        
    # Create a new dictionary that will contain the IDF values for each word
    idf_dict = dict.fromkeys(most_common_words)
    
    # Start iterating through the list of common words again, using the number of appearances and the total number of documents to calculate the IDF and update the relevant key:value in the dictionary
    for word in most_common_words:
        idf_dict[word] = np.log(number_of_documents / appearances_dict[word])
    
    # Create dataframes containing the information of the total counts, the number of documents, and the idf value
    idf_df1 = pd.DataFrame.from_dict(word_counts, orient='index', columns=['total_count']).reset_index().rename(columns={'index':'word'})
    idf_df2 = pd.DataFrame.from_dict(appearances_dict, orient='index', columns=['num_of_documents']).reset_index().rename(columns={'index':'word'})
    idf_df3 = pd.DataFrame.from_dict(idf_dict, orient='index', columns=['idf_value']).reset_index().rename(columns={'index':'word'})
    
    # Merge the dataframes into a single dataframe
    idf_df = pd.merge(idf_df1, idf_df2, left_on = 'word', right_on = 'word')
    idf_df = pd.merge(idf_df, idf_df3, left_on = 'word', right_on = 'word')
    
    # Return the dataframe
    return idf_df

def t_test_loop(target, train, alpha = 0.05):    
    '''
    This function is dependent on a globally defined dataframe named 'train' that contains a 'language' column containing strings
    The target is the header for the column being investigated. The column being investigated must be a numeric type.
    Comparative t-tests are run on the target column between every possible pair of languages represented in the train dataset.
    The function prints out the result of every t-test that has a p-value below alpha. 
    '''
    # Start by developing two identical lists of all of the languages represented in the train dataset
    # We will use the series above to form our list so our output is arranged in a similar order
    # When this is converted to a function, we can generate the list in a more generalized manner
    train_language_list_1 = list(train.groupby('language')[target].mean().sort_values(ascending=False).index)
    train_language_list_2 = list(train.groupby('language')[target].mean().sort_values(ascending=False).index)

    # This empty list will hold information about which pairs have been tested. 
    # If the python and javascript pair has already be tested, then we do not need to test the javascript and python pair
    testing_pairs = []

    for language_1 in train_language_list_1: # Iterates through list 1
        for language_2 in train_language_list_2: # Iterates through list 2 in entirety for each element in list 1

            if language_1 == language_2: # Cannot run a t-test against itself, so skip the test if the two list elements are identical
                continue

            else:
                alpha = 0.05 # Set alpha

                # Run the t-test and store the t-statistic and the p-value
                stat, p = stats.ttest_ind(train[train.language == language_1][target], train[train.language == language_2][target])

                # If the p-value is statistically significant we print the results, otherwise we do nothing
                if p/2 < alpha:

                    # Creating strings to represent the pair that is being tested (eg. 'Python and JavaScript' & 'JavaScript and Python')
                    testing_pair_1 = language_1 + " " + language_2
                    testing_pair_2 = language_2 + " " + language_1

                    # If this unique pair has not yet been tested:
                    if (testing_pair_1 not in testing_pairs) and (testing_pair_2 not in testing_pairs):

                        # Add this pair to the testing_pairs list so that we do not output duplicate t-test results
                        testing_pairs.append(testing_pair_1)
                        testing_pairs.append(testing_pair_2)

                        # Print the results of the test
                        print("----------------")
                        print(f"{target} T-Test: {language_1} & {language_2}")
                        print("----------------")
                        print("Hypotheses:")
                        print(f"H_0: There is no difference in the mean {target} of {language_1} and {language_2}")
                        print(f"H_a: There is a difference in the mean {target} of {language_1} and {language_2}")
                        print('\n')
                        print(f"p-value: {p/2}")
                        print(f"t-statistic: {stat}")
                        print(f"We reject the null hypothesis")
                        print("\n")
                        if stat < 0:
                            print(f"The mean readme {target} for {language_1} is smaller than {language_2}")
                        elif stat > 0:
                            print(f"The mean readme {target} for {language_1} is larger than {language_2}")
                        print('\n','\n')

                        # If the pair had already been tested, do not print any results and continue through the loop
                    else:
                        continue

def baseline_language_model(train, num_observations):
    '''
    This function takes in a train dataset and identifies the proportions for the languages represented in that set.
    It then creates an array num_observations long where each element is one of the languages randomly selected (weighted by the languages proportion)
    The array is returned to be used as a series of predictions to compare other models against.
    '''

    # Generates a list of all the languages in the dataset
    possible_languages = list(train.language.value_counts().index)

    # Empty list to store the proportions of observations for each language
    probabilities = []

    # Appends the probability of each language to the probabilities list based on the proportion of that language in the overall dataset
    for language in possible_languages:
        probabilities.append(train.language.value_counts()[language] / train.language.shape[0])

    # Creates an array of predictions based on weighted random chance    
    baseline_predictions = choice(possible_languages, num_observations, p=probabilities)

    return baseline_predictions
