# Group 39 Project Final Report - Gun Violence in America
#### Nolan Nishikawa - Rhys Smith - Luke Chapman

---
## Introduction
As many of us are aware, there are many problems in the United States that are constantly in news headlines and on social media. These things can range from being at a massive scale such as what is going on with the military or something as small as the latest thing that a celebrity has said on twitter. However, one topic that seems to always be pervasive in headlines has to deal with mass shootings and gun violence. With this also comes the many heated debates on what should be done in an attempt to try and fix this issue. While this topic in itself is something that is interesting and something that most people could debate about for days, what our group was wanting to look at was actual statistical evidence to see how bad this issue really is. As a result, we have found a data set that contains information about mass shootings in the United States, with mass shootings being defined as cases where there have been 4 or more victims as a result of the mass shooting (victims in this case refers to both killed and injured). The data set, spanning from the years 2014 to 2021, includes things such as the dates, locations, number of people killed, and number of people injured in each incident. 

## Explorator Data Analysis (EDA)
One of the things that was immediately made apparent was how severe mass shootings in the United States have been. One of the first things that was made apparent was just the sheer number of shootings that took place between 2014 and 2021. Just by looking at the number of cases, one of the first things that we can see is that there have been 2930 cases of gun violence that fall under the earlier definition of mass shootings. This number alone is already something that most people would be shocked at hearing, but this only gets more shocking when it is made apparent that the number of cases, 2930, is larger than the number of days in 8 years (also noting the fact that in the data set, the year 2021 only had data for about half of the year). That is an average of over one shooting every day over the span of 8 years. 

![Image showing the number of rows in the data set](images/NumberOfRows.png)

Another thing that our EDA made clear was the distribution of mass shootings in each of the states, with Illinois and California being the two most dangerous states, and Wyoming and Vermont being the two safest.

![Image showing number of shootings per state](images/NumberPerStateBar.png)

One final thing that was made clear, building off the last point made, is the distribution of people killed is each state, as well as the distribution of people injured in each state. The former point was looking at mass shootings as a whole, where as in this section we are going to break down these shootings and look at how lethal each case was.

### Number of Deaths by State

![Number of deaths heatmap](images/NumberOfDeathsHeatmap.png)

An alternative view of the above graph would be:

![Number of deaths boxen plot](images/NumberKilledBoxen.png)

### Number of Injuries by State

![Number of injuries heatmap](images/NumberOfInjuredHeatmap.png)

An alternative view of the above graph would be:

![Number of Injuries boxen plot](images/NumberInjuredBoxen.png)



Overall, through looking at our EDA's, we found that a lot of our preconceived notions about gun violence were validated by the data presented. There were also some cases where out data showed us that the situation with gun violence in the United States was much worse than we originally thought.

---

## Question 1 + Results (Rhys' Section)
### How many of the shootings in our data can be considered mass shootings and has the number of shootings been increasing in recent years?
The accepted definition of a mass shooting is defined as: "four or more people injured or killed per incident of gun violence." With that in mind, I have been looking at the frequency of injured or killed per incident analyzed. 
####
![Injured Frequency](../project-group39/images/injured_frequency_rhys.png)
####
In the above image, we can see that on average about 4 people were injured per incident. With some incidents even having greater than 15 or 20 people injured. 
####
![Killed Frequency](../project-group39/images/killed_frequency_rhys.png)
####
In the above plot, it appears that on average a little over 1 person was killed per incident recorded. With some rare but extreme cases where around 20 people were killed.

A majority of the shootings that have occurred in the past 7 years across the United States can be considered mass shootings. After analyzing our data, I can say that on average 4.97 people are either killed or injured per incident recorded which is greater than the required 4 killed or injured to meet the definition. This is quite conerning as I intitially thought mass shootings were relatively rare and did not make up a majority of the shootings over the past 7 years in the United States.
####
![Shootings by Year](../project-group39/images/per_year.png)
####

In the above image, we can see that the number of shootings has steadily risen over the 7 year period our data analyzed. 2020 appears to be by far the worst year which over 600 incidents alone. Even if we ignore the year 2020, the bar graph stills shows an upward trend in the number of shooting incidents between 2014 and 2020.
####



---

## Question 2 + Results (Nolan's Section)

---

## Question 3 + Results (Luke's Section)

---

## Conclusion