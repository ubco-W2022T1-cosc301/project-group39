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
### What percentage of shootings can be considered mass shootings and has the number of shootings been increasing in recent years?
The accepted definition of a mass shooting is defined as: "four or more people injured or killed per incident of gun violence." With that in mind, I have been looking at the frequency of injured or killed per incident analyzed. 
####
![Injured Frequency](images/injured_frequency_rhys.png)
####
In the above image, we can see that on average about 4 people were injured per incident. With some incidents even having greater than 15 or 20 people injured. 
####
![Killed Frequency](images/killed_frequency_rhys.png)
####
In the above plot, it appears that on average a little over 1 person was killed per incident recorded. With some rare but extreme cases where around 20 people were killed.

A majority of the shootings that have occurred in the past 7 years across the United States can be considered mass shootings. After analyzing our data, I can say that on average 4.97 people are either killed or injured per incident recorded which is greater than the required 4 killed or injured to meet the definition. This is quite conerning as I intitially thought mass shootings were relatively rare and did not make up a majority of the shootings over the past 7 years in the United States.
####
![Shootings by Year](images/per_year.png)
####

In the above image, we can see that the number of shootings has steadily risen over the 7 year period our data analyzed. 2020 appears to be by far the worst year which over 600 incidents alone, which is a very high number even considering the ongoing pandemic. Even if we ignore the year 2020, the bar graph stills shows an upward trend in the number of shooting incidents between 2014 and 2019. Which makes us question whether we should be more concerned about gun violence in our everyday lives and what can be done to help the situation and bring down the number of shootings.

For more information, [click the link here to take a more thorough look at my analysis notebook](notebooks/analysis1.ipynb)

####



---

## Question 2 + Results (Nolan's Section)
### How does the time that shootings take place affect how many shootings there are? And if so, what outside factor could possibly influence these results regarding the shootings?

In regards to my research question, one of the first things that I began to take a look at was the time of year that these shootings take place. Specifically, I wanted to see if there was some sort of trend regarding the number of shootings and what the current month of the year. With this, I also began to ask the further question if the weather during these months may or may not have played a factor in the number of shootings that have occured

![Correlation between Months and Number of Shooting in the United States](images/NumberOfShootingsUS.png)

As we can see in the graph above, there is a trend that is made very apparent and is noticed within the first couple seconds of looking at the graph. This trend shows that from 2014 to 2020, there is a significantly higher number of shootings take place during what would be the warmer/summer months of the year. From a logical standpoint (albeit, a very morbid one), this trend in data does make some sense. The warmer weather means it is far more likely that there are going to be people out and about in public, leading to a far higher chance that a mass shooting may occur. 

While this point in itself is worthwhile, I began to look at this and feel somewhat conflicted. Not every state is going to share the same range of weather and seasons. For example, the climate in Texas is very different from the climate in New York, with Texas being warmer year round and New York having a much colder winter. As a result, this left me questioning the validity of the graph above. For the United States as a whole, the above graph does a good job and showing the distribution of shootings for each month, it does not give you the entire picture. As such, did a deeper dive into individual states to see whether the earlier hypothesis of 'more shootings happen during the warmer/summer months' is still true. 

![Correlations between Months and Number of Shootings in Texas](images/NumberOfShootingTexas.png)

In the above, the number of shootings each month has been broken up just for the State of Texas. As we can see, the number of shootings does appear to somewhat follow the same trend as before. However, there is much more variability in all the bars on the graph. From this we can infer that in a warmer state, there is going to be higher numbers of shootings during what would typically be the colder months of the year. However, just this one graph may be not be substantial enough, so we can continue to look at other warmer states, like Arizona.

![Correlation between Months and Number of Shootings in Arizona](images/NumberOfShootingsArizona.png)

In the graph for Arizona, we see that the earlier hypothesis is almost completely untrue. This is due to the highest number of shooting occuring in months that would typically be seen as colder months. As a result, we can now make a firm conclusion that while yes, some of these warmer states may still follow the trend of  summer months having more shootings, overall there is much more variability, with there being some times where the state breaks away from the trend completely. 

However, what about states that get colder during the winter?

![Correlation between Months and Number of Shootings in New York](images/NumberOfShootingsNewYork.png)

![Correlations between Months and Number of Shootings in Minnesota](images/NumberOfShootingsMinnesota.png)

In the above two graphs, we can see that, the trend of more shootings during the summer months rings much more true. Even from just taking a glance at the graph for New York, it is made very clear that there are higher levels of gun violence in the months of June, July, and August. The same can be said for Minnesota where June has many more shootings than most of the other months of the year. From this, we can make the assumption that states that are going to get colder in the winter are going to more closely follow the trend the the entirety of the United States follows. 

After looking at both warmer and colder states, we can begin to make more reasonable assumptions for the United States as a whole. With this, we can determine that overall, the trend that United States follows is a trend that fits the data, with this trend showing that there is a tendency for mass shootings to occur more frequently during warmer months. It is still important to note the trend of each state individually, with warmer states having a trend with much more variability, while colder states tend to follow the same curve as the United States. 

For more information, [click the link here to take a more thorough look at my analysis notebook](notebooks/analysis2.ipynb)

---

## Question 3 + Results (Luke's Section)
### What states have the highest number of gun related violence and are their neighbouring states possibly affected by the high number of violence.

To answer this question we will be looking at the total sum of deaths in each state from 2019. 
####
![Killed Sum](images/KilledByStateBarplot.png)
####
As seen in the above visual we have Texas, California, Florida, and Illinois. These states and their neighbours will be the focus of this question which works well since all are separated from each other and we have some border states and some inland states to look at. 

Now while a simple bar graph can show the actual numbers really well, for someone without previous knowledge about the map of the United States it's hard to see the affect to neighbouring states. So for the next visual we have a map of each states to show the total number of gun related deaths in each state.
####
![Killed Map](images/NumberOfDeathsHeatmap.png)
####
Now that you can see the how the states neighbour each other, it's easier to see which states have the most and least number of deaths. So now we can look at the neighbouring states of the four states (Texas, California, Florida, Illinois). We can see that the total sum of deaths in each state slowly decreases as we move away from these states, with the lowest states being in the far northeast and the mid northwest. Now focusing on the nearest neighbours, we can see that these states like Georgia, Nevada, and Louisiana are some of the next highest in deaths. 

One important factor to consider when looking at the violent states, is the population of the state, since states with a high population have more chances of incidents than states with smaller populations. So to balance this we can compare the total number of violence to the total population of the state. 
####
![Killed Map Population](images/NumberOfDeathsPopulationHeatmap.png)
####
Now looking at the map when we take the total number of deaths per person in each state you can see that some of the highest states include Nevada, Louisiana, Missouri, and new Mexico. All of which are neighbouring states to the four violent states listed before. 

So since the neighbouring states have a higher number of gun related deaths per person compared to their main neighbour. It appears that they are affected by their neighbour of the four most violent states. So the states with the total most gun related deaths in the USA do appear not be limited to their border and their violence is spreading to their neighbours, resulting in a higher percentage of deaths in these neighbouring states. 

You can [find the full analysis notebook here, including the code and the data.](notebooks/analysis3.ipynb)


---

## Conclusion

After cleaning and analyzing the American gun violence data from 2014-2020, it gave way to many horrifying statistics that none of us knew before starting this project. The gun violence situation in the U.S. has grown considerably worse over the 7 year period and we have the data and graphs to prove it. While the term “mass shooting” gets thrown around after each tragic event, the reality of it is that over 50% of the shootings in the U.S can be considered mass shootings by definition. This was an eye opening statistic as previously to this we mainly thought a mass shooting was a relatively rare occurrence. After filtering and analyzing the data separated by states and months in a year, we were able to see that there is a visible curve to the data showing that mass shootings tend to happen in the warmer months of the year. It is also worth noting that the states which stay warmer year round follow this curve less than the states which have a greater variety in weather. We also found a relation between the number of gun related deaths in neighbouring state. By looking at the total in each state and comparing that to the population it was found that the states with the higher percentage of deaths to people were neighbouring the states that had the highest total number of gun related deaths. So it is appears that these gun related incidents are completely contained by border and are seeping into neighbouring states. After working with this gun violence data for the last couple months, we all learned many important statistics about gun violence and how frequent shootings really are in the U.S. We were all shocked by many of the statistics we found and now realize how bad the gun violence situation really is. With at least 1 shooting incident occurring each day and many of these having an average of 1 person killed and 4 people injured, we find these “one in a thousand” incidents are not as rare as we initially thought. Each of our separate analysis led all of us to a very similar conclusion, that the gun violence situation in the U.S is really as bad as it seems if not worse than we could have possibly imagined.
