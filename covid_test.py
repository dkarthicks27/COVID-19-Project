# this is just a test case of covid-19
# let us first define the problem statement
# build an app that let's us visualise the corona effect
# that is whether the curve is increasing on flattening
# depending on the city
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
# file = pd.read_csv('/Users/karthickdurai/Downloads/novel-corona-virus-2019-dataset/covid_19_data.csv')
file = pd.read_csv(url)


def printing_tail_head():
    print(file.head())
    print(file.tail())


def get_summary():
    print(file.dtypes)
    print(file.index)
    print(file.columns)
    print(file.values)


def get_statistics():
    print(file.describe())


def sort_by_columns():
    print(file.sort_values('Recovered', ascending=False))


def slicing_rows_columns():
    print(file['Country/Region'])
    print(file['Deaths'])
    print()
    print(file.Recovered)
    print(file[2:20])
    print(file.loc[20000:21000, ['Country/Region', 'Province/State', 'Deaths', 'Recovered']])
    print(file.iloc[19000:19003, 1:5])


def filter_data(country):
    # this method of filtering is for filtering according to column
    # print(file[file.ObservationDate == '05/03/2020'])
    # we have one more way to filter
    df = (file[file['Country'].isin([country])])
              # .loc[:, ['SNo', 'ObservationDate', 'Province/State', 'Country/Region', 'Deaths', 'Confirmed']])
    return df


def assignment():
    file.loc[9, ['Country/Region']] = 'Mainland China'
    print(file.loc[9:11, ['Country/Region']])
    # print(np.array([5] * len(file)))


def rename_columns():
    file.rename(columns={'Country/Region': 'Country'}, inplace=True)
    # so yes name changed, this is for changing a particular column
    print(file.iloc[:, 2:5])
    # to change multiple columns at once, send it
    # file.columns = ['val1', 'val2', 'val3', ....]


# printing_tail_head()
# get_summary()
table = filter_data('India')
ax = plt.gca()
table.plot(kind='line', x='Date', y='Confirmed', color='red', ax=ax)
table.plot(kind='line', x='Date', y='Deaths', color='blue', ax=ax)
# table.plot(kind='line', x='ObservationDate', y='Confirmed', color='red', ax=ax)
# table.plot(kind='line', x='ObservationDate', y='Deaths', color='blue', ax=ax)

plt.show()
