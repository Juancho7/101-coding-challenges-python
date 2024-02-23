"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""


def is_anagram(word1, word2):
    if word1 == word2:
        return False

    letters1 = list(word1)
    letters2 = list(word2)

    letters1.sort()
    letters2.sort()

    if letters1 != letters2:
        return False

    return True


word1 = "cinema"
word2 = "iceman"
print(is_anagram(word1, word2))

word1 = "dog"
word2 = "house"
print(is_anagram(word1, word2))

word1 = "roma"
word2 = "amor"
print(is_anagram(word1, word2))
