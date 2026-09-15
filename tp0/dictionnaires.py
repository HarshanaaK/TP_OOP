def quantite_piece(pieces_stock, Modele, piece):
    pieces_stock[Modele][piece]
    
    return pieces_stock[Modele][piece]


pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}
assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10


def consommer_piece(pieces_stock, Modele, piece, n):
    pieces_stock[Modele][piece] = pieces_stock[Modele][piece]-n
    return pieces_stock[Modele][piece]
    
consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7

def ajouter_modele(pieces_stock, Modele,moteurs,capteurs, roues):
    pieces_stock[Modele]={"moteurs":moteurs,"capteurs":capteurs,"roues":roues}
    return pieces_stock

ajouter_modele(pieces_stock, "ModeleC",moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == \
{"moteurs": 4, "capteurs": 10, "roues": 16}

def total_pieces(pieces_stock):
    
    total_moteurs = 0
    total_capteurs = 0
    total_roues = 0
    
    for Modele in pieces_stock:
        total_moteurs += pieces_stock[Modele]["moteurs"]
        total_capteurs += pieces_stock[Modele]["capteurs"]
        total_roues += pieces_stock[Modele]["roues"]
        
    return {"moteurs": total_moteurs, "capteurs": total_capteurs, "roues": total_roues}

totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}



