import os

try:
    os.mkdir(r"C:\Users\Elève\Downloads\dossier.zip") #
    os.mkdir(r"C:\Users\Elève\Downloads\dossierimage") #
    os.mkdir(r"C:\Users\Elève\Downloads\dossierword.pdf.etc")
    os.mkdir(r"C:\Users\Elève\Downloads\dossier.exe") #
    os.mkdir(r"C:\Users\Elève\Downloads\dossierautres")
    os.mkdir(r"C:\Users\Elève\Downloads\dossiervidéo") #
except:
    print("Les dossiers etaient déjà créé")
fichier =  os.listdir(r"C:\Users\Elève\Downloads")
for i in range(100):
    for name in fichier:
            if name == "dossier.zip" or name == "dossierimage" or name == "dossierword.pdf.etc" or name == "dossier.exe" or name == "dossierautres" or name =="dossiervidéo":
                print("C'est un des dossiers clé")
            else:
                try:
                    rename = "C:/Users/Elève/Downloads/" + name
                    if name.endswith(".exe"):
                        os.rename(rename, "C:/Users/Elève/Downloads/dossier.exe/"+name)
                    if name.endswith(".mp4") or name.endswith(".mp3") or name.endswith(".avi") or name.endswith("wav"):
                        os.rename(rename, "C:/Users/Elève/Downloads/dossiervidéo/"+name)
                    if name.endswith(".zip") or name.endswith(".tar.gz"):
                        os.rename(rename, "C:/Users/Elève/Downloads/dossier.zip/"+name)
                    if name.endswith(".jpg") or name.endswith(".PNG") or name.endswith(".webp") or name.endswith(".png") or name.endswith(".bmp") or name.endswith(".jpeg"):
                        os.rename(rename, "C:/Users/Elève/Downloads/dossierimage/"+name)
                    if name.endswith(".pdf") or name.endswith(".pptx") or name.endswith(".docx") or name.endswith(".odt") or name.endswith(".ppt") or name.endswith(".odf") or name.endswith(".calc") or name.endswith(".xlsx"):
                        os.rename(rename, "C:/Users/Elève/Downloads/dossierword.pdf.etc/"+name)
                    else:
                        os.rename(rename, "C:/Users/Elève/Downloads/dossierautres/"+name)
                except PermissionError and FileNotFoundError:
                    print("ERROR 404")

