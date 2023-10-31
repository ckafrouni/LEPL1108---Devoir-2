from functools import reduce
import numpy

from binary_domains import BinaryDomains
from translation import Translation


class ReedSolomon:
    def __init__(self, k: int, n: int, y: list[str], pol: str):
        """
        Args:
            k (int): dimension des messages à transmettre.
            n (int): taille du bloc que l'on souhaite transmettre.
            y (liste de string de taille n): les points d'interpolation yi.
            pol (string): polynome irréductible.
        """
        self.f = BinaryDomains()
        self.t = Translation()
        self.k = k
        self.n = n
        self.y = y
        self.pol = pol

    def _evaluate(self, polynome: list[str], x: str) -> str:
        """
        Evalue le polynome A(x) au point x

        Args:
            polynome (liste de strings (octets) de taille k): le polynome
            x (string): point d'évaluation
        Returns:
            (string): la valeur du polynome en x
        """
        y = polynome[-1]
        for i in range(len(polynome) - 2, -1, -1):
            y = self.f.add(self.f.multiply(y, x, self.pol), polynome[i])
        return y

    def encoding(self, message_original: str) -> list[str]:
        """
        Encode le message à stocker sous la forme d'une liste comportant n bytes/octets.

        Args:
            message_original (string): Le message original a encodé.

        Returns:
            (liste de string de taille n): Le message encodé.
        """
        message_original_bin = self.t.translateToMachine(message_original)
        res = list(map(lambda x: self.f.toBinary(0), range(self.n)))

        for i, Y_i in enumerate(self.y):
            tmp = self.f.toBinary(0)
            for j, bc in enumerate(message_original_bin):
                tmp = self.f.add(tmp, self.f.multiply(bc, self.f.power(Y_i, j, self.pol), self.pol))
            res[i] = tmp

        return res
    
    def gaussian_elimination(self, y: list[str], I: list[str]) -> list[str]:
        """
        Ex: k = 4: retourne les coefficients (ai) du polynôme A(Y) = a0 + a1*Y + a2*Y^2 + a3*Y^3
        en partant de 4 points (yi,A(yi)) = (yi,Ii).

        Ce problème est généralisé pour tout k.
        Pour le résoudre -> Effectuer l'élimination de Gauss-Jordan sur le système Va = I.
        Avec V la matrice de Vandermonde.

        Args:
            y (liste de string de taille k): Les points yi.
            I (liste de string de taille k): Les points Ii=A(yi).

        Returns:
            (liste de string de taille k): Les coefficients (ai) de l'interpolation.
        """
        # BEGIN TODO
        return []
        # END TODO

    def decoding(self, message_corrupted: list[str]) -> (bool, list[str]):
        """
        Décode le message corrompu sous la forme d'une liste comportant k bytes.

        Args:
            message_corrupted (liste de string de taille n): Le message 'corrompu' reçu.

        Returns:
            (bool): True s'il est possible de décoder le message corrompu, False sinon.
            (liste de string de taille k): Le message décodé. (si bool = False, alors retourner []).
        """
        # BEGIN TODO
        return False, []
        # END TODO
