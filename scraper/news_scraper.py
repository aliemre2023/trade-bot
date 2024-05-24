from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path

from datetime import datetime

import os


f = open("scraper/data/content.txt", "r")

def anchor_finder():   
    soup = BeautifulSoup(f.read(), 'html.parser')

    div_list = soup.find('div', class_="list-iTt_Zp4a")

    anchor_tags = div_list.find_all('a')

    href_list = list()
    for anchor in anchor_tags:
        href_list.append("https://tr.tradingview.com" + anchor["href"])
    f.seek(0)
    return href_list


href_list = anchor_finder()

message = """***
Yasal Uyarı

Burada yer alan yatırım bilgi, yorum ve tavsiyeler yatırım danışmanlığı kapsamında değildir.Yatırım danışmanlığı hizmeti ; aracı kurumlar, portföy yönetim şirketleri, mevduat kabul etmeyen bankalar ile müşteri arasında imzalanacak yatırım danışmanlığı sözleşmesi çerçevesinde sunulmaktadır.Burada yer alan yorum ve tavsiyeler, yorum ve tavsiyede bulunanların kişisel görüşlerine dayanmaktadır.Bu görüşler mali durumunuz ile risk ve getiri tercihlerinize uygun olmayabılır.Bu nedenle, sadece burada yer alan bilgilere dayanılarak yatırım kararı verilmesi beklentilerinize uygun sonuçlar doğurmayabilir."""

def content_extractor(anchor_list):
    service = Service(binary_path)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    for link in anchor_list:
        #print(link)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get(link)
        driver.implicitly_wait(1)

        
        try:
            """
            Elements depends on website, it may be change in time, need to be controlled
            """
            title = driver.find_element(By.CLASS_NAME, "title-KX2tCBZq").text
            content = driver.find_element(By.XPATH, "//div[@class='body-KX2tCBZq body-pIO_GYwT content-pIO_GYwT body-RYg5Gq3E']").text

            content = title + "\n" + content

            time = driver.find_element(By.CSS_SELECTOR, "time").get_attribute("datetime")
            dt_object = datetime.strptime(time, "%a, %d %b %Y %H:%M:%S %Z")
            day = str(dt_object.day).zfill(2)
            month = str(dt_object.month).zfill(2)
            year = str(dt_object.year).zfill(4)
            date_file_name = f"{year}.{month}.{day}"
        

            if message in content:
                content = content.replace(message, "")
            content += "\n"
            content += "_" * 50
            content += "\n" 

                 
            start_mark = "www."
            end_mart = ".com"
            start_idx = content.find(start_mark) + len(start_mark)
            end_idx = content.find(end_mart)

            news_distributor = ""
            for i in range(start_idx, end_idx):
                news_distributor += content[i]
            
            if news_distributor == "" or len(news_distributor) > 15:
                news_distributor = "undetermined"
            

            directory_path = f"scraper/news/{date_file_name}"
            os.makedirs(directory_path, exist_ok=True)

            distributor = open(f"scraper/news/{date_file_name}/{news_distributor}.txt", "a+")
            distributor.seek(0)
            if content in distributor.read():
                print("Haber zaten çekilmiş.")
            else:
                distributor.write(content)
                print("Haber çekildi.")


        except NoSuchElementException:
            print("Haber çekilemedi.")

        driver.quit()

content_extractor(href_list)