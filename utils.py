from wit import Wit

access_token = "KG7AUFYAF6W5PTB7KBZ5CQVH32O24UIG"

client = Wit(access_token = access_token)

def wit_response(message_text):
	resp = client.message(message_text)['entities']
	
	entity_list = []
	intent = None

	try:
		for entity in resp:
			value = resp[entity][0]['value']
			entity_list.append((entity, value))
		intent = resp['intent'][0]['value']
	except:
		pass
		
	return entity_list, intent