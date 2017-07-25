import requests
from bs4 import BeautifulSoup
def fun():
	url = "http://static.cricinfo.com/rss/livescores.xml"
	urll = "http://www.cricbuzz.com/cricket-match/live-scores"
	r = requests.get(url)
	soup = BeautifulSoup(r.text,"html.parser")
	data = soup.find_all("description")
	score=[]
	res=""
	for i in range(len(data)):
		score.append(data[i].text)
	res="\n".join(score)
	print res
fun()
