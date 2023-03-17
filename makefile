# Variables de configuration
APP_NAME=myapp
PYTHONPATH=$(PWD)/$(APP_NAME)

# Cible pour l'analyse statique avec Pylint : exécute Pylint pour effectuer une analyse 
#statique du code et détecter les erreurs de style.
lint:
	pylint $(APP_NAME) --rcfile=.pylintrc

# Cible pour exécuter les tests unitaires avec unittest
unittest:
	PYTHONPATH=$(PYTHONPATH) python -m unittest discover -s tests -p "*_test.py"

# Cible pour générer la documentation avec pdoc
docs:
	pdoc --html --force --output-dir=docs $(APP_NAME)

# Cible pour vérifier la couverture du code avec coverage
coverage:
	coverage run --source=$(APP_NAME) -m unittest discover -s tests -p "*_test.py"
	coverage report -m

# exécute toutes les tâches en une seule fois
all: lint unittest docs coverage
