# README
## 3D-visualization-of-hydrocarbons-concentrations-in-soil
### Overview
This project uses Scipy and PyVista to visualize isometric pollutant concentration (e.g. hydrocarbons), 

 the meteostat library to analyze climate data from Puebla, Mexico, focusing on precipitation and temperature trends from 1994 to 2024. The primary goal is to identify extreme weather events by calculating percentiles and return periods, and then visualizing these events using seaborn and matplotlib. Moreover, a brief introduction to meteostat is attached.

### How to use
1. Data Collection
- The project retrieves daily weather data from the Puebla meteorological station using the meteostat library.
- The data is collected for a 30-year period (1994-2024), ensuring 99.98% coverage after normalization.

2. Data Processing

- The dataset is normalized and missing values are interpolated to ensure continuity.
- Extreme weather events (precipitation and temperature) are identified using a Return Period (RP) approach based on the method by Camuffo, Becherini, & della Valle (2020).

3. Extreme Event Detection

- A percentile threshold is calculated for both precipitation and temperature to classify extreme events.
- The threshold value is used to identify days with extreme precipitation, extreme maximum and minimum temperatures, and extreme average temperatures.

4. Visualization

- Three main plots are generated:
  - Precipitation Plot: Shows the daily precipitation with extreme events highlighted in red.
  - Temperature Plot: Visualizes extreme maximum and minimum temperatures.
  - Average Temperature Plot: Highlights both high and low extreme average temperatures.
- All visualizations are saved as PNG files (prcp.png, tmin_tmax.png, and tavg.png).

### Outputs
- Precipitation Plot (prcp.png): Highlights days with extreme precipitation.
![prcp](https://github.com/user-attachments/assets/e4d22cbc-6fa2-4c17-9ae0-c6683cb09cf2)
- Temperature Plot (tmin_tmax.png): Shows extreme maximum and minimum temperatures.
![tmin_tmax](https://github.com/user-attachments/assets/e08238ba-558c-4f08-a6b5-377c14141c60)
- Average Temperature Plot (tavg.png): Displays extreme high and low average temperatures.
![tavg](https://github.com/user-attachments/assets/d7a4c63f-547b-4559-9639-a4b44948cfae)

### Conclusions
- Precipitation Extremes: The 1-year return period percentile threshold identified 13 extreme precipitation events over the 30-year period.
- Temperature Extremes:
  - Extreme Maximum Temperatures: 31 days were classified as extreme, indicating heat waves or abnormally high temperatures. This can have significant implications for health, agriculture, and energy consumption.
  - Extreme Minimum Temperatures: Similarly, 31 days were identified with extreme cold conditions, which may impact agriculture, infrastructure, and vulnerable populations.
  - 26 days showed extremely high average temperatures, while 27 days had extremely low average temperatures. This balance suggests periods of both intense heat and cold over the years, reflective of broader climate variability in the region.
 
### References

Camuffo, D., Becherini, F., & della Valle, A. (2020). Relationship between selected percentiles and return periods of extreme events. *Acta Geophysica, 68*(4), 1201–1211. https://doi.org/10.1007/s11600-020-00452-x
