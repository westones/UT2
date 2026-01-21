
def operaciones(a, b):
    resultado_intermedio = a * 2
    resultado_intermedio_2 = resultado_intermedio*10
    resultado_final = resultado_intermedio + b + resultado_intermedio_2
    return resultado_final

# Punto de ruptura en la línea siguiente
p1 = int(input("Introduce el primer operando: "))
p2 = int(input("Introduce el segundo operando: "))
resultado_operacion = operaciones(p1, p2)

# Expresión y watch para observar el valor de 'resultado_intermedio'
print("Resultado final:", resultado_operacion)