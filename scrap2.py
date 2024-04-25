import requests
from bs4 import BeautifulSoup

def fetch_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch website: {url}. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        return None

def extract_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', attrs={'id': 'exhibitors'})
    results = []
    if table:
        divs = table.find_all('div', attrs = {'class': 'c_fo1 c_fs6 white name mb5'})
        for div in divs:
           title = div.get_text(strip=True)
           results.append(title)
    # rows = table.find('tr', id=lambda x: x and x.startswith('company'))
    # for row in rows:
    #     div = row.find('div', class_='c_fo1 c_fs6 white name mb5')
    #     if div:
    #         title = div.get('title')
    #         results.append(title)
    return results

def write_to_notepad(content):
    try:
        with open('companies list berlin connecticum.txt', 'w') as file:
                for con in content:
                    file.write("%s\n" % con)
        # print("Content copied to notepad successfully.")
    except Exception as e:
        print(f"Error writing to notepad: {e}")

# Example usage:
companies = []
for i in range(0,13):
    url1 = "https://www.connecticum.de/companysearchresult.php?&entries=100&page="
    url = url1+str(i)

    html_content = fetch_website(url)
    if html_content:
        data = extract_data(html_content)

        if data:

            for title in data:
                companies.append(title)
                print(title)
        else:
            print("No data extracted.")

    else:
        print("Failed to fetch website content.")
write_to_notepad(companies)
# print(extract_data(html_content))