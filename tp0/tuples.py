def afficher_releve (reserve):
    nom_capteur= reserve[0]
    valeur = reserve[1]
    unite = reserve[2]
    return f"Capteur {nom_capteur} : {valeur} {unite}"

releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"

def recalibrer(releve,nom_capteur,valeur):
    for i in range (3):
        if ( releve [i][0] == nom_capteur) :
            nouveaux_reserves = (releve[i][0],valeur,releve[i][2])
            releve[i]=nouveaux_reserves
            
    return releve

nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3
    
