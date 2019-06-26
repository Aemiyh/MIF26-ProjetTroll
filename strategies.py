import random
import pickle
import numpy as np

CONF_FICHIER = False
CONF_S_OPT = []
PASC_FICHIER = False
PASC_S_OPT = []


def strategiePrudente(partie=None, partiesPrecedentes=None):
    n = partie.stockInitial
    m = partie.nombreCases
    mp = m // 2
    global CONF_FICHIER
    global CONF_S_OPT
    if not CONF_FICHIER:
        fichier = open('data/{}-{}-{}.conf'.format(50, 50, m), 'rb')
        CONF_FICHIER = True
        CONF_S_OPT = pickle.load(fichier)
    elif sorted(CONF_S_OPT.keys())[-1][2] != mp:
        fichier = open('data/{}-{}-{}.conf'.format(50, 50, m), 'rb')
        CONF_S_OPT = pickle.load(fichier)
    p1 = partie.stockGauche
    p2 = partie.stockDroite
    t = partie.positionTroll
    s_opt = list(CONF_S_OPT[p1 + 2, p2 + 2, t - mp])
    s_opt.pop()
    s_opt.pop()
    if sum(s_opt) < 1:
        s_opt[-1] += (1 - sum(s_opt))
    a = np.random.choice(np.arange(1, p1+1, 1), p=s_opt)
    return int(a)


def renvoieCinq(partie=None, partiesPrecedentes=None):
    return 5


def renvoieQuatre(partie=None, partiesPrecedentes=None):
    return 4


def renvoieTrois(partie=None, partiesPrecedentes=None):
    return 3


def renvoieDeux(partie=None, partiesPrecedentes=None):
    return 2


def renvoieUn(partie=None, partiesPrecedentes=None):
    return 1


def renvoieAlea(partie=None, partiesPrecedentes=None):
    return random.randint(1, partie.stockGauche)


def renvoieAleaMieux2(partie=None, partiesPrecedentes=None):
    if partie.stockGauche < 5:
        return partie.stockGauche
    else:
        return random.randint(1, 5)

def renvoieAleaMieux(partie=None, partiesPrecedentes=None):
    return random.randint(1, (partie.stockDroite/2))

def renvoieAleaImpair(partie=None, partiesPrecedentes=None):
    return random.randrange(1,int(partie.stockDroite),2)