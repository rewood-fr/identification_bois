# identification_bois
L'accès au notebook pour l'exploitation des données est disponible sur le Notion de Rewood.
L’outil de matchmaking a été réalisé à l’aide d’un réseau de neurones sur Google Colab. Le principal avantage de cette plateforme est qu’elle est accessible gratuitement et permet l’accès à des ressources puissantes via des serveurs en ligne.

L’ensemble de la base de données d’images se trouve sur ce dépôt GitHub ainsi que certains scripts pour effectuer la répartition des données en trois groupes : train, validation, test (cf. notebook pour comprendre à quoi celà correspond). Il n’est donc pas nécessaire d’accéder directement au dépôt GitHub pour pouvoir utiliser le Notebook. Cependant, lors de l’ajout de données, il est important de récupérer l’ensemble des données présentes sur le dépôt ainsi que les fonctions pour pouvoir de nouveau séparer les classes en tenant compte des nouvelles essences ajoutées.

Pour ajouter des images, il suffit de créer les ajouter dans leur dossier sur Github (ou de comit si vous avez lié le dépôt à un de vos dossier local). Il faut les ajouter dans le **dossier global**, un algorithme que vous lancerez par la suite s’occupera de la partition.

Les deux fonctions présentes sur GitHub sont :

• **Partition** : fonction qui se lance depuis un terminal permettant de séparer l’ensemble des données de global dans les 3 catégories :  train (80% des images), validation (10% des images), test (10% des images). La partition est semi-aléatoire car on tire les images au hasard pour chaque classe en s’assurant que pour chaque classe il y ait suffisamment d’images dans chacune des trois catégories.

• **countData** : fonction qui se lance depuis un terminal permettant de déterminer le nombre d’images par classe et leur répartition dans chacune des catégories.
