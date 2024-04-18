# **West Coast Fire Analysis**

## **Overview:**
This project analyzes the correlation between climate variables and wildfire occurrences in California. Our goal is to understand how monthly rainfall and temperature affect fire frequency across different counties, providing insights into the impacts of climate change on wildfire dynamics.

## **Team Members:**
Alvin,
Debbie,
Nicole,
Nicholas,
Zahraa.

## **Background:**
With the increasing frequency and severity of California wildfires that has likely exacerbated by drought conditions and climate change, this project explores the relationship between climatic factors and wildfire occurrences over the past decade.

## **Research Questions:**
What are the basic weather and fire trends in California over the past 10 years?
How does historical average monthly rainfall and maximum temperatures correlate with wildfire frequency, size, and duration?
Which counties are most affected by wildfires, and how do climatic fluctuations influence this?

## **Data Sources:**
CA Fire data by county (2013-2024)

Rainfall and temperature data by county and month (2013-2024)

Additional historical data from WA Fire (1973-2023)

## **Tools and Libraries Used:**

Python: For data manipulation and analysis

Pandas: For handling data structures

Matplotlib: For creating visualizations

NumPy, SciPy: For numerical operations

APIs, JSON: For data interaction and format handling

Setup and Installation

## **References**

California Fire Incidents

NOAA Climate Data



## **Analysis and Conclusion**

## **Major Findings and Implications:**
The analysis conducted sought to uncover relationships between climate variables—specifically monthly rainfall and maximum temperatures—and wildfire occurrences in California. Contrary to initial hypotheses, the findings indicate only weak correlations between these climatic factors and the frequency, size, and duration of wildfires. This suggests that while climate may play a role in wildfire dynamics, other factors like land management practices, human activities, and perhaps less obvious aspects of the local microclimate might have more significant impacts. These results underscore the complexity of wildfire causation and highlight the need for comprehensive approaches in wildfire research and prevention strategies.

## **Answers to Specific Research Questions:**

1. What are the basic weather and fire trends in California over the past 10 years?

2. How does historical average monthly rainfall and maximum temperatures correlate with wildfire frequency, size, and duration?

3. Which counties are most affected by wildfires, and how do climatic fluctuations influence this?

## **1. Trends in Weather and Fire Over the Past 10 Years:**
Both climatic and fire data were thoroughly analyzed, revealing slight upward trends in temperatures after 2019 and variable rainfall patterns over the decade.
Despite these changes, the statistical correlation between these weather conditions and the number of incidents per year proved to be weak. 

The data on the average temperature and total fire incidents by year reveal a complex relationship. The variability in fire incidents across the years does not always align with the changes in temperature. 
For instance, a drop in temperature from 2015 to 2019 isn't mirrored by a drop in fire incidents, and a cooler 2019 still sees a high number of incidents. 
These observations suggest that temperature is not the sole factor that influences the count of fire incidents.

Similar to the average temperature, an analysis of average rainfall also showed that here does not appear to be a direct correlation between rainfall and the number of fire incidents, as years with higher rainfall do not consistently correspond to fewer fire incidents, and vice versa.

## **2. Relationship Between Climate Variables and Wildfires:**
The analysis of the relationship between total monthly rainfall and acres burned by wildfires indicates a very weak negative correlation, with an r-value of -0.04, pointing to a lack of meaningful linear connection. This is further supported by the nearly horizontal regression line observed in the plot. The scatter plot points vary in size, corresponding to the average duration of fires, but do not exhibit a clear correlation with either rainfall or acres burned. 
Most incidents occur with less than 1 inch of rainfall, and there is a broad range of variability in the acres burned regardless of the amount of rainfall, underscoring the complexity of factors that influence wildfire behavior.

In the analysis examining max temperature against acres burned, a very weak positive correlation is noted with an r-value of 0.10. Though the relationship is not strong, the line is hinting at a slight upward trend where higher temperatures may be associated with larger fires. 
The varying sizes of the data points, which represent the average fire duration, do not present any discernible pattern with temperature, underscoring the likelihood that additional factors beyond temperature contribute to the severity and longevity of fires. 
The dispersion of data across the temperature spectrum further suggests that max temperature is not a robust standalone predictor of fire severity.

These findings indicate that while there is some level of association with maximum temp and acres burned, other variables not included in this study likely play a more crucial role in influencing wildfire characteristics.

## **3. Impact on Specific Counties:**
The County plot highlights the annual fire incident counts for the top 5 counties with varying fire activities. Different colors represent each county, while the marker size reflects the scaled-down average acres burned. 
Riverside County’s fire incidents appear consistently over the years, whereas Shasta County displays several years with a notably large number of incidents, suggested by larger markers. 
But the fire incidents lack a uniform trend across all counties, which suggests that fire incidents in each county are influenced by unique local conditions and factors, which lead to various patterns and stability in the number of fire incidents from year to year.

## **Interpretation and Next Steps:**
Given the weak correlations found in this study, it is advisable to:
Expand the scope of data collection to include variables such as wind, ground water levels, drought indexes, land use changes, forestry management practices, and human activity patterns.
Employ multivariate analysis techniques to explore complex interactions between various potential risk factors.
Consider qualitative research to complement quantitative findings, potentially offering insights into regional differences and specific risk factors not captured by this study.

## **Conclusion:**
In conclusion, our comprehensive analysis exploring the relationship between climate variables and wildfire occurrences in California over the past decade reveals only weak correlations between monthly rainfall, maximum temperatures, and wildfire metrics such as frequency, size, and duration. This finding challenges the initial hypothesis of a strong climatic influence on wildfires, suggesting instead that other factors may play more substantial roles. The limited impact of the studied climate variables underscores the complexity of wildfire causation and emphasizes the need for a broader investigative approach that includes a variety of environmental and anthropogenic factors to develop more effective wildfire research and prevention strategies.






