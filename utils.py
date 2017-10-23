from wit import Wit
import secrets

client = Wit(access_token=secrets.WIT_ACCESS_TOKEN)


def wit_response(message_text):
    resp = client.message(message_text)

    entity = None
    value = None

    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']
    except:
        pass

    return (entity, value)
