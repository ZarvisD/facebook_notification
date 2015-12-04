import requests
import lxml

#user_id=raw_input("Please enter the facebook rss id ")
#password=raw_input("Please enter the facebook rss key ")
user_id='''Your RSS facebook id'''
password='''RSS key look in the facebook RSS notification's url for the key and id'''
url="https://www.facebook.com/feeds/notifications.php?id="+user_id+"&viewer=1543784655&key="+password+"&format=rss20"
r=requests.get(url,verify=False)
#print r.status_code
rss_data=r.content
#print rss_data
from bs4 import BeautifulSoup
soup=BeautifulSoup(rss_data,'html.parser')
titles= soup.find_all('title')
pubdat=soup.find_all('pubdate')
print len(pubdat)
del titles[0]
# for i in range(0,5):
# 	print 'no.'+str(i) + '  '+titles[i].text+pubdat[i].text
# for each_item in titles:
#  	try:
#  		print each_item.text
#  	except:
#  		print each_item

def messages1():
	data =''
	for i in range(0,5):
		data+='no.'+str(i) + '  '+titles[i].text+pubdat[i].text +'\n'
	return  data
import tiwlo
