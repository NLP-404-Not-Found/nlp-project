import numpy as np
import pandas as pd

def get_tf_idf_df(df, all_words):
    tfs = []

    # We'll caclulate the tf-idf value for every word across every document

    # Start by iterating over all the documents
    for doc, text in documents.items():
        # We'll make a data frame that contains the tf for every word in every document
        df = (pd.Series(text.split())
            .value_counts()
            .reset_index()
            .set_axis(['word', 'raw_count'], axis=1, inplace=False)
            .assign(tf=lambda df: df.raw_count / df.shape[0])
            .drop(columns='raw_count')
            .assign(doc=doc))
        # Then add that data frame to our list
        tfs.append(df)

    # We'll then concatenate all the tf values together.
    (pd.concat(tfs)
    # calculate the idf value for each word
    .assign(idf=lambda df: df.word.apply(idf))
    # then use the if and idf values to calculate tf-idf 
    .assign(tf_idf=lambda df: df.idf * df.tf)
    .drop(columns=['tf', 'idf'])
    .sort_values(by='tf_idf', ascending=False))
    return df

