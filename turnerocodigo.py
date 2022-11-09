import time
filaTurnos = []

# ----------------------DEFINIMOS LAS FUNCIONES ----------------------
def creaTurno(nombre):
 global filaTurnos
 filaTurnos.append(nombre)
 print("creando turno")
 time.sleep(1)
 return len(filaTurnos)


def atenderPaciente(turno):
    global filaTurnos
    mostrar()
    print("llamando al paciente \n", filaTurnos[int(turno)])
    time.sleep(1)
    filaTurnos.pop(int(turno))
    print("Restan atender : ")
    mostrar()


def mostrar():
    for i in range(len(filaTurnos)):
        print(" - el paciente ", filaTurnos[i], " con el turno - ",i+1,"\n")
        time.sleep(1)
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
    if op == str(1):
        paciente = input("Ingrese el nombre del paciente ")
        id = creaTurno(paciente)
        print("El turno registrado a nombre de ",paciente," con el numero ",id)
    if op == str(2):
        mostrar()
        turn = input("Seleccione el numero de paciente ")
        turno=int(turn)
        atenderPaciente(turno-1)
    if op == str(3):
        mostrar()
    if op == str(4):
        print("Saliendo...")
        time.sleep(2)
        inicio = False
    if op != str(1) and op != str(2) and op != str(3) and op != str(4):
        print("la opcion es incorrecta, por favor reingrese su opcion con un numero del 1 al 4 \n")