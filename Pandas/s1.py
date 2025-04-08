import pandas as pd
import numpy as np
d=pd.read_csv("s1.csv")

d["Sport"]="Cricket"

print(d)
d1=d.to_csv("s2.csv")
print("loc \n",d.loc[3,['P']])
print("iloc \n",d.iloc[3,2])
#print(d.isna())
#k=int(np.mean(d["P"]))
#print(k)
#df=d.fillna(k)
#print(df)
#print(d.isnull())
#print(d)
#df=d.dropna()
#print(df)
#df1=d.drop_duplicates(["Sport"])
#print(df1)
#print(d.describe())
#print(d.info())
#d1=d[d["P"]<40]
#print(d1["P"])
d.insert(1,"Sports",['AA','BB','VV','DD','BB','VV','DD','BB','VV','DD','BB','VV','DD','POP'])
print(d)
#del(d["Sports"])
#d=d.drop(columns=["Sport"])
#print(d)

#d=d.rename(columns={"P":"Physics"})
#print(d)
#d.loc[4]=[4,"KL",23,34,56,'basketball']
#print(d)



