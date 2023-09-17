from flask import Flask #importe le Flask objet du flask module.  Cet objet est une application Flask, qui est le point d'entrée principal d'une application Web Flask. 

app = Flask(__name__)  #  crée un nouvel objet d'application Flask et l'affecte à la variable app.  Le __name__variable est le nom du module Python en cours d'exécution. 
app.secret_key = "shh"  # définit la clé secrète de l'application Flask.  La clé secrète est utilisée pour crypter les cookies de session et autres données sensibles.  Il est important de garder la clé secrète secrète, car toute personne la connaissant peut décrypter les données.
                        # il faut mettre la clé pr q sa marche , j7 juste enlever 




