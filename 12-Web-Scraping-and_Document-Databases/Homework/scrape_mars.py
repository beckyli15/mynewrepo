#!/usr/bin/env python
# coding: utf-8



# Dependencies
from bs4 import BeautifulSoup
import pandas as pd
import requests
from splinter import Browser


def init_browser():
    executable_path={'executable_path':'./chromedriver.exe'}
    return Browser('chrome',**executable_path,headless=False)

mars_info={}
def scrape_mars_news():
    try:
        browser=init_browser()
        url='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
        browser.visit(url)
        html=browser.html


        # Create BeautifulSoup object; parse with 'html.parser'
        soup = BeautifulSoup(html, 'html.parser')

        #latest_title=soup.find('div',class_='image_and_description_container')
        latest_title=soup.find('div',class_='content_title').text
        latest_paragraph=soup.find('div', class_='article_teaser_body').text
    
        #dictionary
        mars_info['news_title']=latest_title
        mars_info['news_paragraph']=latest_paragraph
        return mars_info

    finally:
        browser.quit()



#JPL Mars Space Images - Featured Image
def scrape_img():
    try:
        browser=init_browser()
        url2=('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
        browser.visit(url2)
        html1=browser.html
        soup = BeautifulSoup(html1, 'html.parser')
        newurl=('http://www.jpl.nasa.gov')



        relative_image_path = soup.find_all('img')[3]["src"]
        featured_image_url = newurl + relative_image_path


        featured_image_url

        mars_info['featured_image_url']=featured_image_url
        return mars_info
    finally:
        browser.quit()

#Mars Weather
def scrape_weather():
    try:
        browser=init_browser()

        weatherurl=('https://twitter.com/marswxreport?lang=en')
        browser.visit(weatherurl)
        html2=browser.html
        soup2 = BeautifulSoup(html2, 'html.parser')

        mars_weather=soup2.find('div',class_='js-tweet-text-container').find('p').text
        mars_info['mars_weather']=mars_weather
        
        return mars_info
    finally:
        browser.quit()


#Mars Facts
def scrape_facts():

    factsurl='https://space-facts.com/mars/'
    tables = pd.read_html(factsurl)


    mars_fact=tables[1]
    mars_fact.columns=['Description','Value']
    mars_fact.set_index('Description',inplace=True)

    data=mars_fact.to_html()
    mars_info['mars_facts']=data

    return mars_info


#Mars Hemispheres
def scrape_hemisphere():
    try:
        browser=init_browser()
        hemispheresurl=('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
        browser.visit(hemispheresurl)
        html3=browser.html
        soup3 = BeautifulSoup(html3, 'html.parser')

        items = soup3.find_all('div', class_='item')
        hemisphere_image_urls = []
        hemispherehome=('https://astrogeology.usgs.gov')

        for i in items: 
            
            title = i.find('h3').text
            
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
            
            browser.visit(hemispherehome+ partial_img_url)
            
            partial_img_html = browser.html
            
            soup3 = BeautifulSoup( partial_img_html, 'html.parser')
            
            img_url_1=soup3.find('img', class_='wide-image')['src']
            img_url=hemispherehome+img_url_1
            hemisphere_image_urls.append({"title":title,"img_url":img_url})

        mars_info['hemisphere_img_url']=hemisphere_image_urls

        return mars_info
    finally:
        browser.quit()







