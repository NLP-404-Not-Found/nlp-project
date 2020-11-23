# Predicting the Language of GitHub Repositories by README using NLP
## About the Project
### Goals
Using natural language processing, web scraping, and classification, we aim to create a machine learning model to predict the primary programming language of a given repository on GitHub, based on the contents of its README.

### Background
GitHub automatically shows the percentages of what coding languages are used in the files of a repository. In this project, we are seeking to label and predict on only the ***primary*** language of each repository. These languages include Java, Python, Javascript, Ruby, HTML, and C++.

### Deliverables
 * A well-documented Jupyter Notebook that contains our analysis
 * A Google Slides presentation suitable for a general audience that summarizes our findings and includes visualizations

### Acknowledgments
Where you got the data, inspiration, etc. 
> My first inspiration for writing Readme files from Maggie Giust's Heart Failure repository [here](https://github.com/magsgiust/heart_failure).

## Data Dictionary
Describe the columns in your final dataset. Use [this link](https://www.tablesgenerator.com/markdown_tables) to easily create markdown tables.

| Feature Name | Description          | Additional Info |
|--------------|----------------------|-----------------|
| x            | time in hours        | integer         |
| y            | count of observation | float           |

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


### Tools & Requirements
Python v3.85
WordCloud
NLTK
Scikit-Learn

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
