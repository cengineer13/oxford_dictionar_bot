import requests
from pprint import pprint as print



app_id = "d1f65482"
app_key = "39b9f5b6e854c3d4f95a9ff3531be7c7"
language = "en-gb"

def getDefinition(word):

    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word.lower()
    response = requests.get(url=url, headers={"app_id": app_id, "app_key":app_key})

    #get data
    data = response.json()
    if 'error' in data.keys():
        return False #Bu so'z mavjud emas


    entries = data['results'][0]['lexicalEntries'][0]['entries']
    # store definition and audio
    output = {}
    for entry in entries:
        # Check audio file is available
        if entry["pronunciations"][0]['audioFile'] is not None:
            output["audio"] = entry["pronunciations"][0].get("audioFile") #get value of specific key

        df_list = []
        for sense in entry['senses']:
            df_list.append(f"👉 {sense['definitions'][0]}")
            output['definitions'] = "\n".join(df_list)
    return output

if __name__ == '__main__':
    print(getDefinition("stuff"))
    print(getDefinition('sasdasd'))


