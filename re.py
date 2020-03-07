#import regular expression.
import re

#open .csv file from folder.
with open('re.csv','r') as ip:
	re_file=ip.read()
# print the matching ip's.
print(re.findall(r'\d+.\d+.\d+.\d+',re_file))