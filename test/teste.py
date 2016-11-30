import unittest
from poker.jogo import *
from poker.dados import *


class Test(unittest.TestCase):

    def testPoker(self):
        self.assertEqual(poker([straight_flush, quadra]),straight_flush)
        assert poker([quadra, full_house1]) == quadra

    def testPontuacao_mao(self):
        self.assertEqual(pontuacao_mao(straight_flush),10)
        assert pontuacao_mao(quadra) == 9
        assert pontuacao_mao(full_house1) == 8


    def testPegaValores(self):
        self.assertEqual(pega_valores(straight_flush), [11,10,9,8,7])

    def testPegaNaipes(self):
        self.assertEqual(pega_naipes(full_house1), ["O","E","C", "P", "E"])

    def testStraight(self):
        self.assertTrue(straight([13,12,11,10,9]))
        self.assertFalse(straight([13, 11, 11, 10, 9]))

    def testQuadra(self):
        self.assertTrue(mesmo_tipo([9,9,9,9,3],4))
        self.assertFalse(mesmo_tipo([9, 9, 9, 8, 3],4))
        self.assertFalse(mesmo_tipo([9, 9, 9, 3, 3],4))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPoker']
    unittest.main()