import requests
from bs4 import BeautifulSoup
import csv

liste = [] #liste pour stocker les données extraites 
listetitre = [] #liste pour stocker les titres des colonnes 
n = 10 
url = "https://www.scrapethissite.com/pages/forms/?page_num="
def scrapping(url):
    global liste
    global listetitre
    response = requests.get(url) #envoyer une requete GET à l'url 
    soup = BeautifulSoup(response.content, "html.parser") #analyser les contenu HTML de la page 
    tableau = soup.find('table') #trouver l'élément 'table' qui contient les données 
    titres = tableau.find('tr').find_all('th') #récupérer les titres des colonnes 
    
    if int(url[len(url)-1]) == 1:
        for titre in titres:
            listetitre.append(titre.text.strip()) #ajouter les titres à la liste 
        liste.append(listetitre) #ajouter la liste des titres à la liste principale 
    else:
        rows = tableau.find_all('tr') #récupérer toutes les lignes du tableau 
        for j in range(1,len(rows)):
            ligne = [] #liste pour stocker les valeurs d'une ligne 
             # Extraire les valeurs de chaque colonne dans la ligne
            ligne.append(rows[j].select('.name')[0].text.strip())
            ligne.append(rows[j].select('.year')[0].text.strip())
            ligne.append(rows[j].select('.wins')[0].text.strip())
            ligne.append(rows[j].select('.losses')[0].text.strip())
            ligne.append(rows[j].select('.ot-losses')[0].text.strip())
            ligne.append(rows[j].select('.pct')[0].text.strip())
            ligne.append(rows[j].select('.gf')[0].text.strip())
            ga = rows[j].select('.ga')[0].text.strip()
            ligne.append(ga)
            diff = rows[j].select('.diff')[0].text.strip()
            ligne.append(diff)
                        # Vérifier certaines conditions pour ajouter la ligne à la liste principale
            if int(diff) > 0 and int(ga) < 300:
                liste.append(ligne) # Ajouter la ligne à la liste principale
# Boucle pour effectuer le scraping sur chaque page
for i in range(1,n+1):
    scrapping(url+str(i))
# Écriture des données dans un fichier CSV
with open('result.csv', mode='w', newline='') as fichier:
    writer = csv.writer(fichier)
    writer.writerows(liste)

print("scrapping réussi.")
