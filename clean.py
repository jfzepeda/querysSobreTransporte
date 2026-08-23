import pandas as pd
import numpy as np

df = pd.read_csv("/Users/juanfelipezepeda/Documents/TEC/Javier 3/querysSobreTransporte/data/enmt_unam.csv", encoding="latin-1")
df_clean = df[[
"p1a_1",
"p1a_2",
"p1a_3",
"p1a_4",
"p1a_5",
"p1a_6",
"p1a_7",
"p1a_8",
"p1a_9",
"p1a_10",
"p1a_11",
"p1a_12",
"p1a_13",
"p1a_14",
"p1a_15",
"p1a_16",
"p1a_17",
"p1a_18",
"p1a_19",
"p1a_20",
"p1a_21",
"p1a_22",
"p17_1",
"p17_4",
"sexo",
"edad_1",
"escol",
"cond_act",
"h21_1",
"Tam_loc",
"ing_fam",
"Pondi2",
"estrato"]]

save_path = "/Users/juanfelipezepeda/Documents/TEC/Javier 3/querysSobreTransporte/data/clean_enmt_unam.csv"
df_clean.to_csv(save_path, index=False)