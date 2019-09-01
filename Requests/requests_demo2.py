# In this, we will refer the site 'https://httpbin.org' for practicing and more documentations.
# This file contains 4 parts GET, POST, AUTH and Dynamic Data. Do commenting and uncommenting as per requirement.

import requests



#-------- HTTP GET request --------#

payload = {'page':2, 'count':25}    # Dictionary of all parameters into the URL

x = requests.get('https://httpbin.org/get', params=payload)

print(x.url)    # Will print the whole URL

print(x.text)   # Will print information regarding URL and our request



# #------- HTTP POST request --------#
# This help us to post data on the server.

# payload = {'name' : 'Jimmy', 'password' : 'jimmy123'}   # Dictionary of data to be post

# x = requests.post('https://httpbin.org/post', data = payload)

# # print(x.text)   # Will print information regarding our request and URL

# # print(x.json())    # Will print dictionary of a JSON response 

# json_dict = x.json()    # Will store the whole dictionary later we can access that.
# print(json_dict['form'])    # Will print the form data from the json response. Can access any from the dictionary.




# #--------- AUTH Method ---------#

# # This will Prompts the user for authorization using HTTP Basic Auth and then apply username and password for the authorization.0
# # We will get output as json(Dictionary), if user/request is authorized.
# # We will not get any output for an unauthorized user/request.
# # With this we can check authorization from the Python auth request only.

# a = requests.get('https://httpbin.org/basic-auth/Jimmy/jimmy123', auth = ('Jimmy', 'jimmy123'))  # Will apply username and password for the authorization.

# print(a.text)   # Print the details of authorization, which give output of dictionary if user is authorized otherwise will not give output at all.

# # Check for authorization with the status-code
# # We Will get code 200 if 'success' which indicate this request is authorized 
# # Or we will get 401 for 'Unauthorized response code' which indicate this request is unauthorised

# print(a)    # Will give you [200] code which indicates authorized.

# a = requests.get('https://httpbin.org/basic-auth/Kevin/kevin123', auth = ('Kevin', 'kevin'))    # Which have wrong password hence, authorization shold have to be failed.

# print(a)   # Will give [401], which indicates authorization is failed.




# #---------- Dynamic Data ----------#

# # In this we will use 'timeout' parameter which uses for specifing time in which if we will not response of our request then it will give you exceotion.
# # Some sites may appy delay to respond the requests

# # First apply URL which have delay of 2 seconds and timeout 3 second hence will will get response successfully.

# d = requests.get('https://httpbin.org/delay/2', timeout=3)

# print(d)    # Will give code [200] which indicates success.
# print(d.text)   # Will print data of the response

# # Here we set delay of 6 sec and timeout of 3 sec. Hence it will raise exception
# d = requests.get('https://httpbin.org/delay/6', timeout=3)  # Will raise ReadTimeout exception, which indicate we don't get response of our request in the tieout time.
# print(d)