from wit import Wit

access_token = "KG7AUFYAF6W5PTB7KBZ5CQVH32O24UIG"

client = Wit(access_token = access_token)

def wit_response(message_text):
	resp = client.message(message_text)
	
	entity_list = []
	intent = None

	try:
		for entity in resp['entities']:
			value = resp['entities'][entity][0]['value']['value']
			entity_list.append((entity, value))
		intent = resp['intent']['value']['value']
	except:
		pass
		
	return entity_list, intent