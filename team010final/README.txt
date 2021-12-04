DESCRIPTION
Our project is a COVID-19 cases and Twitter data visualization website. There are 3 main visualization parts in our project
- Covid visualization: a globe placed in the center of the screen with line charts and numbers on both sides displaying worldwide stats related to COVID-19. Dragging along the slide bar below, color scheme of each country shown on the globe varies according to the severity of Covid in that region. Meanwhile, the total numbers of confirmed cases, deaths and recoveries change dynamically on the right according to the selected date.
- Twitter visualization: A world globe is shown with the numbers of COVID-19 tweets from worldwide geographic coordinates. A higher and redder bar represents more tweets from one location. The total number of COVID-19 related tweets in the 2021 March and April is listed. Two bar charts are shown for the most common tweet countries and languages.
- WordCloud: The COVID-19 tweeter word clouds is generated to analysis the relationship between COVID-19 related tweets focus and the severity of COVID-19.The data is cleaned by filtering out most non-English vocabularies and words with repetitive meaning. The results are shown below, the font size is determined by the frequency of words appearing in tweets.


INSTALLATION
1. cd to CODE folder
2. Make sure the latest npm is installed and run "npm run start"

Packages used in the code:
- globe.gl: provides data visualization layers on a 3-dimensional globe in a spherical projection
- d3-cloud plugin: provides the layout, font size, rotation and other useful feature, to generate fancy word clouds

EXECUTION
1. Click the "Play" button to see the evolution of the COVID-19 cases.
2. Check the total cases on the right
3. Hover on a country to visualize the daily cases
4. Click the "Click to View Twitter" button on the top right corner to visualize the Twitter Data 
5. Rotate and zoom in and out the globe to compare the Tweets number
6. Then click the "Back" button to return the COVID Visualization.

DEMO VIDEO
https://youtu.be/W_0iZo7d59U
