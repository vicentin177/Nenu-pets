sueldo = float(input("Ingrese el sueldo del trabajador: "))

if sueldo < 800000:
    aumento = sueldo * 0.06
    sueldo_con_aumento = sueldo + aumento
    print(f"El nuevo sueldo del trabajador es: ${sueldo_con_aumento:.2f} pesos")
else:
    print(f"El sueldo del trabajador no recibe aumento: ${sueldo:.2f} pesos")
