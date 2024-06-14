# Created by Ben Cohen as an act of war against boredom.

#these libraries are required for the program to function obviously
import geopandas as gpd
import matplotlib.pyplot as plt
import pycountry
from countryinfo import CountryInfo

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

def color_country(country_name):
    if country_name in world['name'].values:
        world['color'] = world['name'].map(lambda x: 'red' if x == country_name else 'white')
        ax = world.plot(column='color', figsize=(15, 10))

        country_info = CountryInfo(country_name)
        capital = country_info.capital()
        population = country_info.population()
        area = country_info.area()
        currencies = country_info.currencies()
        languages = country_info.languages()

        info = f"Country: {country_name}\nCapital: {capital}\nPopulation: {population}\nArea: {area} sq km\nCurrency: {currencies}\nLanguages: {', '.join(languages)}"

        centroid = world.loc[world['name'] == country_name, 'geometry'].centroid.values[0]

        x_offset = 10
        y_offset = 10

        plt.annotate(info, (centroid.x + x_offset, centroid.y + y_offset), color='black',
                     bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="black", lw=2))

        plt.show()
    else:
        print("Country not found. Please try again.")


while True:
    country = input("Enter a country name (or 'exit' to quit): ")
    if country.lower() == 'exit':
        break
    color_country(country)
