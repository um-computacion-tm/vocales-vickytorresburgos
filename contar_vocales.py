import unittest

def vocal_counter(word: str) -> dict:
    vocales = {}
    for letter in word:
        if letter in ('a', 'e', 'i', 'o', 'u'):
            vocales[letter] = 1 + vocales.get(letter, 0)
    return vocales

def vocal_counter_des(word: str):
    resultado = vocal_counter(word)
    return \
        resultado.get('a', 0), \
        resultado.get('e', 0), \
        resultado.get('i', 0), \
        resultado.get('o', 0), \
        resultado.get('u', 0)


class TestVocales(unittest.TestCase):

    def test_caso_algunas_vocales(self):
        esperado = {
            'a': 5,
            'e': 1,
            'u': 1,
        }
        resultado = vocal_counter("aca hay una frase")
        self.assertDictEqual(resultado, esperado)

    def test_caso_tupla1(self):
        ca, ce, ci, co, cu = vocal_counter_des("ursula")
        resultado = (ca, ce, ci, co, cu)
        self.assertEqual(resultado, (1, 0, 0, 0, 2))

    def test_caso_todas_las_vocales(self): #euforia
        esperado ={
            'a':1,
            'e':1,
            'i':1,
            'o':1,
            'u':1
        }
        resultado = vocal_counter('euforia')
        self.assertDictEqual(resultado, esperado)

    def test_caso_tupla2(self):
        ca, ce, ci, co, cu = vocal_counter_des("euforia")
        resultado = (ca, ce, ci, co, cu)
        self.assertEqual(resultado, (1, 1, 1, 1, 1))


if __name__ == '__main__':
    unittest.main()