from yowsup.layers.interface 						import YowInterfaceLayer, ProtocolEntityCallback 
from yowsup.layers.protocol_messages.protocolentities 			import TextMessageProtocolEntity 
from yowsup.layers.protocol_receipts.protocolentities 			import OutgoingReceiptProtocolEntity 
from yowsup.layers.protocol_acks.protocolentities 			import OutgoingAckProtocolEntity 
import requests 
from bs4 import BeautifulSoup
import os

message="weather"
class EchoLayer(YowInterfaceLayer):
	@ProtocolEntityCallback("message")
	def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

		if True:
            		receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(),
				  'read', messageProtocolEntity.getParticipant())
                          
	    		if messageProtocolEntity.getBody().lower() == message.lower() :
				url="http://www.accuweather.com/en/in/Hyderabad/202190/daily-weather-forecast/202190"
				source_code=requests.get(url)
				plain_text=source_code.text
				soup=BeautifulSoup(plain_text,"html.parser")
				max_link=soup.find('span',{'class':'large-temp'})
				min_link=soup.find('span',{'class':"small-temp"})
				max_temp=max_link.string
				min_temp=min_link.string
				response="Maximum temperature is:"+max_temp+"\n Minimum temperature is:"+min_temp			
			else :
          		     response = "Please type weather to get Response"
           	        outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                        response,
                        to = messageProtocolEntity.getFrom())
		self.toLower(receipt)
          	self.toLower(outgoingMessageProtocolEntity)

		
	@ProtocolEntityCallback("receipt")
	def onReceipt(self, entity):
		ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
		self.toLower(ack)
   
