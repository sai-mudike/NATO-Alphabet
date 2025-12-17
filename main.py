import pandas as pd
data_frame=pd.read_csv("nato_phonetic_alphabet.csv")
print(data_frame)

nato={row.letter:row.code for (index,row) in data_frame.iterrows()}
