"""Module generating manifest.yml."""

import os


def _generate_manifest(data, output_dir, template_env):
    template_name = 'manifest.yml'
    template = template_env.get_template(template_name)
    manifest = template.render(data)
    # Écrire le résultat dans un fichier de sortie
    output_name = 'manifest.yml'
    output_path = os.path.join(output_dir, data['application']['name'], output_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(manifest)
    print(f"Le fichier a été généré : {output_path}")
    return()
