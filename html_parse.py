import requests
from bs4 import BeautifulSoup
html = '''<a href="some_url">next</a>
<span class="class"><a href="another_url">later</a></span>'''
response = requests.get('https://github.com/trending/python?since=daily')
html_data = response.text
soup=BeautifulSoup(html_data,'html.parser')
j=0
urls=[]
for h in soup.find_all('h1'):
    if j==0:
    	j=j+1
    	continue
    
    a1 = h.find('a')
    urls.append(a1.attrs['href'])
    j=j+1
    if j==11:
    	break
for x in urls:
	print(x)