import requests as re
from bs4 import BeautifulSoup as bs

github_u = input("Input github username: ") #Collect username of Github User
url = 'https://github.com/' + github_u #Dynamic link
r = re.get(url) #request url

soup = bs(r.content, 'html.parser') #html source code or everything on that page
profile_image = soup.find('img', {'class': 'avatar'})['src'] #find a specific class with a specific tag with the image attached
print(profile_image)
