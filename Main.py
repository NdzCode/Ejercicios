from Mascota import Mascota
from Dueño import Dueño

Nicolas=Dueño("Nicolas","15 de enero")
Nieve=Mascota("Nieve","12 de abril","Canis lupus familiaris","Braco aleman") 
    
def main(Nicolas, Nieve):
    return f'El Nombre del Dueño es {Nicolas.get_name()}, su fecha de nacimiento es el {Nicolas.get_fecha_nacimiento()}, nombre de la mascota es {Nieve.get_name()}, fecha de nacimiento  {Nieve.get_fecha_nacimiento()}, pertenece a la especie {Nieve.get_especie()} de la raza {Nieve.get_raza()}'


if __name__ == '__main__':
    
    print(main(Nicolas,Nieve))