import requests
from bs4 import BeautifulSoup


def fetch_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Fail. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        return None

def extract_div_content(html_content, class_name):
    soup = BeautifulSoup(html_content, 'html.parser')
    divs_with_class = soup.find('div', class_ = class_name)
    if divs_with_class:
        return '\n'.join([div.get.text() for div in divs_with_class])
    else:
        print(f"NO Div with class '{class_name}' not found.")
        return None

def write_to_notepad(content):
    try:
        with open('companies list berlin connecticum.txt', 'w') as file:
            file.write(content)
        print("Content copied to notepad successfully.")
    except Exception as e:
        print(f"Error writing to notepad: {e}")


url = "https://www.connecticum.de/firmenprofile"
html_content = fetch_website(url)
if html_content:
    div_content = extract_div_content(html_content, 'vertical-tabs__content')
    if div_content:
        write_to_notepad(div_content)
    else:
        print("Failed to extract div content.")
else:
    print("Failed to fetch website content.")