import pandas as pd
import matplotlib.pyplot as plt

try:
    url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
except:
    print("error occurred in retrieving Data")
file = pd.read_csv(url)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


def filter_data(country):
    # this method of filtering is for filtering according to column
    # print(file[file.ObservationDate == '05/03/2020'])
    # we have one more way to filter
    if sum(file["Country"].astype("str").str.contains(country)) > 0:
        df = (file[file['Country'].isin([country])])
        return df
    else:
        print("\nIncorrect country name\nplease run again")
        exit()


def country_list():
    first_letter = input("Enter the first letter of Country(CAPS): ")
    # countries = file.loc[:, file.columns.str.startswith(first_letter)]
    if sum(file["Country"].astype("str").str.startswith(first_letter)) > 0:
        df = file[file["Country"].astype("str").str.startswith(first_letter)].drop_duplicates(subset=["Country"])
        print(df)
    name_country = input("\n\nEnter your country name (First letter must be caps rest must be small eg: India): ")
    filtered_table = filter_data(name_country)
    plotting(filtered_table, name_country)


def plotting(dataFrame, name):
    ax = plt.gca()
    dataFrame.plot(kind='line', x='Date', y='Confirmed', color='red', ax=ax)
    dataFrame.plot(kind='line', x='Date', y='Deaths', color='blue', ax=ax)
    plt.title(name)

    plt.show()


if __name__ == '__main__':
    option = int(input("Welcome user\nThis is a very simple application"
                       " ,Here you can see how the corona virus has impacted various countries\n"
                       "So you can choose to either look at country based on first letter or enter the desired country\n"
                       "\n1 for see country listing\n2 for Entering country: "))
    if option == 1:
        country_list()
    elif option == 2:
        country_name = input("\n\nEnter your country name (First letter must be caps rest must be small eg: India): ")
        table = filter_data(country_name)
        plotting(table, country_name)

