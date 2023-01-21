import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import json

df = pd.read_csv("./twitch/PTBR/musae_PTBR_target.csv")
list_id = df["id"].to_list()

executable_path = "C://Users//sam//Desktop//Project_NetworkX_Twitch//chromedriver.exe"
os.environ["webdriver.chrome.driver"] = executable_path

chrome_options = Options()
chrome_options.add_extension('Twitch-Username-and-User-ID-Translator.crx')
dict={}
for id in list_id:
    
    driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
    driver.get("chrome-extension://laonpoebfalkjijglbjbnkfndibbcoon/form.html#")

    driver.execute_script("runRoutineV2('"+str(id)+"','User id')")
    time.sleep(2.5)
    res = driver.find_element(By.ID,'response').text
    print(res)
    if res != None: dict[str(id)] = res
    with open("file.json","w") as outfile:
        json.dump(dict,outfile)
    driver.quit()

