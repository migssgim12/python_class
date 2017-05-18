from bs4 import BeautifulSoup
import requests
import os

def compile_links():
    base_url = "https://or.water.usgs.gov/precip/"
# BASE_URL = 'https://or.water.usgs.gov/precip/hayden_island.rain'
    response = requests.get(base_url) # Sends an HTTP request over the interwebs
    raw = response.text   # Getting the raw HTML as a string
    soup = BeautifulSoup(raw, 'html.parser') # Making a BS4 soup objects

    rengas = [os.path.join(base_url, link['href']) for link in soup.find_all('a') if '.rain' in link['href']]
    return rengas



class RainStation:
    def __init__(self, url: str):
        self.url = url
        self.raw_text = self.scrape_station()
        name, address = self.parse_header()
        self.name = name
        self.address = address
        #         self.url = url


        self.rain_data = list()

        self.scrape_station()

def run_links(self):
    links = compile_links()
    rain_stations = list()
    failed_links = list()
    counter= 0

    for link in links:
        try:
            rs = Rainstation(url=link)
        except ValueError:
            failed_links.append(link)
            print('failed links # ')
        else:
            rain_stations.append(rs)
            print(f'build station {counter}')
        finally:
            counter += 1

big_ol_list = [rs.max_day() for rs in rain_stations ]


    def scrape_station(self):
        response = requests.get(self.url)
        raw_text = response.text
        return raw_text

    #         soup = BeautifulSoup(response.text, 'html.parser')

    def parse_header(self):
        name, address = data.splitlines()[0].split(' - ')
        return name, address

    def __repr__(self):
        message = "RainStation(name={}, address={}, url={})".format(self.name, self.address, self.url)
        return message

    def __str__(self):
        message = 'This is the station name:{}, {}'.format(self.name, self.address)
        return message

if __name == '__main__':
    run_links()