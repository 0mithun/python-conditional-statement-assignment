from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time
import csv

chrome_options = Options()
chrome_options.add_argument("--headless")


class Indiegogo:
    soup = ''
    links = []
    filter_links = []
    all_url = []
    url = ""
    
    def __init__(self, url, cities):
        self.url = url
        self.cities = cities

    def generate_url(self):
        for city in self.cities:
            url = self.url + "&q="+city+',%20US'
            self.all_url.append(url)

    def load_all_project(self, url):
        browser = webdriver.Chrome(chrome_options= chrome_options)
        browser.get(url)
        while(True):
            try:
                more = browser.find_element_by_xpath('//*[@class="i-cta-1 ng-binding ng-isolate-scope"]')
                time.sleep(3)
                more.click()
            except ElementNotVisibleException:
                break
        soup = BeautifulSoup(browser.page_source,'lxml')
        self.soup = soup 
        browser.close()


    def get_all_project_link(self):
        all_item = self.soup.find('div', class_="exploreDetail-campaigns")
        items = all_item.find_all('div', class_="discoverableCard")
        for single_item in items:
            link = single_item.find('a')['href']
            link = link.replace('/pies','#/')
            link = 'https://www.indiegogo.com'+ link
            if link not in self.links:
                self.links.append(link)

    def open_project_link(self, link):
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get(link)
        soup = BeautifulSoup(browser.page_source,'lxml')
        browser.quit()
        return soup

    def filter_all_project_link(self):
        for link in self.links:
            soup = self.open_project_link(link)
            if soup.find('div',class_='campaignTrust-detailsLocation'):
                location = soup.find('div',class_='campaignTrust-detailsLocation').text
                location = location.split(", ")[1].strip()
                if (location == 'United States'):
                    self.filter_links.append(link)

    def write_csv(self, file_name, data):
        with open(file_name, 'w') as f:
            fp = csv.writer(f)
            for line in data:
                fp.writerow([line])

    def print_links(self):
        for link in self.filter_links:
            print(link)

#cities = ['Alexander City','Anniston','Andalusia','Athens','Atmore','Auburn','Bessemer','Birmingham','Chickasaw','Clanton','Cullman','Decatur','Demopolis','Dothan','Enterprise','Eufaula','Florence','Fort Payne']
#cities = ['Gadsden','Greenville','Guntersville','Huntsville','Jasper','Marion','Mobile','Montgomery','Opelika','Ozark','Phenix City','Prichard','Scottsboro','Selma','Sheffield','Sylacauga','Talladega','Troy','Tuscaloosa','Tuscumbia','Tuskegee']
cities = ['Alexander City','Anniston','Andalusia']
url = "https://www.indiegogo.com/explore/home?project_type=campaign&project_timing=all&sort=trending"
ind = Indiegogo(url, cities)
ind.generate_url()
links = ind.all_url
for link in links:
    ind.load_all_project(link)
    ind.get_all_project_link()

#ind.write_csv('al.csv', ind.links)
ind.filter_all_project_link()
for link in ind.filter_links:
    print(link)




#ind.print_links()


