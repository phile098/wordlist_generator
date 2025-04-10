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
def genere_code_pin(nbmin,nbmax):
    """
    genere une wordliste a partir de tous les caracteres"""
    toutchiffre =['0','1','2','3','4','5','6','7','8','9']
    with open(chemin+'/'+fichier,'w') as f:
        for j in range(nbmin, nbmax+1):
            for i in itertools.product(toutchiffre,repeat=j): 
                f.write(''.join(i)+'\n')
def genere_wordliste_liste(mot):
    """
    genere une wordliste a partir d'une liste de mot"""
    with open(chemin+'/'+fichier,'w') as f:
        for j in range(1, len(mot)+1):
            for i in itertools.product(mot,repeat=j):
                f.write(''.join(i)+'\n')
def wordlist_nb_caractere (nb,minimum):
    """
    genere une wordliste a partir de tous les caracteres"""
    toutcaractere = string.printable.strip()
    with open(chemin+'/'+fichier,'w') as f:
        for j in range(minimum, nb+1):
            for i in itertools.product(toutcaractere,repeat=j): 
                f.write(''.join(i)+'\n')
print('''
************************************************************
***Bienvenue dans le generateur de wordlist              ***      
************************************************************
***Auteur: phile098                                      ***
***Version: 1.0                                          ***
***git:https://github.com/phile098/wordlist_generator.git***
***Ce programme est un generateur de wordlist a partire: ***       
***      - de tous les caracteres                        ***
***      - de tous les mots d un fichier                 ***
***      - de tous les chiffres                          ***
***près requis:python3 eet un fichier txt dans le dossier***     
************************************************************
        ''')
fichier=str(input('Entrez le nom du fichier .txt dans lequel vous enregistrez la wordlist: '))
if not os.path.exists(chemin+'/'+fichier):
    print('Le fichier existe pas!!!')
    exit()
if os.path.exists(chemin+'/'+fichier):
    typedefonction=int(input('Entre 1 si tu veux generer une wordliste a partir d une liste  de mot \n 2 si tu veux utiliser a partir de tous les caracteres \n 3 si tu veux generer un code pin \n Entrer votre choix: '))
    if typedefonction!=1 and typedefonction!=2  and typedefonction!=3:
        print('Erreur de saisie!!')
        exit()
    if typedefonction==3:
        minimum=int(input('Entrez la taille minimum du code pin que vous voulez dans la wordlist:'))
        nbmax=int(input('Entrez la taille maximal du code pin que vous voulez dans la wordlist: '))
        if est_entier(nbmax)==False and est_entier(minimum)==False:
            print('Erreur de saisie!!')
            exit()
        else:
            genere_code_pin(nbmax,minimum)
            print('''
****************************************
*******Ta wordlist a été generee*******
****************************************
                ''')  
    if typedefonction==2:
        minimum=int(input('Entrez la taille minimum du mdp que vous voulez dans la wordlist:'))
        nbmot=int(input('Entrez la taille maximal du mdp que vous voulez dans la wordlist: '))
        if est_entier(nbmot)==False and est_entier(minimum)==False:
            print('Erreur de saisie!!')
            exit()
        else:
            wordlist_nb_caractere(nbmot,minimum)
            print('''
****************************************
*******Ta wordlist a été generee*******
****************************************
                ''')  
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
