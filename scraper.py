from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("C:\Users\Natalie\Downloads\chromedriver_win32")
browser.get(START_URL)
scraped_data = []

#Define data scrapping method
def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    
    bright_star_table = soup.find("table", attrs={"class", "wikitable"})
        
    #Find <tbody>
    table_body = bright_star_table.find('tbody')

    #Find <tr>
    table_rows = table_body.find_all('tr')

    #Get data from <td>
    for row in table_rows:
            table_cols = row.find_all('td')
            print(table_cols)
            
            temp_list = []

            for col_data in table_cols:
                #Print Only columns textual data using ".text" property
                print(col_data.text)

                #Remove Extra white spaces using strip() method
                data = col_data.text.strip()
                print(data)

                temp_list.append(data)

            #Append data to star_data list
            scraped_data.append(temp_list)

#Calling Method    
scrape()

#Importing data to csv

stars_data = []


for i in range(0,len(scraped_data)):
    
    Star_names = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

print(stars_data)

headers = ['Star_name','Distance','Mass','Radius','Luminosity']  
   
star_df_1 = pd.DataFrame(stars_data, columns=headers)

star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")

