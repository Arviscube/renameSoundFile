import os
import sys
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, ID3NoHeaderError

def update_music_titles(directory):
    """
    Parcourt un répertoire et remplace le titre des fichiers musicaux
    par le nom du fichier (sans extension).
    """
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.mp3', '.flac', '.m4a', '.wav', '.ogg')):
            filepath = os.path.join(directory, filename)
            file_title = os.path.splitext(filename)[0]  # Nom du fichier sans extension

            try:
                if filename.lower().endswith('.mp3'):
                    # Chargement des métadonnées pour un fichier MP3
                    try:
                        audio = EasyID3(filepath)
                    except ID3NoHeaderError:
                        # Si aucune métadonnée n'existe, en créer une
                        audio = EasyID3()

                    audio['title'] = file_title
                    audio.save()
                else:
                    print(f"Modification des métadonnées non supportée pour {filename}.")
                print(f"Titre modifié pour : {filename}")
            except Exception as e:
                print(f"Erreur lors de la modification de {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation : python3 rename.py path/to/directory")
        sys.exit(1)

    music_directory = sys.argv[1]
    if os.path.exists(music_directory):
        update_music_titles(music_directory)
    else:
        print("Répertoire introuvable.")
