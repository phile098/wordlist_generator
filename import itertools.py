import itertools
import string


def genere_wordliste_liste(mot):
    with open('/home/phile/Documents/hashes/mdp.txt','w') as f:
        for j in range(1, len(mot)+1):
            for i in itertools.product(mot,repeat=j):
                f.write(''.join(i)+'\n')
genere_wordliste_liste(mot)
def wordlist_nb_caractere_et_liste (nb,mots):
    toutcaractere = string.printable.strip()+mots
    print(toutcaractere)
    print(len(toutcaractere))
    with open('/home/phile/Documents/hashes/mdp.txt','w') as f:
        for j in range(1, nb+1):
            for i in itertools.product(toutcaractere,repeat=j): 
                f.write(''.join(i)+'\n')
wordlist_nb_caractere_et_liste(4,'')
