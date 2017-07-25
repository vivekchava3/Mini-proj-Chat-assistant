from yowsup.layers.interface 						import YowInterfaceLayer, ProtocolEntityCallback 
from yowsup.layers.protocol_messages.protocolentities 			import TextMessageProtocolEntity 
from yowsup.layers.protocol_receipts.protocolentities 			import OutgoingReceiptProtocolEntity 
from yowsup.layers.protocol_acks.protocolentities 			import OutgoingAckProtocolEntity 
import requests 
from bs4 import BeautifulSoup
import os

message="caller"
class EchoLayer(YowInterfaceLayer):
	@ProtocolEntityCallback("message")
	def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

		if True:
            		receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(),
				  'read', messageProtocolEntity.getParticipant())
                          
	    		if messageProtocolEntity.getBody().lower() == message.lower() :
			    APIToken = "uMf140ak94"  # PHPHive Truecaller API Token, Obtain it from https://tcapi.phphive.info/console/
    			    no = raw_input("Enter num to be searched")
       		            request_headers = {
        				"X-User": "PHPHive"
    					      }
			    request = urllib2.Request("https://tcapi.phphive.info/" + APIToken + "/search/" + no, headers=request_headers)
			    contents = urllib2.urlopen(request).read()
    			    num = re.sub(r'"*', "", contents)
			    response=num
    

			else :
          		     response = "Please type caller as (Ex:caller 100) to get Response"
           	        outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                        response,
                        to = messageProtocolEntity.getFrom())
		self.toLower(receipt)
          	self.toLower(outgoingMessageProtocolEntity)

		
	@ProtocolEntityCallback("receipt")
	def onReceipt(self, entity):
		ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
		self.toLower(ack)
   
