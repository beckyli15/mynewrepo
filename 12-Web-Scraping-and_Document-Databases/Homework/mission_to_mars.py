#!/usr/bin/env python
# coding: utf-8

# In[60]:


# Dependencies
from bs4 import BeautifulSoup
import os
import pandas as pd
import requests
from splinter import Browser
import lxml.html as lh


# In[24]:


executable_path={'executable_path':'chromedriver.exe'}
browser=Browser('chrome',**executable_path,headless=False)


# In[5]:


url=('https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest')


# In[6]:


# Retrieve page with the requests module
browser.visit(url)
html=browser.html


# In[7]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')


# In[8]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[9]:


#latest_title=soup.find('div',class_='image_and_description_container')

latest_title=soup.find('div',class_='content_title').text
latest_paragraph=soup.find('div', class_='article_teaser_body')
print(latest_title)


# In[10]:


print(latest_paragraph.text)


# In[18]:


#JPL Mars Space Images - Featured Image
url2=('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
browser.visit(url2)
html1=browser.html
soup = BeautifulSoup(html1, 'html.parser')
newurl=('http://www.jpl.nasa.gov')


# In[19]:


relative_image_path = soup.find_all('img')[3]["src"]
featured_image_url = newurl + relative_image_path


# In[20]:


relative_image_path


# In[21]:


featured_image_url


# In[54]:


#Mars Weather
weatherurl=('https://twitter.com/marswxreport?lang=en')
browser.visit(weatherurl)
html2=browser.html
soup2 = BeautifulSoup(html2, 'html.parser')


# In[55]:


mars_weather=soup2.find('div',class_='js-tweet-text-container').find('p').text


# In[56]:


mars_weather


# In[64]:


#Mars Facts
factsurl='https://space-facts.com/mars/'
tables = pd.read_html(factsurl)


# In[70]:


mars_fact=tables[1]
mars_fact


# In[112]:


#Mars Hemispheres
hemispheresurl=('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
browser.visit(hemispheresurl)
html3=browser.html
soup3 = BeautifulSoup(html3, 'html.parser')


# In[136]:



items = soup3.find_all('div', class_='item')
hemisphere_image_urls = []
hemispherehome=('https://astrogeology.usgs.gov')

for i in items: 
    # Store title
    title = i.find('h3').text
    
    # Store link that leads to full image website
    partial_img_url = i.find('a', class_='itemLink product-item')['href']
    
    # Visit the link that contains the full image website 
    browser.visit(hemispherehome+ partial_img_url)
    
    # HTML Object of individual hemisphere information website 
    partial_img_html = browser.html
    
    # Parse HTML with Beautiful Soup for every individual hemisphere information website 
    soup3 = BeautifulSoup( partial_img_html, 'html.parser')
    
    img_url_1=soup3.find('img', class_='wide-image')['src']
    img_url=hemispherehome+img_url_1
    hemisphere_image_urls.append({"title":title,"img_url":img_url})


# In[137]:


title


# In[138]:


img_url


# In[139]:


hemisphere_image_urls


# In[ ]:





# In[93]:





# In[ ]:




