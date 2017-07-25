
import urllib2

import re
import requests
from bs4 import BeautifulSoup


def truecaller():
    APIToken = "uMf140ak94"  # PHPHive Truecaller API Token, Obtain it from https://tcapi.phphive.info/console/
    no = str(raw_input("Enter number to be searched"))
    # Any Number You Want to Search
    request_headers = {
        "X-User": "PHPHive"
    }
    # For Searching User Details
    print "Searching for " + no
    request = urllib2.Request("https://tcapi.phphive.info/" + APIToken + "/search/" + no, headers=request_headers)
    contents = urllib2.urlopen(request).read()
    num = re.sub(r'"*', "", contents)
    print num

	
	
truecaller()
