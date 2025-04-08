import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 

import pandas as pd

df = pd.read_csv('coordinate.csv')

print(df.to_string()) 
