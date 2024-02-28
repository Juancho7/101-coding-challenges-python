"""
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""


def reversing_chains(string: str):
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]

    return reversed_string


string = "Hello World"
print(reversing_chains(string))

string = "Hola mundo"
print(reversing_chains(string))
