print("------------------------------------")
print("Modificacion de datos de la clinica")
print("------------------------------------")
print("MENU")

print("1.- Cambiar numero")
print("2.- Modificar horario")
print("3.-Eliminar datos")
print("4.- Salir")
opcional = int(input(" Digite opcion->"))
if opcional==1:
    numero=int (input("Ingresa el numero de telefono nuevo  porfavor : "))
    print("Numero de telefono actualizado")
elif opcional==2:
    horario=int (input("Ingresa el nuevo horario : "))
    
elif opcional==3:
    print(" Gracias por tu servicio ,los datos han sido eliminados  ")
     
elif opcional==4:
    print("Adios")
else :
    print("Ingrese un numero correcto")