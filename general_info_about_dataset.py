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

# only take metropolitan French regions
regions_to_exclude = [
    'La Réunion',
    'Guyane',
    'Corse',
    'Martinique',
    'Guadeloupe',
    'Polynésie française'
]
parcoursup_but = parcoursup_but[~parcoursup_but['Région de l’établissement'].isin(regions_to_exclude)]

# https://dataesr.fr/fichiers/tableaux_synthese_DUT_22.pdf

salaries = {
    'BUT -  Gestion des entreprises et des administrations': 1460,
    'BUT -  Génie industriel et maintenance': 1630,
    'BUT -  Techniques de commercialisation': 1500,
    'BUT -  Informatique': 1600,
    'BUT -  Qualité, logistique industrielle et organisation': 1630,
    'BUT -  Carrières sociales ': 1400,
    'BUT -  Génie biologique ': 1600,
    'BUT -  Chimie': 1440,
    'BUT -  Génie civil - Construction durable': 1620,
    'BUT -  Génie électrique et informatique industrielle': 1800,
    'BUT -  Management de la Logistique et des Transports': 1500,
    'BUT -  Information communication ': 1320,
    'BUT -  Carrières juridiques': 1500,
    'BUT -  Gestion administrative et commerciale des organisations': 1500,
    'BUT -  Génie mécanique et productique': 1680,
    'BUT -  Hygiène Sécurité Environnement': 1630,
    'BUT -  Réseaux et télécommunications': 1600,
    'BUT -  Mesures physiques': 1700,
    'BUT -  Science et génie des matériaux': 1630,
    'BUT -  Statistique et informatique décisionnelle': 1500,
    'BUT -  Métiers du multimédia et de l\'internet': 1400,
    'BUT -  Métiers de la Transition et de l\'Efficacité Énergétiques': 1630,
    'BUT -  Génie chimique génie des procédés': 1630,
    'BUT -  Packaging, emballage et conditionnement': 1630,
}

parcoursup_but["salary"] = parcoursup_but['diploma_name'].map(salaries)

parcoursup_but.to_csv('parcoursup_but.csv')