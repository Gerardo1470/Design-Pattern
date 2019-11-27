from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class jugadasOfensivas():
    """
    El siguiente escenario son tus jugadas disponibles el los ultimos 2 minutos del juego.
    """

    def __init__(self, estrategia: Estrategia) -> None:
        self._estrategia = estrategia

    @property
    def libroJugadas(self) -> Estrategia:
        return self._estrategia

    @libroJugadas.setter
    def libroJugadas(self, estrategia: Estrategia) -> None:
        self._estrategia = estrategia

    def jugadas_disponibles(self) -> None:  
        print("Contexto: Estas son tus jugadas dosponibles)")
        result = self._estrategia.do_algorithm(["HB run", "Hurry up offense", "Four Verticals", "Jet sweep", "Hail Mary"])
        print(",".join(result))
       
class Estrategia(ABC):
    
    @abstractmethod
    def do_algorithm(self, data: List):
        pass

class estrategiaConcretaA(Estrategia):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)

class estrategiaConcretaB(Estrategia):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))

if __name__ == "__main__":
    # El entrenador tiene sus diversas jugadas en su libro.
    # El mismo debe ser sabio al momento de elegirlas
    # para realizar la opcion correcta y sacar un buen resultado

    context = jugadasOfensivas(estrategiaConcretaA())
    print("Tip : Las jugadas estan ordenadas de mayor a menor % de efectividad")
    context.jugadas_disponibles()
    print()

    print("Precaucion : Las jugadas estan ordenadas de menor a mayor % de efectividad. Ten cuidado")
    context.libroJugadas = (estrategiaConcretaB())
    context.jugadas_disponibles()
