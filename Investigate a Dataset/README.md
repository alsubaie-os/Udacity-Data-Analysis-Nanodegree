# Investigate a Medical Appointment No Show Dataset

## Table of Contents
<ul>
<li><a href="#intro">Introduction</a></li>
<li><a href="#wrangling">Data Wrangling</a>
    <ul>
        <li><a href="#data_cleaning">Data Cleaning</a></li>
    </ul>
</li>
<li><a href="#eda">Exploratory Data Analysis</a>
    <ul>
        <li><a href="#research_question_1">Research Question 1</a></li>
        <li><a href="#research_question_2">Research Question 2</a></li>
        <li><a href="#research_question_3">Research Question 3</a></li>
    </ul>
</li>
<li><a href="#conclusions">Conclusions</a></li>
</ul>

<a id='intro'></a>
## Introduction

> In this project, I will be analyzing data associated with medical appointments in Brazil. The dataset contains information about 100k medical appointments in Brazil and is focused on the question of whether or not patients show up for their appointment. A number of characteristics about the patient are included in each row.
> The dataset
> - 110.527 medical appointments
> - 14 associated variables (characteristics)
> - The most important one if the patient show-up or no-show to the appointment
> - What factors are important for us to know in order to predict if a patient will show up for their scheduled appointment?
> - The analysis will be done using Python libraries NumPy, pandas, and Matplotlib.
> - The dataset can be downloaded from [Kaggle](https://www.kaggle.com/joniarroba/noshowappointments).


<a id='wrangling'></a>
## Data Wrangling

> In this section of the report, I will load in the data, check for cleanliness, and then trim and clean the dataset for analysis.
> - Load the data and print out a few lines. Perform operations to inspect data types and look for instances of missing or possibly errant data.


<a id='data_cleaning'></a>
### Data Cleaning

> - Drop unused columns
> - Rename columns
> - Convert data types
> - Drop duplicates
> - Drop rows with missing values
> - Drop rows with invalid values


<a id='eda'></a>
## Exploratory Data Analysis

> In this section of the report, I will compute statistics and create visualizations with the goal of addressing the research questions that I posed in the Introduction section.

<a id='research_question_1'></a>
### Research Question 1: Does a specific age period [age range] considered a factor for affecting the patient show up at the appointment, and which age range have the highest show up at the appointment.

1. > old adults have the highest percentage of showing up at the appointment 84.69% of showing up at the appointment <br>
2. > young adults have the highest percentage of not showing up at the appointment 24.65% of showing up at the appointment <br>

### Research Question 2: What is the day of the week when the highest number of patients show up for appointments, and which day of the week has the lowest number of patients showing up for appointments.

1. > Thursday has the highest percentage of patients showing up for appointments 80.65% <br>
2. > Saturday has the highest percentage of patients not showing up for appointments 23.08% <br>

### Research Question 3: What is the month when the highest number of patients show up for appointments, and which month has the lowest number of patients showing up for appointments.

1. > June has the highest percentage of patients showing up for appointments 81.54% <br>
2. > May has the highest percentage of patients not showing up for appointments 20.79% <br>


<a id='conclusions'></a>
## Conclusions
The following findings highlight the variations in appointment attendance based on age groups, weekdays, and months: <br>
> Older adults had the highest percentage (84.69%) of showing up for their appointments, while young adults had the highest percentage (24.65%) of not showing up.
> <br>Thursdays had the highest attendance rate (80.65%) among the weekdays, whereas Saturdays had the highest percentage (23.08%) of patients not showing up.
> <br>Additionally, the month of June had the highest attendance rate (81.54%), while May had the highest percentage (20.79%) of patients not showing up for their appointments. 