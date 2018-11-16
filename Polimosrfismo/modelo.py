import abc


class PersonaEquipo(metaclass=abc.ABCMeta):

    """
        Se crea la clase abstracta
    """
    # __metaclass__ = abc.ABCMeta

    def __init__(self, n):
        self.nombre=n

    def setNombre(self, n):
        self.nombre=n

    def getNombre(self):
        return self.nombre

    @abc.abstractmethod
    def entrenar():
        pass



class Futbolista(PersonaEquipo):

    def __init__(self,n):
        super(Futbolista, self).__init__(n)
        self.posicion_campo=""

    def entrenar(self):
        print("Yo %s, Futbolista, hago practica en el entrenamiento" % self.nombre)


class Entrenador(PersonaEquipo):
    def __init__(self, n):
        super(Entrenador, self).__init__(n)
        self.codigo_entrenador=""

    def entrenar(self):
        print("Yo, %s , entrenador, entreno a los jugadores "% self.nombre)


class Medico_Equipo(PersonaEquipo):
    def __init__(self, n):
        super(Medico_Equipo, self).__init__(n)
        self.titulo=""

    def entrenar(self):
        print("Yo %s, medico, atiendo a los jugadores en el entrenamiento" % self.nombre)

class Presidente(PersonaEquipo):
    def __init__(self, n):
        super(Presidente, self).__init__(n)
        self.propiedades=""

    def entrenar(self):
        print("Yo %s, presindente, pongo el dinero para el entrenamineto" % self.nombre)


e2 = Futbolista("Antonio");
e3 = Entrenador("Ramon");
e4 = Medico_Equipo("Francisco");
e5 = Presidente("Jose");

lista = (e2, e3, e4, e5)
for l in lista:
    l.entrenar()

