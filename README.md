# chess_project

Pour rappel, il est nécessaire d'avoir python et git installé.

Pour exécuter le programme:

1. Ouvrir la console de Git
2. Se rendre à l'emplacement où l'on veut cloner le projet
3. Exécuter "git clone https://github.com/jaikko/chess_project.git"
4. Dans cette console, se rendre dans le dossier racine du projet avec la commande "cd chess_project" 
5. Exécuter la commande "virtualenv -p python3 venv". venv est le nom de dossier.
6. Dans la racine du dossier du projet, éxecuter la commande "source venv/Scripts/activate"
7. Lancez la commande "python -m pip install -r requirements.txt"
8. Exécuter "python main.py"

Pour générer un nouveau fichier flake8-html:

1. Ouvrir la console de Git
2. Si aucun environnement virtuel est créé, se référer aux étapes 4et 5 au-dessus
3. Dans la racine du dossier du projet, éxecuter la commande "source venv/Scripts/activate"
4. Dans la racine du dossier du projet, éxecuter flake8 --format=html --htmldir=flake8-report

Pour utiliser le progamme, il suffit de suivre les indications indiquées.




