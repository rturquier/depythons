# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:17:50 2020

@author: Rémi Turquier
"""


# import libraries
import pandas as pd


# import API module
import depute_api

# load deputies dataframe
api = depute_api.CPCApi()
deputies_json = api.parlementaires()
deputies_df = pd.json_normalize(deputies_json)

# get list of all *groupes parlementaires*
groupes = deputies_df["groupe_sigle"].unique()

# Intermediary functions
def deputies_of_group(group, n_deputies):
    all_names = deputies_df[deputies_df["groupe_sigle"] == group]["nom"]
    return all_names[:n_deputies]


def interventions_of_group(group, n_deputies=15):
    names = deputies_of_group(group, n_deputies)
    print(names)
    interventions = []
    for name in names:
        print(name)
        interventions += [[group, name, api.interventions2(name)]]
    return interventions


# Populate list of interventions (this step takes some time)
"""
interventions_from_all_groups = []

for groupe in groupes[8:]:
    interventions_from_all_groups += interventions_of_group(groupe)

interventions_df = pd.DataFrame(
    interventions_from_all_groups, columns=["groupe", "nom", "interventions"]
)
"""

def stockintervention(groupe):
    interventions_group = []
    nbdep = deputies_df.groupby('groupe_sigle')['nom'].count()[str(groupe)]
    print(nbdep)
    interventions_group += interventions_of_group(groupe, nbdep)
    interventions_df = pd.DataFrame(
        interventions_group,
        columns=["groupe", "nom", "interventions"]
        )
    
    return interventions_df


deputies_df.groupby('groupe_sigle')['nom'].count()

LREM_inter_df = stockintervention('LREM')
LREM_inter_df

path_csv = r"C:\Users\Asus\Desktop\Jérémie\Fac_ENSAE\Informatique\Datapython_2AS1\Projet\LREM_inter.csv"
LREM_inter_csv = LREM_inter_df.to_csv(path_csv)

MODEM_inter_df = stockintervention('MODEM')

path_csv2 = r"C:\Users\Asus\Desktop\Jérémie\Fac_ENSAE\Informatique\Datapython_2AS1\Projet\MODEM_inter.csv"
MODEM_inter_df.to_csv(path_csv2)

LR_inter_df = stockintervention('LR')

path_csv3 = r"C:\Users\Asus\Desktop\Jérémie\Fac_ENSAE\Informatique\Datapython_2AS1\Projet\LR_inter.csv"
LR_inter_df.to_csv(path_csv3)

SOC_inter_df = stockintervention('SOC')

path_csv4 = r"C:\Users\Asus\Desktop\Jérémie\Fac_ENSAE\Informatique\Datapython_2AS1\Projet\SOC_inter.csv"
SOC_inter_df.to_csv(path_csv4)

for group in ['AE', 'GDR', 'LFI', 'LT', 'NG', 'NI', 'UAI', 'UDI']:
    group_inter_df = stockintervention(group)
    path_csv_for = r"C:\Users\Asus\Desktop\Jérémie\Fac_ENSAE\Informatique\Datapython_2AS1\Projet\{0}_inter.csv".format(group)
    group_inter_df.to_csv(path_csv_for)
