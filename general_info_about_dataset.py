import pandas as pd

parcoursup = pd.read_csv('datasets/fr-esr-parcoursup.csv')

# filter by BUT
parcoursup_but = parcoursup.loc[parcoursup['Filière de formation.1'].str.contains("BUT ", case=True)]

# create the column to the name of diploma
parcoursup_but["diploma_name"] = "BUT - "\
                                 + " " + parcoursup_but["Filière de formation détaillée bis"]

# merge different 'parcours'
parcoursup_but["diploma_name"] = parcoursup_but["diploma_name"].str.split('parcours').str[0]
parcoursup_but["diploma_name"] = parcoursup_but["diploma_name"].str.split('Parcours').str[0]


parcoursup_but.to_csv('parcoursup_but.csv')