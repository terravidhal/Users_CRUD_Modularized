from flask_app import app  # importe le app objet du flask_app module.  Cet objet est une application Flask, qui est le point d'entrée principal d'une application Web Flask. 

# import users.py from folder 'flask_app/controllers'
from flask_app.controllers import users 


if __name__ == "__main__":  # est une vérification pour voir si le code est exécuté en tant que programme principal.  Si c'est le cas, alors le app.run()La méthode est appelée pour démarrer l’application Flask.  Le debug=TrueL'argument indique à Flask de s'exécuter en mode débogage, ce qui imprimera des messages d'erreur plus détaillés en cas de problème.
    app.run(debug=True, port=4000)

