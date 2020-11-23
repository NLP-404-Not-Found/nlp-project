# Predicting the Language of GitHub Repositories by README using NLP
## About the Project
### Goals
Using natural language processing, web scraping, and classification, we aim to create a machine learning model to predict the primary programming language of a given repository on GitHub, based on the contents of its README.

### Background
GitHub automatically shows the percentages of what coding languages are used in the files of a repository. In this project, we are seeking to label and predict on only the ***primary*** language of each repository. These languages include Java, Python, Javascript, Ruby, HTML, and C++.

### Deliverables
 * A well-documented Jupyter Notebook that contains our analysis
 * A Google Slides presentation suitable for a general audience that summarizes our findings and includes visualizations
<!--
### Acknowledgments
Where you got the data, inspiration, etc. 
> My first inspiration for writing Readme files from Maggie Giust's Heart Failure repository [here](https://github.com/magsgiust/heart_failure).
-->

## Data Dictionary

| Feature Name      | Description                                                                                                                                                                                                                    | Additional Info |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| repo              | The end URL to the project. Can append to https://github.com/ to get a repo's full URL. Consists of the user, slash the name of the repository.                                                                                | object          |
| language          | The primary programming language of a repository, according to GitHub's auto-analysis.                                                                                                                                         | object          |
| readme_contents   | Messy, uncleaned text from a repo's README file as a single string.                                                                                                                                                            | object          |
| stemmed           | Readme_contents with each word stemmed, i.e. dimensionality reduction such that 'call', 'called', and 'calling' are treated as the same word. Stems are not the same as root words and do not always appear in the dictionary. | object          |
| lemmatized        | Similar to stemmed, but reduces words to its root word, which will always appear in the dictionary.                                                                                                                            | object          |
| clean             | Lemmatized readme_contents with stopwords removed.                                                                                                                                                                             | object          |
| stopwords_removed | The number of stopwords that were removed from the clean text.                                                                                                                                                                 | int64           |
| doc_length        | How long a repo's README is.                                                                                                                                                                                                   | int64           |
| words             | The clean text in array form.                                                                                                                                                                                                  | object          |
<!--
## Initial Thoughts & Hypotheses
### Thoughts
First ideas about project while initially exploring the dataset.

### Hypotheses
A hypotheses that you test in your project. Feature x significantly increases with feature y.
```
Null hypothesis: Feature x does not correlate with feature y.
Alternative hypothesis: Feature x has a significant correlation with feature y.
```

A second hypotheses that you test in your project. Feature x significantly increases with feature y.
```
Null hypothesis: Feature x does not correlate with feature y.
Alternative hypothesis: Feature x has a significant correlation with feature y.
```

## Project Steps
### Acquire
Short description for each step of the process.
### Prepare
- Short
- Description
### Explore
Can use exandable text for large amounts of text.
<details>
  <summary> Click to Expand </summary>
  
  Text goes in here. Maybe an image.
  ### Headers Still Work
  If you add an empty line between the summary code and text.
</details>

### Model
- Short
  - Description
  
### Conclusions
Key insights from project.
-->

### Tools & Requirements
* Python v3.85 (including packages WordCloud, NLTK, and Scikit-Learn)
* GitHub's API

## License & Reproduction
Anyone can reproduce this project. All we ask is that you credit us if you use our work as part of your own project.
1. Clone this repo.
2. Acquire the data:
    * a. <a href="https://github.com/settings/tokens">Go here</a> and generate a personal access token. You do ***not*** need select any scopes, i.e. leave all the checkboxes unchecked.
    * b. Save it in your env.py file under the variable ```github_token```.
    * c. Add your github username to your env.py file under the variable ```github_username```.
    * d. Add more repositories to the `REPOS` list below if you so choose.
3. Add any extra stop-words in the prepare.py file.
4. Run the code in the ```nlp_model``` Jupyter Notebook.

## Creators
<a href="https://github.com/KwameTaylor">Kwame V. Taylor</a>, Data Scientist<br>
<a href="https://github.com/adam-gomez">Adam Gomez</a>, Data Scientist
