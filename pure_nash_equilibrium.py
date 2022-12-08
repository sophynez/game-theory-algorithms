import numpy as np

'''
to do :
stratégie pure :
- pareto optimum
- equilibre de nash

strategie mixte :
- support [ DONE ]
- paiement [ DONE ]
- utilité
- equilibre de nash
'''
sig1 = [1/3, 1/3, 1/3]
sig2 = [0, 1/2, 1/2]

strat1 = ['U', 'D', 'M']
strat2 = ['L', 'M', 'R']

matrice = [[[4, 3], [5, 1], [6, 2]],
           [[2, 1], [8, 4], [3, 6]],
           [[3, 0], [9, 6], [2, 5]]]
# support
def return_supp(sig, strat) :
    cpt = 0
    supp = []
    non_supp = []
    for i in sig :
        if i != 0 :
            supp.append(strat[cpt])
        else :
            non_supp.append(strat[cpt])
        cpt += 1
    return supp, non_supp

supp1, non_supp1 = return_supp(sig1, strat1)
supp2, non_supp2 = return_supp(sig2, strat2)
print(f'Le support du joueur 1 {supp1}')
print(f'Non_supp du joueur 1 : {non_supp1}')
print(f'Le support du joueur 2 {supp2}')
print(f'non_supp du joueur 2 {non_supp2}')

# paiement strategie
def return_paiement(sig ,strategie, joueur):
    cpt = 0
    paiement = 0
    if joueur == 1 :
        for i in matrice[strategie] :
            paiement += sig[cpt] * i[0]
            cpt += 1
        return paiement
    if joueur == 2 :
        for i in range(3) :
            paiement += matrice[i][strategie][1] * sig[cpt]
        return paiement

print(f' Les paiements du joueurs 1' )
p1_u = return_paiement(sig2, 0, 1)
p1_d = return_paiement(sig2, 1, 1)
p1_m = return_paiement(sig2, 2, 1)

print(f'paiement strategie U {p1_u}')
print(f'paiement strategie D {p1_d}')
print(f'paiement strategie M {p1_m}')

print(f' Les paiements du joueurs 2' )
p2_l = return_paiement(sig1, 0, 2)
p2_m = return_paiement(sig1, 1, 2)
p2_r = return_paiement(sig1, 2, 2)

print(f'paiement strategie L {p2_l}')
print(f'paiement strategie M {p2_m}')
print(f'paiement strategie R {p2_r}')

# fonction d'utilité
p1 = [p1_u, p1_d, p1_m]
p2 = [p2_l, p2_m, p2_r]
def return_utilite(paiement, sig) :
    utilite = 0
    cpt = 0
    for i in range(3):
        utilite += paiement[cpt] * sig[cpt]
        cpt += 1
    return utilite


print(f' Utilité joueur 1 :: {return_utilite(p1, sig1)}')
print(f' Utilité joueur 2 :: {return_utilite(p2, sig2)}')

def return_indiff_supp(paiement, utilite, non_supp) :
    if all_equal(paiement) and paiement[0]==utilite and check_non_supp():
        pass


def all_equal(elem):
    return np.all(np.diff(elem) == 0)

def check_non_supp(strat, supp):
    for i in strat :
        if i not in supp :
            pass




print(all_equal(p1))



