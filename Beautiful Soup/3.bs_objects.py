## In this we will be going over Beautiful Soup objects.
## Here lines started with '##' are comments and '#' are python statements.
## Do commenting and uncommenting as per requirements.

import requests
from bs4 import BeautifulSoup

## To keep things simple and also reproducible, consider the following HTML code
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""


## Store that html content of the index.html
# with open('index.html', 'w') as f:
#     f.write(html_doc)


soup =BeautifulSoup(html_doc, 'lxml')

## Print that html content in some good manner
print(soup.prettify())


##-------- Tag ---------#

## Finds the first occurrence of usage for a "b" bold tag.
print(soup.b)

## The "find" function also does the same, where it only finds the first occurrence in the HTML doc of a tag with "b".
print(soup.find('b'))

## To find all the elements into the content, find_all() method is used.
print(soup.find_all('b'))



##---------- Name --------#

## We can access the name of that tag with the soup.b.name.
# print(soup.b.name)

## We can alter the name of the tag also
# tag = soup.b
# print(tag)
# tag.name = 'em'
# print(tag)


##---------- Attributes ----------#

## Find specified by providing index value
# print(soup.find_all('b')[2])    # Will print 2nd <b> tag.

# tag = soup.find_all('b')[2]
## We can access tag's attributes like id, class etc.
# print(tag['id'])

## Let another element
# tag = soup.find_all('b')[3]
# print(tag)

## We can also access non-standard attributes also
# print(tag['another-attribute'])


## If we want to see all the attributes then we can do this too
# print(tag.attrs)    # Will get dictionary of all the attributes of this tag.

## All these values are mutable hence we can change these values as per own
# tag['another-attribute'] = 3
# print(tag['another-attribute'])

## We can also delete the attributes value by Python's del method
# print(tag.attrs) 
# del(tag['id'])
# del(tag['another-attribute'])

# print(tag.attrs)    # Will get empty dictionary, because we delete both the attribites.



##---------- String -----------#

## We can get all the content in string which is inbetween the start tag and end tag. <p>---string to be displayed---<p>
# tag = soup.find_all('b')[3]
# print(tag)
# print(tag.string)

## We can replace this string content by tag.string.replace_with('') method.
# tag.string.replace_with('This is replaced text')
# print(tag)