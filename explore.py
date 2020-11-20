import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# default viz size settings
plt.rc('figure', figsize=(9, 7))
plt.rc('font', size=13)

from wordcloud import WordCloud

def word_cloud_1(all_words, javascript_words, python_words):
    all_cloud = WordCloud(background_color='white', height=1000, width=400, margin=2).generate(all_words)
    javascript_cloud = WordCloud(background_color='white', height=600, width=800, margin=2).generate(javascript_words)
    python_cloud = WordCloud(background_color='white', height=600, width=800, margin=2).generate(python_words)

    plt.figure(figsize=(10, 8))
    axs = [plt.axes([0, 0, .5, 1]), plt.axes([.5, .5, .5, .5]), plt.axes([.5, 0, .5, .5])]

    axs[0].imshow(all_cloud)
    axs[1].imshow(javascript_cloud)
    axs[2].imshow(python_cloud)

    axs[0].set_title('All Words')
    axs[1].set_title('Javascript')
    axs[2].set_title('Python')

    for ax in axs: ax.axis('off')

    plt.show

def word_cloud_2(html_words, ruby_words, c_plus_plus_words):
    html_cloud = WordCloud(background_color='white', height=1000, width=400, margin=2).generate(html_words)
    ruby_cloud = WordCloud(background_color='white', height=600, width=800, margin=2).generate(ruby_words)
    c_plus_plus_cloud = WordCloud(background_color='white', height=600, width=800, margin=2).generate(c_plus_plus_words)

    plt.figure(figsize=(10, 8))
    axs = [plt.axes([0, 0, .5, 1]), plt.axes([.5, .5, .5, .5]), plt.axes([.5, 0, .5, .5])]

    axs[0].imshow(html_cloud)
    axs[1].imshow(ruby_cloud)
    axs[2].imshow(c_plus_plus_cloud)

    axs[0].set_title('HTML')
    axs[1].set_title('Ruby')
    axs[2].set_title('C++')

    for ax in axs: ax.axis('off')

    plt.show