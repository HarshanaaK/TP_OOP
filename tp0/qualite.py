"""fonction calculons le coût énergétique d’un déplacement selon
le type de terrain, la fonction prend en entrée :
t : le type de terrain,
x1 et y1 : la position de départ,
x2 et y2 : la position finale"""
def f(t, x1, y1, x2, y2):
    #création d'une variable calculant la distance de déplacement
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 
    if t == "R": # condition type de terrain
        c = dist * 1.0 # calcul du cout
    elif t == "H":
        c = dist * 1.5
    elif t == "S":
        c = dist * 2.0
    else:
        c = dist * 3.0
    return c
 
 #la fonction avait une variable d inutilisé au départ et manqué de documentation (docstring) et ne définssait pas les variable créés et avait mélangé affichage et calculs.