# First of all you have to install this library with the 'pip install requests'.
# Do commenting and uncommenting as per requirement.

import requests

x = requests.get('https://xkcd.com/353/')

print(x)    # Will print object sent from server of link.

# print(dir(x))     # Will print attributes and methods in that object

# print(help(x))     # Will print detailed desciption of that object, methods and attributes

# print(x.text)   # Will print content of the image in bytes

# print(x.status_code)    # Will print status code of response

# # status code 200 : for 'success'
# # status code 300 : for 'redirect'
# # status code 400 : for 'client error' (If you try to access some pages which don't have access persmission to you.)
# # status code 500 : for 'server error'


# print(x.ok) # Will print 1)True : if 'status_code is < 400' (Which means there is no client or server error) 
#             #            2)False : if 'status_code is >=400' (Which means there is client or server error) 
#             # This type of work is done to see how our or other site is working at particular time      

# print(x.headers) # Will print all the header information like server, content-type, Last-modification etc. 




# # To download image from URL

# z = requests.get('https://imgs.xkcd.com/comics/python.png')  # Take only specific URL of that photo

# with open('Python-comic.png', 'wb') as f:   # Will create new file with write bytes permissions
#     f.write((z.content))
