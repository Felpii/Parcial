import random

def main():
    print("¡Bienvenido, Adivinimenos el numero!")
       
    while True:
        try:
            max_numero = int(input("\nDigite un número maximo del rango (debe ser mayor a 1): "))
            if max_numero > 1:
                break
            else:
                print("Por favor ingresa un numero mayor a 1.")
        except ValueError:
            print("Error: Debes ingresar un numero valido.")
    
    max_intentos = max_numero // 20
    if max_intentos < 3:
        max_intentos = 3

    numero_adivinar = random.randint(1, max_numero)
    
    resultados = ["fallo"] * (max_numero + 1)
    resultados[numero_adivinar] = "acerto"
    
    print(f"\nTienes {max_intentos} intentos para adivinar el numero entre 1 y {max_numero}.")
    
    intentos = 0
    adivinado = False
    
    while intentos < max_intentos and not adivinado:
        try:
        
            intento = int(input("\nIntenta adivinar el numero: "))
            intentos += 1
            
           
            if intento < 1 or intento > max_numero:
                print(f"El numero debe estar entre 1 y {max_numero}. Intenta de nuevo.")
                continue
            
           
            if intento == numero_adivinar:
                adivinado = True
                print(f"\n¡Felicidades! Has adivinado el numero en {intentos} intentos.")
            else:
               
                if intento < numero_adivinar:
                    print("El numero a adivinar es MAYOR.")
                else:
                    print("El numero a adivinar es MENOR.")
                
                
                print(f"Te quedan {max_intentos - intentos} intentos.")
                
        except ValueError:
            intentos += 1
            print("Error: Debes ingresar un numero entero valido.")
            print(f"Te quedan {max_intentos - intentos} intentos.")
    
    if not adivinado:
        print(f"\n¡Se acabaron los intentos! El numero era {numero_adivinar}.")
    
    print("\nResultados:")
    for i in range(1, len(resultados)):
        print(f"{i}: {resultados[i]}", end=" | ")
    print("\n")

if __name__ == "__main__":
    main()
