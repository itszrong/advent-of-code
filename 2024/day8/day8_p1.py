# pip install pandas

import pandas as pd
input_df = pd.DataFrame([list(line) for line in input_str.split('\n')])

freq_dict = {}
for i in range(len(input_df)):
    for j in range(len(input_df.columns)):
        value = input_df.iloc[i,j]
        if value not in ['.']:
            if value in freq_dict:
                freq_dict[value].append((i,j))
            else:
                freq_dict[value] = [(i,j)]
freq_dict

antinode_set = set()
all_antennas = sum(freq_dict.values(), [])
for key in freq_dict:
    for i in freq_dict[key]:
        for j in freq_dict[key]:
            if i == j:
                pass
            else:
                dx = j[0]-i[0]
                dy = j[1]-i[1]
                n=1
                while 0 <= i[0]-n*dx < len(input_df.columns) and 0 <= i[1]-n*dy < len(input_df):
                    antinode_set.add((i[0]-n*dx,i[1]-n*dy))
                    n += 1
                
                dx = j[0]-i[0]
                dy = j[1]-i[1]
                n=1
                while 0 <= j[0]+n*dx < len(input_df.columns) and 0 <= j[1]+n*dy < len(input_df):
                    antinode_set.add((j[0]+n*dx,j[1]+n*dy))
                    n += 1
        
        antinode_set.add(i)

len(antinode_set), antinode_set
