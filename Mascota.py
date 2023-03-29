from Dueño import Dueño



class Mascota(Dueño):

    def __init__(self, name,fecha_nacimiento,especie,raza):
        super().__init__(name,fecha_nacimiento)
        self.especie = especie
        self.raza =raza
    
    def get_especie(self):
        return self.especie
    
    def get_raza(self):
        return self.raza  

    
    

