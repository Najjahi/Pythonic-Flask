import os
from flask import current_app


def get_previous_next_recette(recette):
    plat = recette.plat_name
    for lsn in plat.recettes:
        if lsn.title == recette.title:
            index = plat.recettes.index(lsn)
            previous_recette = plat.recettes[index - 1] if index > 0 else None
            next_recette = (
                plat.recettes[index + 1] if index < len(plat.recettes) - 1 else None
            )
            break
    return previous_recette, next_recette


def delete_picture(picture_name, path):
    picture_path = os.path.join(current_app.root_path, path, picture_name)
    try:
        os.remove(picture_path)
    except:
        pass
