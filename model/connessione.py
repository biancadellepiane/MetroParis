from dataclasses import dataclass


@dataclass
class Connessione:
    id_connessione: int
    id_linea: int
    id_stazP: int
    id_stazA: int

    #con hashable rendo univoco, in questo caso su id_connessione
    def __hash__(self):
        return hash(self.id_connessione)

    #serve per dire come eguagliare
    def __eq__(self, other):
        return self.id_connessione == other.id_connessione
