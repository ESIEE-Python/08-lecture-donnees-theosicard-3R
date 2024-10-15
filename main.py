'''
Fichier main.py
'''

#### Imports et définition des variables globales
#import random

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []

    with open(filename, 'r+', encoding='utf-8') as f:
        a = f.readlines()

    for line in a:
        line = line.replace('\n', '')
        sub_list = line.split(';')
        sub_list = [int(item) for item in sub_list]
        l.append(sub_list)

    return l

def get_list_k(data, k):
    '''
    Retourne la liste à l'indice K dans la liste data
    '''
    l = []
    l = data[k]
    return l

def get_first(l):
    '''
    Récupère le premier élement de la liste.
    '''
    return int(l[0])

def get_last(l):
    '''
    Récupère le dernier élément
    '''
    return int(l[-1])

def get_max(l):
    '''
    Récupère la valeur max
    '''
    return max(map(int, l))

def get_min(l):
    '''
    Récupère la valeur min
    '''
    return min(map(int, l))

def get_sum(l):
    '''
    Calcul la somme de la liste. 
    '''
    return sum(map(int, l))

#### Fonction principale

def main():
    '''
    Fonction main() du script
    '''
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, k))

    # Test de quelques fonctions
    b = get_first(data[0])
    print(f'First : {b}')

    c = get_last(data[0])
    print(f'Last : {c}')

    d = get_max(data[0])
    print(f'Max : {d}')

    e = get_min(data[0])
    print(f'min : {e}')

    f = get_sum(data[0])
    print(f'sum: {f}')

if __name__ == "__main__":
    main()
