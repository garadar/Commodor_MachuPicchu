"""Module generating the app using generate manifest/form/submit/script."""
import os
import argparse
from jinja2 import Environment, FileSystemLoader
import yaml

from generate_manifest import _generate_manifest
from generate_form import _generate_form
from generate_submit import _generate_submit
from generate_script import _generate_script
from copy_icon import _copy_icon


def get_yaml_app_spec(app_spec):
    """Charger le fichier YAML."""
    with open(app_spec, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data


def generate_file(app_spec, output_dir):
    """Fonction principale pour traiter la génération de fichier."""
    # Récupérer les données du pillar pour les clés spécifiées et le nom de la template
    try:
        data = get_yaml_app_spec(app_spec)
    except ValueError as e:
        print(e)
        raise e

    # Configuration de Jinja2 pour charger des templates à partir d'un dossier
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")  # Dossier où se trouvent les templates
    env = Environment(loader=FileSystemLoader(template_dir))

    # Manifest
    _generate_manifest(data, output_dir, template_env=env)

    # Form
    _generate_form(data, output_dir, template_env=env)

    # Script
    _generate_script(data, output_dir, template_env=env)

    # Submit
    _generate_submit(data, output_dir, template_env=env)

    # Copy icon
    _copy_icon(data, args.app_spec_dir, output_dir)

# Définir la fonction principale pour accepter des arguments de ligne de commande
if __name__ == "__main__":
    # Configurer argparse pour prendre le fichier app_spec yaml en argument
    parser = argparse.ArgumentParser(description="Générer une application OOD en utilisant un fichier app_spec et un  template Jinja2.")
    parser.add_argument('app_spec_dir', type=str, help="Chemin vers le répertoire  app_spec au format .yml")
    parser.add_argument('output_dir', type=str, help="Chemin vers le répertoire de sortie")

    # Lire les arguments
    args = parser.parse_args()

    # Appeler la fonction principale avec le minion_id et les clés du pillar
    app_spec = args.app_spec_dir + "/config.yml"
    generate_file(app_spec, args.output_dir)
