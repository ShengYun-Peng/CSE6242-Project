# CSE6242-Project

### Description

* Twitter visualization: A world globe is shown with the numbers of COVID-19 tweets from worldwide geographic coordinates. 
A higher and redder bar represents more tweets from one location. 
The total number of COVID-19 related tweets in the 2021 March and April is listed. 
Two bar charts are shown for the most common tweet countries and languages.
* WordCloud: The COVID-19 tweeter word clouds is generated to analysis the relationship between COVID-19 related tweets focus and the severity of COVID-19.The data is cleaned by filtering out most non-English vocabularies and words with repetitive meaning. The results are shown below, the font size is determined by the frequency of words appearing in tweets. 


### Proposal
Video: https://youtu.be/qlcI9DYTQEI 

### Final
1. Install dependencies
```shell
npm install
```
You may need the following code to fix all the warnings
```shell
npm audit fix --force
```

2. Run 
```shell
npm run start
```

3. Click the "Click to View Twitter" button in the top right corner to view the Twitter Visualization. 
Then click the "Back" button to return the COVID Visualization.

4. Packages

* [globe.gl](https://github.com/vasturiano/globe.gl): provides data visualization layers on a 3-dimensional globe in a spherical projection

* [d3-cloud plugin](https://github.com/jasondavies/d3-cloud): provides the layout, font size, rotation and other useful feature, to generate fancy word clouds
