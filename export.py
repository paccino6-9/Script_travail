import os
import pandas as pd

# === Dossier courant (là où est lancé le script) ===
racine = os.getcwd()

# Récupérer uniquement les dossiers au premier niveau
noms_dossiers = [d for d in os.listdir(racine) if os.path.isdir(os.path.join(racine, d))]

# Créer un DataFrame
df = pd.DataFrame({"Nom dossier": noms_dossiers})

# Sauvegarder en Excel dans le dossier courant
fichier_excel = os.path.join(racine, "liste_dossiers.xlsx")
df.to_excel(fichier_excel, index=False)

print(f"Fichier Excel créé : {fichier_excel}")