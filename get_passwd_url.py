# @Author: S. Sharma <silentcat>
# @Date:   2019-01-28T13:36:54-06:00
# @Email:  silentcat@protonmail.com
# @Last modified by:   silentcat
# @Last modified time: 2019-01-28T13:48:31-06:00

from bs4 import BeautifulSoup

contents = None
with open('index.html') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')
images = soup.find_all('img')
for image in images:
    if 'password' in image.get('src'):
        print(image.get('src'))
        break
