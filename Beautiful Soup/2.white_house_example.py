## In this we take site "https://www.whitehouse.gov/briefings-statements/" for the practicing.
## Goal is to extract all the links on the page of briefing and statements.

from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.whitehouse.gov/briefings-statements/")

## Check page is accessible or not. Will get [200] for accessible.
print(res.status_code)

## Assign all content of the page to the src
src = res.content

## Create object of the bs4 to parse into the source or content of the link
soup = BeautifulSoup(src, 'lxml')

## Create empty list of all URLs. Later we will append urls in it.
url = []    

## Let count the links we extracted
count = 0
## See the link page, in that all the <a> tags are inside the <h2> tag.(You can do that by after going to that page then right click of the element and go to the inspect elements.)
## Hence first we find <h2> tags and then into the <h2> tags we will find <a> tags.
for h2_tag in soup.find_all("h2"):
    a_tag= h2_tag.find("a")  # Will find one <a> tag into every <h2> tag.
    url.append(a_tag.attrs['href'])     # Will append only links/urls to the url list.
    count +=1

## Print all the urls
print(url)  
#Print the no of links we extracted.
print(count)