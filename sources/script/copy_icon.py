"""Module generating form.yml."""

import os
import shutil



def _copy_icon(data, app_spec_dir, output_dir):
    # Copy Icon app in dest dir
    icon_in = os.path.join(app_spec_dir, "icon.png")
    icon_out = os.path.join(output_dir, data['application']['name'], "icon.png")
    try:
        shutil.copy(icon_in, icon_out)
        print(f"File copied to: {icon_out}")
    except (FileNotFoundError, PermissionError) as e:
        raise RuntimeError(f"Error during copy (check file exist/permission : {icon}")

    return()
