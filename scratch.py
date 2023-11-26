import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape data from a single page
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting data - Replace with your specific HTML structure
    # Example: extracting titles and prices from a hypothetical website
    titles = [title.text for title in soup.find_all('span', class_='style-scope')]
    duration = [duration.text for duration in soup.find_all('span', class_='style-scope')]
    thumbnail = [img['src'] for img in soup.find_all('img', class_='yt-core-image')]

    # Creating a dictionary to store the data
    data = {'Title': titles, 'Duration': duration, 'Thumbnail': thumbnail}
    return data

# Function to scrape multiple pages
def scrape_multiple_pages(base_url, num_pages):
    all_data = []

    for page_num in range(1, num_pages + 1):
        url = f"{base_url}?page={page_num}"
        data = scrape_page(url)
        all_data.append(data)

    return all_data

# Define the base URL and the number of pages to scrape
base_url = 'https://www.youtube.com/watch?v=VAdGW7QDJiU&list=PL4fGSI1pDJn4pTWyM3t61lOyZ6_4jcNOw'  # Replace with the target website
num_pages_to_scrape = 20  # Replace with the desired number of pages

# Scrape data from multiple pages
scraped_data = scrape_multiple_pages(base_url, num_pages_to_scrape)

# Convert the scraped data to a Pandas DataFrame
all_data_combined = {key: sum([d.get(key, []) for d in scraped_data], []) for key in scraped_data[0].keys()}
df = pd.DataFrame(all_data_combined)

# Save the data to an Excel file
output_file = 'scraped_data.xlsx'
df.to_excel(output_file, index=False)

print(f"Data scraped and saved to '{output_file}'")
