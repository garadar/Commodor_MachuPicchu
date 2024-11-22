import os
import argparse
from jinja2 import Environment, FileSystemLoader

import yaml


def getYamlAppSpec(app_spec):

    # Charger le fichier YAML
    with open(app_spec, "r") as file:
        data = yaml.safe_load(file)

    return data


# Fonction principale pour traiter la génération de fichier
def generate_file(app_spec, output_dir):
    # Récupérer les données du pillar pour les clés spécifiées et le nom de la template
    try:
        data = getYamlAppSpec(app_spec)
    except ValueError as e:
        print(e)
        exit(1)

    # Configuration de Jinja2 pour charger des templates à partir d'un dossier
    template_dir = "templates"  # Dossier où se trouvent les templates
    env = Environment(loader=FileSystemLoader(template_dir))

    # Charger la template spécifiée dans le pillar
    template_name = 'form.yml'
    try:
        template = env.get_template(template_name)
    except Exception as e:
        print(f"Erreur lors du chargement de la template '{template_name}': {e}")
        exit(1)

    # Rendre le template avec les données du pillar

    rendu = template.render(data)

    # Écrire le résultat dans un fichier de sortie
    output_name = 'my_new_form.yml'
    output_path = os.path.join(output_dir, data['application']['name'], output_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        f.write(rendu)

    print(f"Le fichier a été généré : {output_path}")

# Définir la fonction principale pour accepter des arguments de ligne de commande
if __name__ == "__main__":
    # Configurer argparse pour prendre le fichier app_spec yaml en argument
    parser = argparse.ArgumentParser(description="Générer une application OOD en utilisant un fichier app_spec et un  template Jinja2.")
    parser.add_argument('app_spec', type=str, help="Chemin vers le fichier app_spec au format yaml")
    parser.add_argument('output_dir', type=str, help="Chemin vers le répertoire de sortie")

    # Lire les arguments
    args = parser.parse_args()

    # Appeler la fonction principale avec le minion_id et les clés du pillar
    generate_file(args.app_spec, args.output_dir)

