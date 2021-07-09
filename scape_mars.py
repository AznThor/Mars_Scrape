#!/usr/bin/env python
# coding: utf-8

# In[12]:


get_ipython().system('pip install splinter')
get_ipython().system('pip install webdriver-manager')


# In[21]:


import pandas as pd
import requests
from splinter import Browser
from bs4 import BeautifulSoup as beautifulsoup
from webdriver_manager.chrome import ChromeDriverManager


# In[22]:


#Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[24]:


# VISIT URL WEBpage 
url = "https://redplanetscience.com/"
browser.visit(url)
html = browser.html
soup = beautifulsoup(html, 'html.parser')


# In[25]:


soup.find("div", class_="list_text")


# In[26]:


Date = soup.find("div", class_="list_text").find("div", class_="list_date").text
Titles = soup.find("div", class_="list_text").find("div", class_="content_title").text
Teaser = soup.find("div", class_="list_text").find("div", class_="article_teaser_body").text


# In[27]:


print(Date)
print(Titles)
print(Teaser)


# In[38]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
#Webpage
Marsurl = "https://spaceimages-mars.com/"
browser.visit(Marsurl)

# Turn into soup
html = browser.html
soup = beautifulsoup(html, "html.parser")


Mars_URL_Feature = url + soup.find("img", class_="headerimage fade-in")["src"]

print(Mars_URL_Feature)


# In[40]:


mars_facts = 'https://space-facts.com/mars/'


# In[41]:


table = pd.read_html(mars_facts)
mars_facts_dataframe = table[0]
mars_facts_dataframe


# In[42]:


mars_table_html = mars_facts_dataframe.to_html(header=None)

mars_table_html


# In[43]:


hemisphereurl = "https://marshemispheres.com/"
browser.visit(hemisphereurl)

html = browser.html
soup = beautifulsoup(html, "html.parser")


# In[61]:


# div with image links
hemisphere_descriptions = soup.find_all("div", class_='description')

hemisphere_img_urls = []

# loop through divs to get title and link to full-size images
for i in hemisphere_descriptions:
    
    title = i.find('h3').text
    
    part_image_href = i.find('a', class_='itemLink product-item')['href']
    
    browser.visit(hemisphereurl + part_image_href)
    
    part_html = browser.html
    
    soup_par = beautifulsoup(part_html, 'html.parser')
    
    picture_url = hemisphereurl + soup_par.find('img', class_='wide-image')['src']
    
    hemisphere_img_urls.append({"title": title, "img_url": picture_url})


# In[62]:


hemisphere_img_urls


# In[ ]:




