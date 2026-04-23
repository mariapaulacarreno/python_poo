from persona import Persona

juan = Persona("Juan", "Castellanos", 15)
juan.mostrarPersona()

leidy = Persona("Leidy", "Alvarez", 18)
leidy.mostrarPersona()

leidy.apellido = "Perez"
leidy.mostrarPersona()

juan = leidy

juan.mostrarPersona()
