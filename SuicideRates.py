
# To import packages pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# LINE PLOT
"""
Created a line plot.
Graph is plotted for suicide rates of different countries over sone years.
A datasource is chosen and file path for the datasource is provided to read the file.

X axis is labelled as Years and Y axis is labelled as suicide rates.

Function will first read the file, select the specific countries and will produce a line graph for those countries.
Total suicide rate of male and females are taken.
Seperate lines are created to indicate different countries.
Label for x and y axis is provided. Legend is provided. 
It will provide a comparitive analysis of how suicide rates are getting changed in different countries over vsome period

"""
# To define a function


def Lineplot(SuicideRates):

    # To read the data source file
    Suicide_data = pd.read_csv(SuicideRates)

    # To select countries from the data source
    countries = ['Argentina', 'United Kingdom',
                 'United States', 'Japan', 'Finland', 'Georgia']

    # To select corresponding data for the selected countries
    data_selected = Suicide_data[Suicide_data['country'].isin(countries)]

    # To add suicide_rate of both males and females
    grouped_data = data_selected.groupby(['year', 'country'])[
        'suicide_rate'].sum().reset_index()

    # To plot the data in graph
    plt.figure(figsize=(10, 6))

    for country in countries:
        country_data = grouped_data[grouped_data['country'] == country]

        # Code to plot line graph
        plt.plot(country_data['year'],
                 country_data['suicide_rate'], label=country)

    # To give a title for the graph
    plt.title('Suicide Rates Over Time')

    # To label X axis and Y axis
    plt.xlabel('Years')
    plt.ylabel('Suicide Rates')

    # To display legend and grid
    plt.legend()
    plt.grid(True)

    # To display the graph
    plt.show()


# To plot the graph
Lineplot('SuicideRates.csv')

# PIE CHART
"""
Created a Pie chart.
Chart is plotted for suicide rates of female in the year 2015 of some countries.

The function will first read the file, select the specific countries for the year 2015. 
Then it filters the suicide rate for female.
Then creates a pie chart for the data.

"""
# To define a function


def Piechart(SuicideRates, year=2015):

    # To read the data source file
    Suicide_data = pd.read_csv(SuicideRates)

    # To select countries and year from the data source
    countries = ['Greece', 'Poland',
                 'Netherlands', 'Latvia', 'Malta', 'Brazil']
    data_selected = Suicide_data[(Suicide_data['country'].isin(
        countries)) & (Suicide_data['year'] == year)]

    # To filter data for female
    Female_data = data_selected[data_selected['sex'] == 'female']

    # To plot the data in chart
    plt.figure(figsize=(8, 8))

    # Code to plot pie chart
    plt.pie(Female_data['suicide_rate'],
            labels=Female_data['country'], startangle=140)

    # To give a title for the chart
    plt.title(f'Suicide Rates of female ({year})')

    # To display the chart
    plt.show()


# To plot the chart
Piechart('SuicideRates.csv')


# BAR CHART
"""
Created a Bar chart.
Chart is marked for suicide rate of both males and females from 2000 to 2015.

Years is marked along X axis and Suicide rates is marked along Y axis.

Function reads the data scource file. Get the values of denmark for both males and females. 
Plot a stacked bar chart , which helps to get a proper visualisation of 
how males and females rate differ in each year.

"""
# To define a function


def Barchart(SuicideRates):

    # To read the data source file
    Suicide_data = pd.read_csv(SuicideRates)

    # To filter data for the Denmark
    Denmark_data = Suicide_data[Suicide_data['country'] == 'Denmark']

    # To pivot the data for stacked bar chart
    stacked_data = Denmark_data.pivot(
        index='year', columns='sex', values='suicide_rate')

    # Plot the stacked bar chart with male and female rates stacked in a single bar
    stacked_data.plot(kind='bar', stacked=True, figsize=(10, 6), width=0.8)

    # To give a title for the chart
    plt.title('Stacked Bar Graph of Male and Female Suicide Rates in Denmark')

    # To label X axis and Y axis
    plt.xlabel('Years')
    plt.ylabel('Suicide Rates')

    # To display legend
    plt.legend(title='Sex', loc='upper right')

    # To display the chart
    plt.show()


# To plot the chart
Barchart('SuicideRates.csv')
