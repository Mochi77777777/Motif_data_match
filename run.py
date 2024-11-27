import pandas as pd

main = pd.read_csv('first_BC_MUT_knownResults.csv',usecols=['Motif Name'])
target = pd.read_csv('TR.csv',usecols=['TF_motifs'])
p_value= pd.read_csv('first_BC_MUT_knownResults.csv',usecols=['Motif Name','P-value'],na_values=[0])

motif_list = main['Motif Name'].tolist()

target_list = target['TF_motifs'].tolist()

match_motif = []
match_target = []
pv_match = []

for a in motif_list:
    for b in target_list:
        if b in a :
            match_motif.append(a)
            match_target.append(b)
            p_value_row = p_value[p_value['Motif Name'] == a]
            if not p_value_row.empty:
                pv_match.append(p_value_row['P-value'].values[0])
            else:
                pv_match.append(None)


data = {'Motif Name':match_motif,'TF_motifs':match_target,'P-value':pv_match}


df = pd.DataFrame(data)

df.to_excel('data.xlsx')