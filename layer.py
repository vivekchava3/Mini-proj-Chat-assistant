from yowsup.layers.interface 							import YowInterfaceLayer, ProtocolEntityCallback 
from yowsup.layers.protocol_messages.protocolentities 				import TextMessageProtocolEntity 
from yowsup.layers.protocol_receipts.protocolentities 				import OutgoingReceiptProtocolEntity 
from yowsup.layers.protocol_acks.protocolentities 				import OutgoingAckProtocolEntity 
import requests 
from bs4 import BeautifulSoup
import os
import urllib2
import re
import wikipedia

class EchoLayer(YowInterfaceLayer):
	@ProtocolEntityCallback("message")
	def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over
		msg=messageProtocolEntity.getBody().lower()
		list=msg.split()
		print type(list)
		if True:
            		receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
                          
	    		if msg == 'weather' :
		  			url="http://www.accuweather.com/en/in/hyderabad/202190/daily-weather-forecast/202190"
					source_code=requests.get(url)
					plain=source_code.text
					soup=BeautifulSoup(plain,"html.parser")
					max_link=soup.find('span',{'class':'large-temp'})
					min_link=soup.find('span',{'class':'small-temp'})
					max_temp=max_link.string
					min_temp=min_link.string
					response="The temperature now is as follows:\n"+"Maximum Temperature is:"+max_temp+"\n Minimum Temp is:"+min_temp[1:]
	
			elif messageProtocolEntity.getBody().lower()=='score':
					url = "http://static.cricinfo.com/rss/livescores.xml"
					urll = "http://www.cricbuzz.com/cricket-match/live-scores"
					r=requests.get(url)
					soup=BeautifulSoup(r.text,"html.parser")
					data=soup.find_all("description")
					score=[]				
					for i in range(len(data)):	
						score.append(data[i].text)
					response="\n".join(score)
			elif list[0]=='caller':
					#try:
						APIToken = "uMf140ak94"  # PHPHive Truecaller API Token, Obtain it from https://tcapi.phphive.info/console/
    						no = list[1]
    					# Any Number You Want to Search
    						request_headers = {
        					"X-User": "PHPHive"
    							}
    					# For Searching User Details
    					#print "Searching for " + no
    						request = urllib2.Request("https://tcapi.phphive.info/" + APIToken + "/search/" + no, headers=request_headers)
    						contents = urllib2.urlopen(request).read()
    						num = re.sub(r'"*', "", contents)
    						#str2 ="name"
    						#str3="gender"
    						#str4="email"
    						#str5="facebook"
    						#i=num.index(str2)
    						#j=num.index(str3)
    						#k=num.index(str4)
    						#l=num.index(str5)
    						#name = num[i:j-1]
    						#name = name.title()
    						response=num
						#response=name+num[k:l-1]
					#except:
					#	response="Sorry.. No record found.."								
			elif list[0]=='info':
				try:
					i=1
					info=""
					while i<len(list):
						info+=list[i]
						i=i+1
					print info
					print type(info)
					response=wikipedia.summary(str(info))
					#response=res
				#info=list[1]
				#response=wikipedia.summary(str(info))
				except:
					response="There are many pages related to your query.\nPlease be more specific.\n Thank You"

			else :
 				response="Hello! To get accurate responses type any one of the following:\n"+"Type score to get the latest cricket scores..\n"+"Type weather to know the temperatures now..\n"+"Type info as (Ex:info string) to get information about that string\n"+"Type caller as (Ex:caller number) to get unknown caller identity\n"+"Thank You!"       
				#response = "Type 1:Score to get latest cricket scores\n2:weather to get the maximum and minimum temperatures\n3:wiki to get whatever you want to search for\n4:caller to get details of caller"
           	        outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                        response,
                        to = messageProtocolEntity.getFrom())

           	self.toLower(receipt)
          	self.toLower(outgoingMessageProtocolEntity)

		
		


	@ProtocolEntityCallback("receipt")
	def onReceipt(self, entity):
		ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
		self.toLower(ack)
    
    #@ProtocolEntityCallback("msg")
#	def onTextMessage(self,messageProtocolEntity):
#		receipt=OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(),messageProtocolEntity.getFrom(),'read',messageProtocolEntity.getParticipant())		
#		if messageProtocolEntity.getBody().lower()==message.lower():
#			r = requests.get(url)
#			soup = BeautifulSoup(r.text)
#			data = soup.find_all("description")
#			score=[]
#			for i in range(len(data)):
#				score.append(data[i].text)
#			response="".join(score)
#		else:
#			response="Please type score to get response"
#		outgoingMessageProtocolEntity=TextMessageProtocolEntity(response,to=messageProtocolEntity.getFrom())
#		self.toLower(receipt)
#		self.toLower(outgoingMessageProtocolEntity)
   #@ProtocolEntityCallback("receipt")
   #def onReceipt1(self,entity):
#	ack=OutgoingAckProtocolEntity(entity.getId(),"receipt1",entity.gettype(),entity.getFrom())
#	self.toLower(ack)


   
