import wikipedia

def wiki_spi():
	
	info=raw_input("Enter the wiki page to be searched..")
	print wikipedia.summary(str(info))
wiki_spi()
