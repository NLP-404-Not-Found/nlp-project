import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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