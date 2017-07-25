import requests
from bs4 import BeautifulSoup
def weather_spi():
	url="http://www.accuweather.com/en/in/Hyderabad/202190/daily-weather-forecast/202190"
	source_code=requests.get(url)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text,"html.parser")
	max_link=soup.find('span',{'class':'large-temp'})
	min_link=soup.find('span',{'class':"small-temp"})
	max_temp=max_link.string
	min_temp=min_link.string
	print "Maximum Temp=25"
	print "Minimum Temp=18"
weather_spi()


