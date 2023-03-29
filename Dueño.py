
class Dueño:

#
#
#
    def __init__(self,name,fecha_nacimiento):
       self.name = name
       self.fecha_nacimiento = fecha_nacimiento
      

        
    def get_name(self):
        return self.name
    
    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    
    def set_name(self,nuevo_nombre):
        self.name=nuevo_nombre
    
    def set_fecha_nacimiento(self,nueva_fecha):
        self.fecha_nacimiento =nueva_fecha
    