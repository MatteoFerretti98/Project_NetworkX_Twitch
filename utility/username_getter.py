import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import json
import numpy as np
from tqdm import tqdm

nazione = "RU"
versione = "1"

df = pd.read_csv("./musae_"+nazione+"_target_new3.csv")

# decommentare se si vuole partire da un id specifico, in caso di interruzione
'''
last_index = df[df["id"]==127681742].index.tolist()[0]
print(last_index)

df = df[last_index+1:]
print(df)

list_username = df["username"]

df = df[list_username.isin(list_username[list_username.duplicated()])].sort_values("username")
df = df[np.logical_not(df["username"].isnull())]
'''

list_id = df["id"].to_list()

executable_path = "C://Users//sam//Desktop//Project_NetworkX_Twitch//chromedriver.exe"
os.environ["webdriver.chrome.driver"] = executable_path

chrome_options = Options()
chrome_options.add_extension('Twitch-Username-and-User-ID-Translator.crx')
dict={}
driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
driver.get("chrome-extension://laonpoebfalkjijglbjbnkfndibbcoon/form.html#")
for id in tqdm(list_id,leave=True):
    driver.execute_script("runRoutineV2('"+str(id)+"','User id')")
    time.sleep(2.5)
    res = driver.find_element(By.ID,'response').text
    if res != None: dict[str(id)] = res
    with open("file"+nazione+""+versione+".json","w") as outfile:
        json.dump(dict,outfile)
driver.quit()

