#!/usr/bin/env python3

# -*- coding: utf-8 -*-
import itertools
import string
import os
chemin = os.path.dirname(os.path.abspath(__file__))

def lecteur(fichier):
    """
    lit un fichier et renvoie une liste de mots"""

    if not os.path.exists(chemin):
        print("Le fichier n'existe pas!!")
        exit()
    t=[]
    with open(chemin+'/'+fichier,'r') as f:
        for i in f:
            t.append(i.strip())
    return t
def est_entier(valeur):
    """
    verifie si la valeur est un entier"""
    try:
        int(valeur) 
        return True  
    except ValueError:
        return False  

def genere_wordliste_liste(mot):
    """
    genere une wordliste a partir d'une liste de mot"""
    with open(chemin+'/'+fichier,'w') as f:
        for j in range(1, len(mot)+1):
            for i in itertools.product(mot,repeat=j):
                f.write(''.join(i)+'\n')
def wordlist_nb_caractere (nb):
    """
    genere une wordliste a partir de tous les caracteres"""
    toutcaractere = string.printable.strip()
    with open(chemin+'/'+fichier,'w') as f:
        for j in range(1, nb+1):
            for i in itertools.product(toutcaractere,repeat=j): 
                f.write(''.join(i)+'\n')
print('''
*********************************************
**Bienvenue dans le generateur de wordlist **       
*********************************************
        
        
        ''')
fichier=str(input('Entrez le nom du fichier .txt dans lequel vous enregistrez la wordlist: '))
if not os.path.exists(chemin+'/'+fichier):
    print('Le fichier existe pas!!!')
    exit()
if os.path.exists(chemin+'/'+fichier):
    typedefonction=int(input('Entre 1 si tu veux generer une wordliste a partir d une liste  de mot ou 2 si tu veux utiliser a partir de tous les caracteres? '))
    if typedefonction!=1 and typedefonction!=2:
        print('Erreur de saisie!!')
        exit()
    if typedefonction==2:
        nbmot=int(input('Entrez la taille maximal du mdp que vous voulez dans la wordlist: '))
        if est_entier(nbmot)==False:
            print('Erreur de saisie!!')
            exit()
        else:
            wordlist_nb_caractere(nbmot)
    if typedefonction==1:
        lecture=str(input('Entrez le nom du fichier .txt contenant les mots: '))
        liste=lecteur(lecture)
        if len(liste)==0:
            print('liste vide!!')
            exit()
        else:
            genere_wordliste_liste(liste)

            print('''
****************************************
*******Ta wordlist a été generee*******
****************************************
                ''')    
