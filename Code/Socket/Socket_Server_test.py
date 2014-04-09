#Socket server qui devra etre implemente sous blender

import socket

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind(('', 12800))
connexion_principale.listen(5)

# /!\ commande blocante /!\
connexion_avec_client, infos_connexpeion = connexion_principale.accept()

print(infos_connexion)