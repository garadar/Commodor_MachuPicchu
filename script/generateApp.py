import os
import argparse
from jinja2 import Environment, FileSystemLoader
import salt.client  # Le module SaltStack pour interagir avec Salt

# Fonction pour récupérer les données spécifiques du pillar SaltStack
def get_pillar_data(minion_id, key):
    # Initialiser le client Salt
    client = salt.client.LocalClient()

    # Obtenir les données de tout le pillar pour ce minion
    req= 'nodes:' + key
    print(req)
    pillar_data = client.cmd(minion_id, 'pillar.get', [req])

    if pillar_data and minion_id in pillar_data:
        minion_pillar = pillar_data[minion_id]
        # Extraire seulement les clés spécifiées
        data_to_return = {}
        for key in keys:
            value = minion_pillar.get(key, None)
            print(value)
            if value is not None:
                data_to_return[key] = value
            else:
                print(f"Attention: La clé '{key}' n'existe pas dans le pillar pour {minion_id}.")
        
        # Vérifier si 'template_name' est présent dans le pillar
        template_name = minion_pillar.get('template_name', None)
        if not template_name:
            raise ValueError(f"Aucune template spécifiée dans le pillar (clé 'template_name') pour le minion {minion_id}")
        
        return data_to_return, template_name
    else:
        raise ValueError(f"Aucune donnée de pillar trouvée pour le minion {minion_id}")

# Fonction principale pour traiter la génération de fichier
def generate_file(minion_id, key):
    # Récupérer les données du pillar pour les clés spécifiées et le nom de la template
    try:
        data, template_name = get_pillar_data(minion_id, key)
    except ValueError as e:
        print(e)
        exit(1)

    # Configuration de Jinja2 pour charger des templates à partir d'un dossier
    template_dir = "templates"  # Dossier où se trouvent les templates
    env = Environment(loader=FileSystemLoader(template_dir))

    # Charger la template spécifiée dans le pillar
    try:
        template = env.get_template(template_name)
    except Exception as e:
        print(f"Erreur lors du chargement de la template '{template_name}': {e}")
        exit(1)

    # Rendre le template avec les données du pillar
    rendu = template.render(data)

    # Écrire le résultat dans un fichier de sortie
    output_path = os.path.join("output", f"{minion_id}_config.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        f.write(rendu)

    print(f"Le fichier a été généré : {output_path}")

# Définir la fonction principale pour accepter des arguments de ligne de commande
if __name__ == "__main__":
    # Configurer argparse pour prendre le minion_id et les clés du pillar en argument
    parser = argparse.ArgumentParser(description="Générer un fichier à partir des données du pillar SaltStack et d'un template Jinja2.")
    parser.add_argument('minion_id', type=str, help="Le minion_id pour récupérer les données du pillar")
    parser.add_argument('key', type=str, help="Les clés spécifiques du pillar à récupérer (ex: grains.id pillar.roles)")

    # Lire les arguments
    args = parser.parse_args()

    # Appeler la fonction principale avec le minion_id et les clés du pillar
    generate_file(args.minion_id, args.key)

