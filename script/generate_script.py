import os


def _generate_script(data, output_dir, template_env):
    template_name = 'script.sh.erb'
    template = template_env.get_template(template_name)
    manifest = template.render(data)
    # Écrire le résultat dans un fichier de sortie
    output_name = 'script.sh.erb'
    output_path = os.path.join(output_dir, data['application']['name'], 'template', output_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        f.write(manifest)
        os.chmod(output_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
    print(f"Le fichier a été généré : {output_path}")
    return()