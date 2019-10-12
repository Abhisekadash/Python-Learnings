import requests
import os
import pdb
import argparse
from bs4 import BeautifulSoup
# A function to choose the path
class HTMLParser:
	
	def choose(self):
	#To input Command Line argument
		parser = argparse.ArgumentParser(description='Process some Language.')
		parser.add_argument('-l', '--language', help='an Language any like java,python,ruby')
		args = parser.parse_args()
		site='https://github.com/trending/'+args.language+'?since=daily'
		response=requests.get(site)
		#convert response in form of text
		html_data=response.text
		return html_data

	#To find the string you want to find
	def find_text(self,html_data1):
		urls=[]
		#used to parse the html content
		soup=BeautifulSoup(html_data1,'html.parser')
		j=0
		# To find all 'h1' header in html_data
		#pdb.set_trace()
		for h in soup.find_all('h1'):
			if j==0:
				j+=1
				continue
			# After find heading tag, to find the a tag
			a1 = h.find('a')
			#print(a1)
			#apppend in list after convert it to text
			urls.append(a1.text)
			j=j+1
			if j==11:
				break
		#print(urls)
		return urls
	#This function to print in proper way
	def print_proper1(self,urls):
		url1=[]
		for x in urls:
			#if is there any white space strip() will delete it
			url1.append(x.strip())
		url2=[]
		l=[]
		for x in url1:
			#To print the proper text i want
			l=x.split("    ")
			url2.append(l[1])
		# Use of enumerate for counting the no. of text
		ob1=list(enumerate(url2,1))
		for x in ob1:
			#is use to split the tuple
			print(f"{x[0]} : {x[1]}")

ht=HTMLParser()
html_data=ht.choose()
list_of_text=ht.find_text(html_data)
#print(list_of_text)
ht.print_proper1(list_of_text)