import pandas as pd
import json

#UNICO PARAMETRO DA SETTARE
nazione = "RU"
#######################

df_original = pd.read_csv("./musae_"+nazione+"_target.csv")
l = df_original["id"].to_list()
with open('./dictionaries_id_username/file'+nazione+'.json') as json_file:
    data = json.load(json_file)
with open('./file'+nazione+'.json') as json_file1:
    data1 = json.load(json_file1)
with open('file'+nazione+'1.json') as json_file2:
     data2 = json.load(json_file2)
with open('file'+nazione+'2.json') as json_file3:
      data3 = json.load(json_file3)
with open('file'+nazione+'3.json') as json_file4:
     data4 = json.load(json_file4)
with open('file'+nazione+'4.json') as json_file5:
      data5 = json.load(json_file5)

data.update(data1)
data.update(data2)
data.update(data3)
data.update(data4)
data.update(data5)

df = pd.DataFrame.from_dict(data, orient='index',columns=['username']).reset_index(names=["id"])
df["id"] = df["id"].astype("int64")

if(len(df) != len(df_original)): exit("I 2 file non hanno stessa lunghezza! "+str(len(df))+" "+str(len(df_original)))
   
print(df_original["id"].dtype)
df_original = df_original.drop(columns=["username"])
df_merge = df_original.merge(df,how="left",on="id")
df_merge.to_csv("./musae_"+nazione+"_target_new4.csv",index=False)
print(df_merge)

df_original = pd.read_csv("./musae_"+nazione+"_target_new4.csv")
l = df_original["username"]
print(df_original[l.isin(l[l.duplicated()])].sort_values("username"))
df = df_original[df_original["username"].isnull()]
print(df)