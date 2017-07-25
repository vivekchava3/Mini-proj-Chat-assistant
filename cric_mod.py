from yowsup.layers.interface 						import YowInterfaceLayer, ProtocolEntityCallback 
from yowsup.layers.protocol_messages.protocolentities 			import TextMessageProtocolEntity 
from yowsup.layers.protocol_receipts.protocolentities 			import OutgoingReceiptProtocolEntity 
from yowsup.layers.protocol_acks.protocolentities 			import OutgoingAckProtocolEntity 
import requests 
from bs4 import BeautifulSoup
import os

message="score"
class EchoLayer(YowInterfaceLayer):
	@ProtocolEntityCallback("message")
	def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

		if True:
            		receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(),
				  'read', messageProtocolEntity.getParticipant())
                          
	    		if messageProtocolEntity.getBody().lower() == message.lower() :
				url = "http://static.cricinfo.com/rss/livescores.xml"
				r = requests.get(url)
				soup = BeautifulSoup(r.text)
				data = soup.find_all("description")
				score=[]
				res=""
				for i in range(len(data)):
					score.append(data[i].text)
				response="".join(score)
			else :
          		     response = "Please type Score to get Response"
           	        outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                        response,
                        to = messageProtocolEntity.getFrom())
		self.toLower(receipt)
          	self.toLower(outgoingMessageProtocolEntity)

		
	@ProtocolEntityCallback("receipt")
	def onReceipt(self, entity):
		ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
		self.toLower(ack)
   
