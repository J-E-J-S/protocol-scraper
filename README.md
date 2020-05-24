Protocol Scraper  
=======================

This is a web scraper using the [Protocols.io API](https://apidoc.protocols.io/) to automate protocol collection and writing.  
 
 Manual
 -------

 **Pre-requisites:** 
 * Python 3 (Tested on 3.8.3)
 * Python requests package 
 * Windows (May work cross-platform but not tested)


* To install Python, see these [instructions](https://realpython.com/installing-python/)
* To install the requests package you need to have pip installed, see these [instructions](https://pip.pypa.io/en/stable/installing/)
	* then in terminal type: pip install requests
	* if on Windows you may have to type: python -m pip install requests 

**Steps:**
1. Type the name of the protocol you want between the '' after the search_for_protocol variable 
``` 
search_for_protocol = 'Type protocol here'
```
2. Run the script in an IDE or from the terminal 
 	* First navigate to the directory storing the ProtocolScraper.py script, then type 
``` 
python ProtocolScraper.py 
``` 
3. The script will generate 3 text files. Find the one with the best written protocol and stylise as desired. 
	* If some information is missing, following the url at the bottom of the file to see if you can fill in the details

Note: There is currently a codec error in translating some scientific symbols - see at bottom of generated file to fill these in. 