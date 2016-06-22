import csv, mechanize, urllib2
from bs4 import BeautifulSoup

output = open('output.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser()
br.open('http://www.dnr.state.mn.us/safety/boatwater/statistics.html')
#print br.response().read() 

#get HTML so I can target the table via its HTML tags
html = br.response().read()
# #transform HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")
#print soup

br.select_form(nr=0) #nr=0 to get the first (only) form on the page

table = soup.find('table', 
    {'class': 'altrowstable data',
    'id': 'alternatecolor'})
#print table

#extract info from table cells
for row in table.find_all('tr'):
        data = [cell.text.encode('utf-8') for cell in row.find_all('p')]
        print data

        #writer.writerow(data)
