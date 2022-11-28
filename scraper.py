from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# Enlace a NASA Exoplanet
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Controlador web
options = webdriver.EdgeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging']) 
browser = webdriver.Edge(options=options)
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Definir el método de extracción de datos para Exoplanet
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## AGREGAR EL CÓDIGO AQUÍ ##
        soup = BeautifulSoup(browser.page_source,"html.parser")

        for ul in soup.find_all("ul", attrs = {"class", "exoplanet"}):
            li_url = ul.find_all("li")

            planet_list = []

            for index, li_tag in enumerate(li_url):
                if index == 0 :
                    planet_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        planet_list.append(li_tag.contents[0])
                    except:
                        planet_list.append("")
            planets_data.append(planet_list)

        browser.find_element(by = By.XPATH, value = '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()         
    
    


        
# Llamada del método
scrape()

# Definir los encabezados
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Definir el dataframe de Pandas
dataFramePlanet = pd.DataFrame(planets_data, columns = headers)

# Convertir a CSV
dataFramePlanet.to_csv("Planets_Data.csv", index = True, index_label = "id")

    


