class BinaryDomains:
    def toBinary(self, n: int) -> str:
        """
        Convertit un entier n en un string contenant la séquence sur un octet (ou 8 bits).

        Args:
            n (int): L'entier à convertir en représentation binaire 8 bits.
        Returns:
            string: Forme binaire de l'entier en string.
        """
        return "".join(str(1 & int(n) >> i) for i in range(8)[::-1])

    def add(self, x: str, y: str) -> str:
        """
        Additionne deux séquences binaires (x+y) reçues sous la forme de string.

        Exemple : "10111001" + "10010100" = "00101101".

        Args:
            x (string): Premier élément de l'addition.
            y (string): Deuxième élément de l'addition.

        Returns:
            string: Résultat de l'addition x+y en binaire.
        """
        # BEGIN TODO
        x = int(x, 2)
        y = int(y, 2)

        res = x ^ y
        return self.toBinary(res)
        # END TODO

    def multiply(self, x: str, y: str, pol: str) -> str:
        """
        Multiplie deux séquences binaires (x*y) reçues sous la forme de string, en utilisant
        le polynôme irréductible choisi pour le corps.

        Exemple : "10111001" * "10010100" = "10110010" avec comme pol: "101001101"

        Args:
            x (string): Premier élément de la multiplication.
            y (string): Deuxième élément de la multiplication.
            pol (string): Polynome irréductible

        Returns:
            string: Résultat de la multiplication x*y en binaire.
        """
        # BEGIN TODO
        a = int(x, 2)
        b = int(y, 2)
        pol = int(pol, 2)

        mult = 0
        while b != 0:
            if (b & 1) == 1:
                mult = mult ^ a
                b ^= 1

            a <<= 1  # Multiply a by X (left shift)
            if a & (1 << 8):  # If a >= X^8, then apply modular reduction
                a ^= pol

            b >>= 1  # Divide b by X (right shift)

        return self.toBinary(mult)
        # END TODO

    def power(self, x: str, k: int, pol: str) -> str:
        # ATTENTION : Added by me

        acc = self.toBinary(1)
        for _ in range(k):
            acc = self.multiply(acc, x, pol)

        return acc

    def inverse(self, x: str, pol: str) -> str:
        """
        Inverse un élément x du corps donné (donne x^(-1)) sous la forme d'une séquence binaire.

        Exemple : ("10111001")^(-1) = "10001110" avec comme pol: "101001101"

        Args:
            x (string): Elément à inverser.
            pol (string): Polynome irréductible

        Returns:
            string: Résultat de l'inversion en binaire.
        """
        # BEGIN TODO
        b = self.toBinary(1)
        c = x

        for _ in range(7):
            c = self.multiply(c, c, pol)
            b = self.multiply(b, c, pol)

        return b
        # END TODO
