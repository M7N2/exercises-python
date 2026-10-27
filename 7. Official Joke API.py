import requests
import pandas as pd 

url = 'https://official-joke-api.appspot.com/jokes/ten'
r = requests.get(url)
df = pd.DataFrame(r.json())
print(df[['setup', 'punchline']].to_string(index=False))
#df.drop(columns=['type', 'id'], inplace=True)
#df
