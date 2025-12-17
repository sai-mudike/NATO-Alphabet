import pandas as pd




data_frame=pd.read_csv("nato_phonetic_alphabet.csv")
nato_data={row.letter:row.code for (index,row) in data_frame.iterrows()}


user_input=input("Enter a word: ").upper()

nato_words=[nato_data[letter] if letter in nato_data else None for letter in user_input]

print(nato_words)

