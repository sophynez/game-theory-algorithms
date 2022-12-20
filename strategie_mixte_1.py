import numpy as np

'''
to do :
stratégie pure :
- pareto optimum
- equilibre de nash

strategie mixte :
- support [ DONE ]
- paiement [ DONE ]
- utilité [ DONE ]

TP 2 : 
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
print("--> Enumeration des support du joueur 1 :")
print(f'*  {supp1}')
print(f'* :: hors support  : {non_supp1}')
print("--> Enumeration des support du joueur 2 :")
print(f'*  {supp2}')
print(f'* :: hors support  :  {non_supp2}')

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

p1_u = return_paiement(sig2, 0, 1)
p1_d = return_paiement(sig2, 1, 1)
p1_m = return_paiement(sig2, 2, 1)

print("--> les paiement du joueur 1 :")
print(f'* strategie U {p1_u}')
print(f'* strategie D {p1_d}')
print(f'* strategie M {p1_m}')

print(f' Les paiements du joueurs 2' )
p2_l = return_paiement(sig1, 0, 2)
p2_m = return_paiement(sig1, 1, 2)
p2_r = return_paiement(sig1, 2, 2)

print(f'* strategie L {p2_l}')
print(f'* strategie M {p2_m}')
print(f'* strategie R {p2_r}')

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


print(f' --> Utilité joueur 1 :: {return_utilite(p1, sig1)}')
print(f' --> Utilité joueur 2 :: {return_utilite(p2, sig2)}')

## indifference au support : (sig1, sig2) est-il un equilibre de Nash ???

'''
* pour tous les joueurs, les paiements de chacune de leurs strategie sont egaux
* pour tous les joueurs, les paimenents dechacune de leurs tratégie n'appartenant pas au support sont egaux
'''


def check_paiement(p):
    return np.all(np.diff(p) == 0)

def get_paiement_strat_hors_supp(strat, supp, p):
    map = dict(zip(strat, p))
    pshs = []
    for i in strat :
        if i not in supp:
            pshs.append(i)
    return pshs
l1 = get_paiement_strat_hors_supp(strat1, supp1, p1)
l2 = get_paiement_strat_hors_supp(strat2, supp2, p2)

if check_paiement(p1) and check_paiement(p2) and check_paiement(l1) and check_paiement(l2) :
    print("(sig1, sig2) equilibre de Nash")
else :
    print("(sig1, sig2) n'est pas un equilibre de Nash")







