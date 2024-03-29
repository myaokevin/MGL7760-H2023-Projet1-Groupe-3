# Variables de configuration
APP_NAME=web/project/app.py
PYTHONPATH=$(PWD)/$(APP_NAME)

# Cible pour l'analyse statique avec Pylint : exécute Pylint pour effectuer une analyse 
#statique du code et détecter les erreurs de style.
lint:
	pylint $(APP_NAME) 

# Cible pour exécuter les tests unitaires avec unittest
unittest:
	python -m unittest discover -s testunit -p "*.py" -v

# Cible pour générer la documentation avec pdoc. Cela générera une documentation HTML dans le dossier "docs" du projet.
docs:
	pdoc $(APP_NAME) 

# Cible pour vérifier la couverture du code avec coverage
coverage:
	coverage run --source=$(APP_NAME) -m unittest discover -s testunit -p "*.py"
	coverage report -m

# exécute toutes les tâches en une seule fois
all: lint unittest docs coverage

#---------------------------------------------------------------