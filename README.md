# Profibility drivers for Movies 2015 to present

**Authors**: Eric Roberts, Justin Williams

## Overview

A one-paragraph overview of the project, including the business problem, data, methods, results and recommendations.

## Business Problem

Microsoft is looking to create their own movie content. They need to know what factors are currently driving success at the box office. Our overarching goal is to determine why movies are doing well, and make reccomendations for the Microsoft team.

***
Questions:
* What genre of movies are most profitable?
* What is the optimal time of year to maximize profits?
* Does higher average rating drive profitability?
***

## Data

The data being used for this project came from a multitude of sources:
* Box Office Mojo
* IMDB
* TheMovieDB.org

__Notes:__ 
_Box Office Mojo by IMDbPro receives data from a variety of sources, including film studios, distributors, sales agents, and others from around the world._
_The Movie Database (TMDb) is a community built movie and TV database. Every piece of data has been added by their community dating back to 2008._

The following datapoints where operationalized as:

* Profitability - total, domestic and foreign gross. 
* Seasonality - time of year as month. 
* Genre - type of genre defined by [IMDB tags](https://help.imdb.com/article/contribution/titles/genres/GZDRMS6R742JRGAG#)

Datapoints most prominently utilized in our analysis were:
* Domestic, Foreign and Total Gross - reported in $USD modeled continously
* Release date - reported by MM/DD/YYYY of original theater release date modeled categorically
* Genre - modeled categorically
* Average Rating - 10 point likert modeled continously

## Methods

Descriptive statistics and histograms were created for continous variables to identify outliers and missing values. Once these were identified, appropiate action was taken to remove or transform to facilitate analysis. Value counts were calculated for categorical variables to assess distributions, cell counts and missing values. Categories were excluded or collapsed as necessary as detailed in our Jupyter Notebook. Our final analysis consisted of various visualizations addressing our three key questions of interest. Scatterplots were utilized when the variables were both continous, and barcharts used when summarizing continious variables across categories. 

## Results

Present your key results. For Phase 1, this will be findings from your descriptive analysis.

***
Questions to consider:
* How do you interpret the results?
* How confident are you that your results would generalize beyond the data you have?
***

### Figure 1
![Figure 1](./images/total_gross.png)

* Sci-Fi, Animation and Adventure have median gross profits > 200 million
* Action and Fantasy have mean gross profits > 200 million with median < 100 million
* Sport, Romance, War and Documentaries were the least profitable with < 50 million mean 

### Figure 2
![Figure 2](./images/multigenre_total_gross_restrict_years_tenObs.png)

Four cross-classified categories were significantly more profitable then the rest.

These were:
* Action, Adventure, Sci-Fi
* Action, Adventure, Fantasy
* Adventure, Animation, Comedy
* Action, Adventure, Comedy

### Figure 3
![Figure 3](./images/avg profit by month 2015 to present.png)

### Figure 4
![Figure 4](./images/total_gross.png)

## Conclusions

Provide your conclusions about the work you've done, including any limitations or next steps.

***
Questions to consider:
* What would you recommend the business do as a result of this work?
* What are some reasons why your analysis might not fully solve the business problem?
* What else could you do in the future to improve this project?
***

## For More Information

Please review our full analysis in [our Jupyter Notebook](./dsc-phase1-project-template.ipynb) or our [presentation](./DS_Project_Presentation.pdf).

For any additional questions, please contact **name & email, name & email**

## Repository Structure

Describe the structure of your repository and its contents, for example:

```
├── README.md                           <- The top-level README for reviewers of this project
├── dsc-phase1-project-template.ipynb   <- Narrative documentation of analysis in Jupyter notebook
├── DS_Project_Presentation.pdf         <- PDF version of project presentation
├── data                                <- Both sourced externally and generated from code
└── images                              <- Both sourced externally and generated from code
```
