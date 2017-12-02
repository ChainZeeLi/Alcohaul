import urllib2
from bs4 import BeautifulSoup
import pandas as pd

import urllib

#specify the url
beerAle = "https://github.com/himanmaaraj/svgr/blob/0f65f04d02bd72cd8df0d1525695d3661c2ff49a/index.php"


#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(beerAle)

soup = BeautifulSoup(page, "html.parser")
#all_tables=soup.find_all('section')

print soup

right_table=soup.find('section', class_='section-body list-view ')


Name = ""
Price = 0

for row in right_table.find_all('li') :
	for data in row.find_all('p'):
	#	print data.string.strip()
		if str(data).count('$')==0:
			Name = data.string.strip()
			print Name

		print "a = alcohol(name = "+'"'+Name+'"'+ ", price = "+",quantity="+ "100" +   ")"
		print "a.save()"


	
