#importer à partir d'un fichier csv

# Check if the filename is set as environment variable
if [[ -z "${CSV_FILE}" ]]; then
CSV_FILE="biblio.csv"
fi
# Create an empty SQL file
DB_FILE=biblio.sql
touch $DB_FILE
# Skip the first line
tail -n +2 $CSV_FILE > csv_file_data.csv
while IFS=, read -r titre description isbn annee_apparition image auteur editeur categorie
do
echo "
INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('$titre', '$description', '$isbn', '$annee_apparition', '$image', '$auteur', '$editeur','$categorie' );" >> $DB_FILE
done < csv_file_data.csv
#############