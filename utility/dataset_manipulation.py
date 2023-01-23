import pandas as pd
import numpy as np
nazioni = ["DE","ENGB","ES","FR","PTBR","RU"]

#target
for nazione in nazioni:
    path_target = "./twitch/"+nazione+"/musae_"+nazione+"_target.csv"
    df_target = pd.read_csv(path_target)
    df_target['username'] = np.where(df_target['username'].isnull(), df_target['new_id'], df_target['username'])
    df_target.to_csv(path_target,index=False)

    path_edges = "./twitch/"+nazione+"/musae_"+nazione+"_edges.csv"
    path_edges_out = "./twitch/"+nazione+"/musae_"+nazione+"_edges_username.csv"
    df_edges = pd.read_csv(path_edges)
    df_edges['from'] = df_edges['from'].map(df_target.set_index('new_id')['username'])
    df_edges['to'] = df_edges['to'].map(df_target.set_index('new_id')['username'])
    print(df_edges)
    df_edges.to_csv(path_edges_out,index=False)
    