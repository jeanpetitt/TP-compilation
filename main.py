import re


def find_comment(text):
    # l'alphabet ici est  l'ensemble des
    #caractères ascii
    
    # definir une expression  pour la reconnaissance des commentaire

    rejex = r'%\*/|/\*([^*]|\*(?!/))*\*/'
    rejex1 = r'\#|/\*([^*]|\*(?!/))*\*/'
    """
        nous pouvons decouper notre pattern rejex en quatre partie
        - %\*/: cette partie recherche %*/ cette sequence evite que l'expression régulière
        ne soit interpré comme commentaire multi-ligne dans certaines situation
        - |: indique qu'il y'a une alternative soit rechercher une chaine qui commence par /* et ce termine par 
        */
        - /\*: cette partie recherche le caractere /* qui ouvre le commentaire
        -([^*]|\*(?!/)): recherche tous les kteres qui se trouvent entre /* et */. cette syntaxe signifie
        trouver tous les caractères sauf *  * qui n'est pas suivi de /
        
        - /\* fermeture du commentaire
    """

    # trouver toute les correspondance du rejex dans le texte
    comment = re.findall(rejex1, text)
    print(comment)

    return comment


texte1 = '%*/ceci est un commentaire \n  ceci est pas commentaire \n /* ceci est un second commentaire */")'
texte2 = "# commentaire sur une ligne"

find_comment(texte1)
find_comment(texte2)


    
