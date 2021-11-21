
# Anime não encontrado
class AnimeNotFound(Exception):
    def __init__(self) -> None:
        super().__init__("Anime not found, SID invalid")

# Chave ou Valor inválido
class InvalidKeyOrValue(Exception):
    def __init__(self) -> None:
        super().__init__("Key ( or Value ) is invalid, check documentation on Github")

# Número inválido
class InvalidNumber(Exception):
    def __init__(self, value: str) -> None:
        super().__init__(f"The {value} value is invalid, enter a number greater than 1")