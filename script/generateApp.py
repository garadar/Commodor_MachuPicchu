import os
import argparse
from jinja2 import Environment, FileSystemLoader
import yaml

from generate_form import _generate_form
from generate_manifest import _generate_manifest


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
        raise(e)

    # Configuration de Jinja2 pour charger des templates à partir d'un dossier
    template_dir = "templates"  # Dossier où se trouvent les templates
    env = Environment(loader=FileSystemLoader(template_dir))

    # Manifest
    _generate_manifest(data, output_dir, template_env=env)

    # Form
    _generate_form(data, output_dir, template_env=env)

    # Submit
    _generate_submit(data, output_dir, template_env=env)

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

