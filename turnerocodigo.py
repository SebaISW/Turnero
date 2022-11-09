import time
filaTurnos = []

# ----------------------DEFINIMOS LAS FUNCIONES ----------------------
def creaTurno(nombre):
 global filaTurnos
 filaTurnos.append(nombre)
 return len(filaTurnos)


def atenderPaciente(turno):
    global filaTurnos
    mostrar()
    print("llamando al paciente ", filaTurnos[int(turno)])
    filaTurnos.pop(int(turno))
    print("Restan atender : ")
    mostrar()


def mostrar():
    for i in range(len(filaTurnos)):
        print("el paciente ", filaTurnos[i], " con el turno ",i)
inicio = True

# ---------------------- INICIAMOS EL MAIN LOOP ----------------------
while inicio :
    op = input("""Seleccione una opcion
    1 - Crear Turno
    2 - Atender paciente
    3 - Mostrar pacientes en espera
    4 - salir
""")
# ---------------------- CONDICIONAL DE OPCIONES  ----------------------
    if int(op) == 1:
        paciente = input("Ingrese el nombre del paciente ")
        id = creaTurno(paciente)
        print("El turno registrado es el ", id, "con el nombre ", paciente)
    if int(op) == 2:
        turn = input("Seleccione el numero de paciente ")
        atenderPaciente(turn)
    if int(op) == 3:
        mostrar()
    if int(op) == 4:
        print("Saliendo...")
        time.sleep(2)
        inicio = False