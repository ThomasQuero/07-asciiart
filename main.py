#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    tuples = []
    if not s:
        return tuples
    prev = s[0]
    count = 1
    for c in s[1:]:
        if c == prev:
            count += 1
        else:
            tuples.append((prev, count))
            prev = c
            count = 1
    tuples.append((prev, count))
    return tuples


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    if not s:
        return []
    # Compter le nombre d'occurrences du premier caractère
    count = 1
    while count < len(s) and s[count] == s[0]:
        count += 1
    # Appel récursif sur le reste de la chaîne
    return [(s[0], count)] + artcode_r(s[count:])
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
