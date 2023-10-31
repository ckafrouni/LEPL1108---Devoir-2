class Translation:
    def toBinary(self, n: int) -> str:
        """
        Convertit un entier n en un string contenant la séquence sur un octet (ou 8 bits).

        Args:
            n (int): L'entier à convertir en représentation binaire 8 bits.
        Returns:
            str_bin (string): Forme binaire de l'entier en string.
        """
        str_bin = "".join(str(1 & int(n) >> i) for i in range(8)[::-1])
        return str_bin

    def toInt(self, str_bin: str) -> int:
        """
        Convertit un string contenant la séquence sur un octet (ou 8 bits) en un entier n.

        Args:
            str_bin (string): Forme binaire de l'entier en string.
        Returns:
            n (int): L'entier à convertir en représentation binaire 8 bits.
        """
        n = int(str_bin, 2)
        return n

    def translateToMachine(self, phrase: str) -> list[str]:
        """
        Convertit une phrase (encodée comme un string) en une liste de strings d'octets (ou 8 bits).

        Args:
            phrase (string): Phrase en français ou en anglais.
        Returns:
            phrase_bin (list of strings): Liste de strings, chaque string représente un octet/8 bits
        """
        phrase_bin = [self.toBinary(ord(char)) for char in phrase]
        return phrase_bin

    def translateToHuman(self, bin_phrase: list[str]) -> str:
        """
        Convertit une liste de strings d'octets (ou 8 bits) en une phrase (encodée comme un string).

        Args:
            bin_phrase (list of strings): Liste de strings, chaque string représente un octet/8 bits
        Returns:
            phrase (string): Phrase en français ou en anglais.
        """
        phrase = ""
        for bin_str in bin_phrase:
            phrase += chr(self.toInt(bin_str))
        return phrase
