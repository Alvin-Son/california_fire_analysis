# **West Coast Fire Analysis**

## **Overview:**
This project aims to analyze the relationship between climate variables and wildfire occurrences in California. Our goal is to seek to understand how monthly rainfall and temperature affect fire frequency across different counties, providing insights into how impacts of climate change may affect wildfire dynamics in the future.

## **Team Members:**
Alvin,
Debbie,
Nicole,
Nicholas,
Zahraa.

## **Background:**
With the increasing frequency and severity of California wildfires, likely exacerbated by drought conditions and climate change, this project explores the relationship between climatic factors and wildfire occurrences over the past decade.

## **Research Questions:**
1. What are the basic weather and fire trends in California over the past 10 years?

2. How does historical average monthly rainfall and maximum temperatures correlate with wildfire frequency, size, and duration?

3. Which counties are most affected by wildfires, and how do climatic fluctuations influence this?

## **Data Sources and References:**
### CA Fire data by county (2013-2024)

- Available at: https://www.fire.ca.gov/incidents

### California Weather data - 2013-2024

### California Open Data Portal - County boundaries
- Available at: https://data.ca.gov/dataset/ca-geographic-boundaries/resource/b0007416-a325-4777-9295-368ea6b710e6

### NOAA Climate Data

- NOAA National Centers for Environmental information, Climate at a Glance: County Mapping, published April 2024, retrieved on April 9, 2024. Available at: https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/county/mapping

### Additional historical data from WA Fire (1973-2023)

## **Tools and Libraries Used:**

Python: For data manipulation and analysis

Pandas: For handling data structures

Matplotlib: For creating visualizations

NumPy, SciPy: For numerical operations

Setup and Installation

## **Description of collection and cleanup processes**

**Collection and Exploration**

The collection of fire data was a simple csv download including records for each incident from 2013 to present. Weather data was more complicated to obtain because of an incomplete API database. The team resorted to downloading weather csv data manually in bulk for the desired timeframe, but were only able to get monthly data. Data exploration revealed that the fire data included 2000+ records of incidents including the number of incidents, acres burned, and the duration by county, including location. Weather data gathered included total monthly rainfall and max monthly temp by county.

**Data Cleaning and Preparation**

Cleanup and preparation was relatively straightforward. This involved looping through and merging 240 weather csvs, as well as extracting the month and year from the header and inserting this as two new columns for each month obtained. Fire Data was more challenging as there were many null values, duplicate records, extreme outliers and multiple values merged into one row where fires spread across county boundaries. Fire data included individual incident records, so the data had to be summarized by month in order for it to be compared to monthly weather data. Grouping fire data by month was the only option, but it was clear that this may skew the results and smooth out useful nuances of individual fire events that would be more accurately compared to daily weather conditions.

**Limitations to Analysis**

The biggest limitation to the analysis was the availability of weather data and the scope of the project. Due to time and resource constraints, the project went ahead using monthly rainfall and max temperature data, when it would have been more accurate to use daily weather data. Monthly data was a challenge since it is hard to compare accurately to fire data. Individual fires vary in duration, from as little as 1 day to over a year in some cases. More specifically, nearly 50% of fires lasted less than 1 week, and nearly 40% of fires lasted more than two months. This means that monthly aggregate weather data was a poor comparison to fires that either occurred on a specific day with specific weather conditions, or occurred over several months. Furthermore, due to a short time frame the project was only able to look at two weather variables, when there are many others that would likely have a significant impact on fire occurrence, duration and size. Two  obvious factors include wind speed and groundwater resources.



## **Analysis**

### **Major Findings and Implications:**
The analysis conducted sought to uncover relationships between climate variables—specifically monthly rainfall and maximum temperatures—and wildfire occurrences in California. Contrary to the initial hypotheses, the findings indicate only weak correlations between these climatic factors and the frequency, size, and duration of wildfires at an average monthly level. This suggests that while temperature and rainfall alone may play a role in wildfire dynamics, additional weather related factors are also likely to play a significant role. Other, non-weather related factors, such as land management practices, human activities might also have an impact. These results underscore the complexity of wildfire causation and highlight the need for comprehensive approaches in wildfire research and prevention strategies.

### **Answers to Specific Research Questions:**

1. What are the basic weather and fire trends in California over the past 10 years?
2. How does historical average monthly rainfall and maximum temperatures correlate with wildfire frequency, size, and duration?
3. Which counties are most affected by wildfires, and how do climatic fluctuations influence this?

### **1. Trends in Weather and Fire Over the Past 10 Years:**

### **1.1. 10-year average rainfall and max temperature maps***

The first map shows average total rainfall by county over the whole 10 year period (2013 - 2023). Darker shades of blue indicate counties with higher average rainfall, and lighter shades of blue indicate counties with lower average rainfall. The orange dots overlaid are sized according to the number of fire incidents per county over the study period. While not a strong relationship, the map shows that counties in the central part of the state have had collectively fewer fire incidents than counties in the northern and southern counties. This finding would however, require greater analysis to determine if this finding is of value. Further analysis could look to compare particular years to see how these patterns might change.
<img width="1033" alt="Screen Shot 2024-04-18 at 3 20 43 PM" src="https://github.com/NicholasJWiid/project_1_WC_fire_analysis/assets/159491405/9d39e9df-7c6f-4366-b6da-7bf451119936">

The second map below shows the average maximum temperatures by county over the 10 year study period, using a color gradient from light yellow to dark green, with darker areas indicating lower maximum  temperatures. The red dots overlaid show all the fire locations for the 2000+ fires between 2013 and 2023. These records are sized according to the total acres burned for each incident. It appears that the acres burned by each fire varies from each county independently from the 10 year average maximum temperature.There are cases where the fire covers a large amount of ground in both moderate temp and higher temp counties. This implies that the size of fires are at a very high level not directly related to the 10 year average maximum temperatures. Further analysis could again look to compare particular years to see how these patterns might change.
<img width="1170" alt="Screen Shot 2024-04-18 at 3 24 52 PM" src="https://github.com/NicholasJWiid/project_1_WC_fire_analysis/assets/159491405/d18e96aa-499a-40c3-9e54-cd1d48d69eb9">

### **1.2 Yearly fire incident counts vs. annual average rainfall and max temperature**

Weather and fire data were analyzed on a year by year basis, revealing slight upward trends in temperatures after 2019 and variable rainfall patterns over the decade. Despite these changes, the statistical correlation between these weather conditions and the number of incidents per year proved to be weak. 

The data on the average temperature and total fire incidents by year reveal a complex relationship. The variability in fire incidents across the years does not always align with the changes in temperature, although there at times appears to be a mild synchronization of these two patterns. A drop in temperature from 2015 to 2019 only shows a drop in fire incidents from 2017, while a slightly warmer 2020 does show a slight increase in number of incidents. These weak observations suggest that on a broad annual level, annual average max temperature alone is not likely to have much influence on the number of fire incidents annually.
<img width="927" alt="Screen Shot 2024-04-18 at 3 28 22 PM" src="https://github.com/NicholasJWiid/project_1_WC_fire_analysis/assets/159491405/bc767115-958a-42bd-bc8d-942bd407c3f3">

Similar to the average temperature, an analysis of average rainfall also showed that there does not appear to be a direct correlation between annual average rainfall across the state and the number of fire incidents on a year by year basis. Years with higher rainfall do not consistently correspond to fewer fire incidents, and vice versa. 
<img width="984" alt="Screen Shot 2024-04-18 at 3 29 56 PM" src="https://github.com/NicholasJWiid/project_1_WC_fire_analysis/assets/159491405/43e6bbde-4146-47aa-bed1-92372ef2aa9d">

Further analysis for both rainfall and temperature could consider more localized comparisons on a county by county basis for selected years of interest.

### **2. Relationship Between Climate Variables and Wildfires:**

**2.1 Correlation**

The analysis of the relationship between total monthly rainfall and total monthly acres burned by wildfires indicates a very weak negative correlation. This is the right direction of relationship that the study hoped to uncover (increasing rainfall related to decreasing fire size), but an r-value of -0.04  points to a lack of meaningful linear connection of these variables. This is further supported by the nearly horizontal regression line observed in the plot. The scatter plot points vary in size, corresponding to the average duration of fires, but do not exhibit a clear connection with either rainfall or acres burned.

Most fire incidents correspond to total monthly rainfall of less than 1 inch, and there is a broad range of variability in the acres burned regardless of the amount of rainfall. This helps to underscore the complexity of factors that influence wildfire behavior, and specifically the limitations regarding using monthly rainfall values.
![image](https://github.com/NicholasJWiid/project_1_WC_fire_analysis/assets/159491405/7793e012-9844-4bec-ad42-1dee4b18eb61) 

In the analysis examining monthly max temperature against total monthly acres burned, a very weak positive correlation is noted with an r-value of 0.10. The line shows a very slight upward trend where higher temperatures are associated with larger fires, but again the relationship is still very weak.
The varying sizes of the data points, which represent the average fire duration, do not present any discernible pattern with temperature, underscoring the likelihood that additional factors beyond temperature contribute to the severity and longevity of fires. 

The dispersion of data across the temperature spectrum further suggests that monthly max temperature is not a robust standalone predictor of total monthly fire severity.

These findings indicate that while there is some level of association with maximum temp and acres burned (and to an even lesser extent rainfall), there are almost certainly other variables not included in this study that are likely to play an additional and possibly even collective role in influencing wildfire outcomes.
![image](https://github.com/NicholasJWiid/project_1_WC_fire_analysis/assets/159491405/bcfe48fa-63d2-40ba-9c62-a7e8dd281e82)

Further analysis would look at much more granular weather data in order to compare with fire events that are happening on various time scales, from 1 day to 1 year, according to the data. 

**2.2 Summary statistics table - All variables**

The table below shows summary statistics for the three main fire variables. A few things to highlight include:

- A high mean and much lower median for both acres burned and fire duration, show the vast variability of the data. The median values show that half the fires are 6 days or less in duration and are also relatively small in size. The mean shows us that we have a very skewed dataset, and suggest that there are a smaller number of fires that had a massive impact.
<img width="683" alt="Screen Shot 2024-04-18 at 3 35 17 PM" src="https://github.com/NicholasJWiid/project_1_WC_fire_analysis/assets/159491405/840913c7-13b5-49bf-9678-eaf539d30dd4">

Further analysis could look deeper into the statistical characteristics of the dataset, looking to isolate outlier events and study the weather conditions before, during and after such an occurrence.

### **3. Impact on Specific Counties:** ![image]
**3.1 Top 5 county fire incidents by year**

The County plot below highlights the annual fire incident counts for the top 5 counties with varying fire activities. Different colors represent each county, while the marker size reflects the scaled-down average acres burned. 

Riverside County’s fire acres burned appears relatively consistent over the years, whereas Shasta County displays much more fire size variability with the largest total acres burned compared to other counties.

Unsurprisingly, the fire incidents lack any uniform trend across all counties, further showing the year on year variability in each county. 
<img width="1120" alt="Screen Shot 2024-04-18 at 3 38 32 PM" src="https://github.com/NicholasJWiid/project_1_WC_fire_analysis/assets/159491405/31f16648-b85e-46a7-9193-9481751f3ce6">

Further analysis could look to compare individual county fire trends with localized weather patterns, looking at a more granular weather level, and perhaps focusing on the specific daily and weekly weather variables surrounding particularly significant fire events.

**3.2 10-year average max temperature by county with top 5 acres burned overlay**

The map below again shows the 10 year average max temperatures by county with the overlaid values for total acres burned for the top 5 most affected counties for the same period. The hover labels show the actual acres burned per county in the Final Analysis notebook, so the size of the red dots here is just relative, with Shasta in the North shown to be the most affected county.
<img width="1159" alt="Screen Shot 2024-04-18 at 3 40 17 PM" src="https://github.com/NicholasJWiid/project_1_WC_fire_analysis/assets/159491405/c7f7c6dd-4e58-4a2a-9d79-00961b6bd5d8">

### **Interpretation and Next Steps:**

Given the weak correlations found in this study, it is advisable to:
- Expand the scope of data collection to include additional weather variables, e.g. wind, ground water levels, drought indexes, and non-weather variables, e.g. land use changes, forestry management practices, and human activity patterns.
- Gather weather and other data on a daily basis in order to fully investigate the relationship between fire and weather variables. Drought risk index levels (often a combination of rainfall and temperature variables), daily wind speed and fluctuation in groundwater are seen to be the most obvious and potentially influential additional factors that would need to be factored in.
- Dive deeper into the analysis of the fire data, in terms of accuracy and reliability, but also from the perspective of being able to prepare it more thoroughly for comparison with weather variables. This is important for two reasons:
  1. Because fires last for varying lengths of time, aggregating data by month does not give an accurate representation of an individual fire's impact. Each individual fire occurrence would also need to be compared to the weather variables for the same date range, with additional local factors considered, to get a more accurate sense of any relationship.
  2. Many fires cross county boundaries, yet the data is consolidated. More work would be required to accurately separate the impact of the fire for each county instead of simply assuming it was equal for all counties affected.
- Employ multivariate analysis techniques to explore complex interactions between various potential risk factors.
- Consider qualitative research to complement quantitative findings, potentially offering insights into regional differences and specific risk factors not captured by this study.


# **Conclusion:**
This high level analysis exploring the relationship between monthly rainfall, temperature variables and aggregate monthly wildfire frequency, size, and duration in California over the past decade reveals a weak relationship. These findings challenge the initial idea that rainfall and max temperature at a monthly level would show significant influence on wildfire occurrence and intensity. The results suggest instead that there are many additional factors to consider. The limited impact of the studied weather variables underscores the complexity of wildfire causation and emphasizes the need for a broader investigative approach, including more granular weather data, an improved strategy for normalizing fire data so that it can be more easily compared to weather variables, and the consideration of a variety of other environmental and anthropogenic factors. With greater resources and time, such an approach would be able to provide much greater insight into the relationship between fire and weather variables, leading to the development of more effective wildfire research programs and prevention and preparation strategies.
<<<<<<< HEAD
>>>>>>> 7d75a7f (Update README.md)
=======
>>>>>>> aa15833b6feb4239254b4d9773772e6587abbb91
