personajes = ['Harry Houdini', 'Newton', 'David Blane',
              'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']


def filtrar_personajes(personajes, tipo):
    magos = []
    cientificos = []
    otros = []
    for x in personajes:
        if x == 'Harry Houdini' or x == 'Teller' or x == 'David Blane':
            magos.append(x)
        elif x == 'Newton' or x == 'Hawking' or x == 'Einstein':
            cientificos.append(x)
        else:
            otros.append(x)

    if tipo == 'magos':
        return magos
    elif tipo == 'cientificos':
        return cientificos
    else:
        return otros


magos = filtrar_personajes(personajes, 'magos')
cientificos = filtrar_personajes(personajes, 'cientificos')
otros = filtrar_personajes(personajes, 'otros')


def hacer_grandioso(magos):
    lista_gran = []
    for x in range(len(magos)):
        lista_gran.append('El gran ' + magos[x])
    return lista_gran


lista_gran = hacer_grandioso(magos)


def imprimir_nombres():
    print(* personajes, sep='\n')
    print('\n Magos:', * lista_gran, sep='\n')
    print('\n Cientificos:', * cientificos, sep='\n')
    print('\n Otros:',  *otros, sep='\n')


imprimir_nombres()
