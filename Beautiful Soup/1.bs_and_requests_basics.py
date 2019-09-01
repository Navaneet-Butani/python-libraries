## Which lines contains '##' at starting, are the coments.
## Which lines contain '#' at starting are python commands, you have to uncomment as per the requirements.
## Take care of intatation while commenting and uncommenting.

import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.google.com")

print(res.status_code)    # Will print status code of response

## status code 200 : for 'OK'(success)
## status code 300 : for 'redirect'
## status code 400 : for 'client error' (If you try to access some pages which don't have access persmission to you.)
## status code 500 : for 'server error'


# print(res.headers)   # Will print header of that site.(make sure url site is accessible to you.)

src = res.content   # Get the whole content of the requested web page and stores in src.

# print(res.content)     # Will print whole content of the url.

## Create object of the bs4 to parse into the source or content of the link
soup = BeautifulSoup(src, 'lxml')   

## Let's get all the links from the content. Will get all the <a> tags from the URL page.
links = soup.find_all("a")

## Print all the links from the page.
# print(links)


## For finding specified link from the all links
## Let find linkes who have "About" in that link. 
## For the text between <a>text</a>, we have property ".text"
## For the link attributes, we have ".attrs". 
## Find specific "href" attributes' content with link.attrs["href"].
# for link in links:
#     if 'About' in link.text:
#         print(link)
#         print(link.attrs['href'])


## Like this you can parse all the information from any web page.
## You can use any tags like here we used <a> and grab information from that.
## Get the content of all attributes as well as any specific attributes.