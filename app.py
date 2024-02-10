import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'https://www.startupindia.gov.in/content/sih/en/search.html?states=5f48ce592a9bb065cdf9fb3c&stages=scaling&roles=Startup&page=1'

try:
    # Send an HTTP GET request to the website
    response = requests.get(url)
    print("here")
    # Check if the request was successful (status code 200)
    response.raise_for_status()

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
 # Save the soup object to a text file
    with open('soup.txt', 'w', encoding='utf-8') as file:
        file.write(str(soup))    # Use BeautifulSoup to extract company names and website links
    company_list = []
    for company in soup.find_all('div', class_='company'):
        name = company.find('span', class_='company-name').text
        website = company.find('a', class_='company-website')['href']
        company_list.append((name, website))

    # Print the collected data
    for name, website in company_list:
        print(f'Company: {name}')
        print(f'Website: {website}')
except requests.exceptions.RequestException as e:
    print(f'Failed to retrieve the page. Error: {e}')
except Exception as e:
    print(f'An error occurred: {e}')
