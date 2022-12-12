# Olimpic-Medal-Predicter
## Project Intro
  - The main goals of this project were to gain experience conducting exploratory analisis on a dataset as well as using scikit learn to create machine learning models.
  - I then cleaned the dataset and created some new features from the provided data to help with exploratory analisis and model bulding.
  - For exploratory analisis I was mainly interested in seeing what were the common factors of countrys that performed well in the olimpics.
  - For the model I created a knn and random forest classifier and optimized them with a gridsearch to attempt to predict whether someone would win a gold medal or not.

## Resources Used
  -  Python 3.9
  - Jupiter Notebooks and Spyder IDE
  - Libraries: Pandas, MatplotLib, Seaborn, Scikit Learn, Numpy.
  - Corelation Heatmap article: https://medium.com/@szabo.bibor/how-to-create-a-seaborn-correlation-heatmap-in-python-834c0686b88e 
## Data Cleaning
  - Concatanated Summer and Winter datasets and mearged the country dictionary data.
  - Created dummy variables for the medal that the athelete won.
  - Created feilds that show how many previous medals of each type the atheleate had won.
## Exploratory Analisis
**For the EDA I broke the anilisis into two parts, those being the exploration of the continuos variables and the catigorical variables.**

**When looking at the continuos variables there are three key take aways I found.**
  - Firstly most of the continuos variables are not normaly distributed so it will probably be worth trying to normalize them when we apply this data to our Gold medal clasification model.
  - Second when we looked at he corelation heat map we could see that Previos_Medals_Won was very highly corelated with the other previos medal variables as intuition would assume, this means that we should experiment with leaving it out of our Gold medal clasification model in attempts to avoid multicolliniarity.
  - Lastly, all of the previos medal one histograhms showed that there is a very small sample size of people that have been able to maintin podium placing abillity over the years it it would probalbly be vary interesting to look a those few examples to see if we can find any similaritys between them.

![Corelation HeatMap](pictures/Corelation_hm.PNG)

**Within the catigorical variables there was a lot of interesting findings but these were the ones i found most notable.**
  - Aquatic sports are the most prevelent sports at the olimpics followed closly by Athetics so if your a country and your goal is to come home with the most medals i think it is a reasonable stratagy to invest the most amount of money into those sports.
  - The USA has one around twice as manny gold medals as the nex higest country.
  - Throughout the time frame this data was collected there have been around twice as manny mens medals awarded as wommens medals.

![Top 20 Countries](pictures/Top20_Countrys_bar.PNG)     ![Top 20 Sports](pictures/Top20_Sport_bar.PNG)

**I then created a couple of piviot tabels that i was ablue to use to draw the following conclutions.**
  - The USA has won the most medals and has also won the most medals in aquatics, this is very interesting because it     shows either that the USA knows that aquatics are the most frequent sport in the olimpics and have therefor invested    more resorses into that programe. Or since they have one the most medals overall they have probalby won the most medals in alot of sports, so it would be worth looking at this a proportion if I was going to expolore any further.
  - Population was not have as big a factor in the number of gold medals a country had won as I had thought it would.
  - GDP per Capita was not have as big a factor in the number of gold medals a country had won as I had thought it would.

![Gold by Country and Population](pictures/Gold_by_Country_and_Pop_piv.PNG)      ![Gold by Country and Sport](pictures/Gold_by_Country_and_Sport_piv.PNG)

## Building The Model
For the model I wanted to build somthing that would be able to predict whether or not an athelete would win gold.
  - I started by picking the variables that I thoght would work best with the types of models i was planning on using as well as variable that would have as little multicolliniarity as posible
    - I ended up chooseing 'Year', 'Sport', 'Discipline', 'Country', 'Gender', 'Population','GDP_per_Capita', 'Prev_Gold_Medals_Won', 'Prev_Silver_Medals_Won', 'Prev_Bronze_Medals_Won'
  - I then used pandas to turn my selected variables into dummy variables 
  - Using Scikit Learn I created train test split where 80% of the data was training data and 20% was test data.
  - I decided to build both a knn and random forest classification models and compare the results to find which model preformed best with this data.
  - Once I had the basic models constructed i used GridsearchCV in order to optimize the models.
  ### Model Results
  I used accuracy as my metric for the models.
  
  **knn**: 
  
  **Random Forest**: 
  
  ### Model Flaws
  Since my data was only from people who has placed on the podium at the olimpics my model does not predict the whether or not an olimpic athelete will win gold, it predicts whether or not an olimpic athelete will win gold given they placed on the podium. This obviously limits the aplication of this model in the real world greatly.
