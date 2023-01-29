import requests
import csv

r = requests.get("https://newsapi.org/v2/everything?q=apple&from=2023-01-28&to=2023-01-28&sortBy=popularity&apiKey=551fde63a636435c990650ae795d9bdb")


def get_news(country, file_name, api_key=''):         
    url =   f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    fileName = file_name
    with open(f'{fileName}.csv', 'w') as f:
        writer = csv.writer(f)
        articleNo = 0
        for article in articles:
            articleNo += 1
            writer.writerow([f'ARTICLE : {articleNo}'])
            writer.writerow(['\nTITLE: \n', article['title'], '\nDESCRIPTION : \n', article['description']])
            writer.writerow("\n")


def main():

    print("""Choose between the following countries: \n fr = France \n gb = United Kingdom \n in = India \n nz = New Zealand \n us = United States of America \n ca = Canada \n or enter the 2-letter ISO 3166-1 code of the country you want to get headlines for (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)""")
    response = input('--> ')
    file_nomenclature = input('What would you like to name the CSV file? --> ')
    get_news(response, file_nomenclature)
    print('A CSV File has been made in the current directory')


main()
