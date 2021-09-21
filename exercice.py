#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number > 0:
        return number
    elif number < 0:
        return -number
    else:
        return "0"
    


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    list = []
    for letter in prefixes:
        list.append(letter + suffixe)
    return list
        


def prime_integer_summation() -> int:
    summation = 0
    for prime_number in range(2, 100):
        for any_number in range(2, prime_number):
            if prime_number % any_number == 0:
                break
        else: 
            summation += prime_number
    
    return summation


def factorial(number: int) -> int:
    nb_factorial = 1
    first_integer = 1
    while first_integer < number:
        first_integer +=1
        nb_factorial = nb_factorial * first_integer
        
    return nb_factorial


def use_continue() -> None:
    for integer in range (1, 11):
        if integer == 5:
            continue
        print (integer)



def verify_ages(groups: List[List[int]]) -> List[bool]:
    groups_unk = []
    
    for ages in groups:
        for number in range(0,100):
            if len(groups[number]) > 10 or len(groups[number]) < 3: 
 #               groups_unk += groups[number] #      return f"pas acceptable {groups_unk}"
                continue
        for age_number in ages:
            if age_number < 18 :
                continue
            elif age_number > 70 and age_number == 50:
                continue
        else:
            if age_number == 25:
                return groups


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
