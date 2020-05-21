import requests
import json
import re
import sys
import codecs 
#print (jason['protocol']['title']) # access element in protocol by 


search_for_protocol = 'PCR'




def search_page(string):
	'''given search string will return jason format of the search page for that string'''

	base = 'https://www.protocols.io/api/v3/protocols' # http request base 
	payload = {'filter': 'public', "order_field" : 'relevance', "key" : string} # api parameters : https://apidoc.protocols.io/#get-list

	r = requests.get(base, params=payload) # requests page information 
	jason = r.json() # page as json format 
	
	
	return jason 


def protocol_ids(jason):
	''' given json of search page, will return list of ids in descending order of releveancy '''
	ids = []

	for item in jason['items']: # this format because dictionary into list 
		ids.append(item['id'])


	return ids


def get_protocols(ids):

	base = 'https://www.protocols.io/api/v3/protocols/'
	protocol_list = [] # holds jason of protocol objects for top 3 relevent protocols

	count = 0 
	while count < 3:
		
		number = str(ids[count]) # gets id from list and converts to string for search
		url = base + number # plugs id into url 
		r = requests.get(url) # request api 
		jason = r.json() # converts json 
		protocol_list.append(jason) 

		count += 1 

	return protocol_list


def single_translate(protocol):
	''' Takes a protocol object and returns list of steps as strings with title of protocol being first element''' 

	title = protocol['protocol']['title'] # title of protocol
	steps = protocol['protocol']['steps'] # steps object of protocol

	step_list = [title] # stores cleaned text with title of protocol being first item in list 
	for step in steps:
		step_description = step['components'][1]['source']['description'] # navigates JSON to description which holds html of step text 
		cleanr = re.compile('<.*?>')
		clean_text = re.sub(cleanr, '', step_description) # removes html syntax from step text 
		step_list.append(clean_text) 


	count = 1
	while count < len(step_list):
		step_list[count] = str(count) + '. ' + step_list[count] # adds step number to description but not to title 
		count += 1 



	return step_list


def write_protocols(protocol_list):

	count = 0 
	while count < len(protocol_list): 
		
		translation = single_translate(protocol_list[count]) # translates protocol object into plain text steps (see single_translate function) + remove spaces

		title = translation[0].replace(' ', '_') # first element in single_translation list is always title 

		f = open(str(count)+ '_' + title + '.txt', 'w') # creates file with unique name 
		
		for step in translation:
			 
			 step = step.encode('cp1252', 'replace').decode('cp1252') # this fixes bug that brings up UnicodeEncodeError for greek/roman symbol 
			 f.write(step + '\n') # writes out steps to file

		f.close()

		count += 1


def main():

	jason = search_page(search_for_protocol)
	ids = protocol_ids(jason)
	protocol_list = get_protocols(ids)
	write_protocols(protocol_list)

	

main()

 