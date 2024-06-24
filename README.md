# The Fall of the Soviet Union and its effects on American space flight

 

## Table of Contents

1. [Overview](#overview)
2. [Proposal](#proposal)
3. [The Data](#the-data)
4. [Data Cleaning](#data-cleaning)
5. [Visualizations](#visualizations)
6. [Conclusion](#conclusion)


## Overview

The launch of Sputnik-1 marked the start of the Space Race between the United States and the Soviet Union. Throughout the years, the Soviets would dominate space, reaching new milestones left and right. The US would respond to Sputnik by racing to establish the National Aeronautics and Space Administration (NASA). Each Space Agency (NASA and the Strategic Rocket Forces of the Russian Federation - RVSN) would both compete in what is now dubbed the 'Space Race', a product of the Cold War which pitted the two countries against each other to reach new milestones in the exploration of Space. The end goal for both countries was the Moon, which President John F. Kennedy stated that the US would send humans by 1970. This would occur in 1969, and to the American public was essentially the culmination of the space race. However, the Soviets would continue to launch plenty of rockets in order to further their military and technological prowess in Space. The Soviets would suffer different setbacks geopolitically however in the late 70's and early 80's, and the Soviet Union would ultimately fall in 1991. This set back the russians heavily, with funding for Space Launches dropping and the number of launches dropping significantly. It wouldn't be until the mid 2000's that Roscosmos (the russian federation's launch agency) would bounce back and start launching not only their own satellites and missions again, but outsourcing their cheap SLV's (Space Launch Vehicles) to other countries, and even the United States. From 1991 to the mid 2000's, NASA had no competition and public support for sending more explorative launches up. However, with the explosion of technology during this period, commercial space became much more lucrative. This opened the doors for SpaceX and ULA to find cost effective measures to reach space efficiently, and would soon essentially replace NASA entirely, with the US government awarding the two companies contracts to send different payloads into orbit as well.



## Proposal

The fall of the Soviet Union played a key role in allowing companies such as SpaceX and ULA to become major players in the commercial Space Launch industry. 



## The Data

The dataset titled 'All Space Missions from 1957' (found [here](https://www.kaggle.com/datasets/agirlcoding/all-space-missions-from-1957?resource=download)) The data can be found in one CSV file, and has a shape of 4,324 rows and 9 columns. Those columns were... 

- Two unnamed columns counting each row
- 'Company Name' denoting which particular company / organization launched each SLV
- 'Location' showing which launch site was used
- 'Datum' which had a string valued and a detailed down to the minute day and time of launch
- 'Detail' explaining what rocket was used / its payload
- 'Status Rocket' having two string values inside, the two being 'StatusActive' or 'StatusRetired'
- 'Rocket' which didn't provide much explanation for, just had numeric float values
- 'Status Mission' which like the Status Rocket column, had two values string. 'Success' or 'Failure'




## Data Cleaning

With these columns in mind all I wanted from the dataset was how many launches occured on or near the fall of the Soviet Union, separated by the individual organizations that launched. 

Originally, cleaning the data only took a little bit of effort. I started by dropping the first two unnamed columns that provided no value to the dataset. Then, I noticed the 'Datum' column was a string value with the dates including the date and time down to the minute of each launch. My first thought was to clean this column by only taking 

Overall, the dataset itself was not cluttered and did not have any major cleaning required. The biggest hurdle was changing the 'Datum' column into a more useful pandas datetime object. 

There were no outliers in this dataset.



## Visualizations

### NASA vs USSR comparison

![NASA USSR comparison](images/nasa-ussr-comparison.png)

### US based companies comparison

![NASA USSR comparison](images/nasa-spacex-ula-2000-and-onward.png)

### Adding Russia to the mix

![NASA USSR comparison](images/russia-comparison.png)

## Conclusion

The Fall of the Soviet Union drastically effected the amount of launches that the United States was doing. In the early 2000's, NASA would pivot to a different focus, from exploration to research and development. This, paired with the rising commercial value of space allowed for companies like SpaceX and ULA to find cost effective ways to send payloads into space, and ultimately led to those companies and others to take the reigns in regards to the space launch industry. According to the data, NASA has completely stopped sending their own rockets and payloads into space. It is almost ironic that after the fall of the Soviet Union, capitalism prevailed and now civilian companies are outpacing every other nation on the planet, and doing it in a very cost effective measure. This provides us with a brief glimpse at a possible future of Space Flight and exploration, where the motives to send things up have shifted from more of a political and militaristic reason, to more of a profit oriented reason. 