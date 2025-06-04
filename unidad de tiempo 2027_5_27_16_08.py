# Sistema de medición de tiempo :-_ (Lanzamientos de Moneda)
# 1 unidad :-_ = 10 lanzamientos de moneda = 0.432 segundos (récord mundial: 17s/10 unidades)

import random
import time

oo_dia = input("¿Cuantos oo crees que hay al día?")
    # Si no ingresa nada, usar fecha por defecto
if not oo_dia:
        oo_dia= 24001
        print("Usando oodia por defecto: 24001")
else:
    try:
            # Parsear la fecha ingresada
            
            print(f"Fecha de oodia ingresada: {oo_dia}")
    except ValueError:
            print("Formato de oodia inválido. Usando fecha por defecto: 24001")
            oo_dia= 24001


def dibujar_sistema_tiempo():
    print()
    print("\n" + "="*50)
    print("SIMBOLOS LENGUAJE ESPAÑOL (Castellano)")
    print("[Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Ññ Oo Pp Qq Rr Ss Tt Uu Ww Xx Yy Zz]")
    print("\n" + "="*50)
    print()
    """Dibuja el sistema de tiempo con caracteres ASCII"""
    print("="*60)
    print("           SISTEMA DE TIEMPO :-_ (LANZAMIENTOS)")
    print("="*60)
    print()

        # Tamaños de moneda
    print("    TAMAÑOS DE MONEDAS  Oo:")
    print("     O ← Moneda Grande")
    print("     0 ← Moneda Grande")
    print("     • ← Moneda pequeña")
    print("     o ← Moneda pequeña")
    print()

    print("    _|||0|  OK  → 0 ← ")
    print("    _|||o|  ok  → • ← ")
    print("      👌    ok  → 0 ← ")

    print()
    print("="*60)
    print()
    
    # Dibujo de la moneda cayendo
    print(" Altural minima   H ")
    print()
    print("    SECUENCIA DE LANZAMIENTO (altura mínima para volteo)  Oo :")
    print("    ┌────────────┐")
    print("    │  BASE DE   │  ← Base de madera rígida")
    print("    │  MADERA    │    (sin imanes)")
    print("    └────────────┘")

    print()
    print()
    print("                      H     O")
    print()
    print()
    print()
    print("                     |        ")
    print("                     |      ↓  ")
    print("                    H|      _  ")
    print("                     |          ")
    print("                     |        ")
    print("                     |        ")
    print("                     ┌────────────┐")
    print()
    print("                            ||           ")
    print("                            ||           ")
    print("                           \  /           ")
    print("                            \/             ")
    print()
    print()
    print()
    print("                     |        ")
    print("                     |        ")
    print("                    H|        ")
    print("                     |          ")
    print("                     |      ↓  ")
    print("                     |      _  ")
    print("                     ┌────────────┐")
    print()
    print("                            ||           ")
    print("                            ||           ")
    print("                           \  /           ")
    print("                            \/             ")
    print()
    print("          0                                     O      ")
    print("          ↑                                     ↑      ")
    print("    ┌────────────┐                       ┌────────────┐")
    print()
    print("                            ||           ")
    print("                            ||           ")
    print("                           \  /           ")
    print("                            \/             ")
    print()
    print("          ↓                                     ↓      ")
    print("          O                                     0      ")
    print("    ┌────────────┐                       ┌────────────┐")
    print()
    print("                            ||           ")
    print("                            ||           ")
    print("                           \  /           ")
    print("                            \/             ")
    print()
    print("    ┌────────────┐                       ┌────────────┐")
    print("    │     0      │                       │     O      │ ")
    print("    │            │                       │            │ ")
    print("    └────────────┘                       └────────────┘")
    print()
    print("="*60)
    
    print()
    print()
    print("                      h     o")
    print()
    print()
    print()
    print("                     |        ")
    print("                     |      ↓  ")
    print("                    h|      -  ")
    print("                     |          ")
    print("                     |        ")
    print("                     |        ")
    print("                     ┌────────────┐")
    print()
    print("                            ||           ")
    print("                            ||           ")
    print("                           \  /           ")
    print("                            \/             ")
    print()
    print()
    print()
    print("                     |        ")
    print("                     |        ")
    print("                    h|        ")
    print("                     |          ")
    print("                     |      ↓  ")
    print("                     |      -  ")
    print("                     ┌────────────┐")
    print()
    print("                            ||           ")
    print("                            ||           ")
    print("                           \  /           ")
    print("                            \/             ")
    print()
    print("          •                                     o      ")
    print("          ↑                                     ↑      ")
    print("    ┌────────────┐                       ┌────────────┐")
    print()
    print("                            ||           ")
    print("                            ||           ")
    print("                           \  /           ")
    print("                            \/             ")
    print()
    print("          ↓                                     ↓      ")
    print("          o                                     •      ")
    print("    ┌────────────┐                       ┌────────────┐")
    print()
    print("                            ||           ")
    print("                            ||           ")
    print("                           \  /           ")
    print("                            \/             ")
    print()
    print("    ┌────────────┐                       ┌────────────┐")
    print("    │     •      │                       │     o      │ ")
    print("    │            │                       │            │ ")
    print("    └────────────┘                       └────────────┘")

    print()
    print()
    print()
    print("="*60)
    print()


    print("    SECUENCIA =  RECOGER -> LEVANTAR -> DEJAR CAER -> NO MOVIL -> RECOGER  ")
    print()
    print("="*60)
    print()
    print("    NO MOVIL   ")
    print()
    print("0               0s")
    print("    -------─------")
    print()
    print()
    print("          ||           ")
    print("          ||           ")
    print("         \  /           ")
    print("          \/             ")
    print()
    print()
    print()
    print("    RECOGER")
    print("0               █s")
    print()
    print("      -👌    ")
    print("    ┌────────────┐")
    print()
    print()
    print("          ||           ")
    print("          ||           ")
    print("         \  /           ")
    print("          \/             ")
    print()
    print()
    print()
    print("    LEVANTAR")
    print("0                █s")
    print()
    print("      -👌     ")
    print("   |   ↑       ")
    print("   |           ")
    print("  H|           ")
    print("   |           ")
    print("   |           ")
    print("    ┌────────────┐")
    print()
    print()
    print("          ||           ")
    print("          ||           ")
    print("         \  /           ")
    print("          \/             ")
    print()
    print()
    print()
    print("    DEJAR CAER")
    print()
    print("0                █s")
    print("           ")
    print("      🫴     ")
    print("   |           ")
    print("   |           ")
    print("  H|           ")
    print("   |           ")
    print("   |           ")
    print("    ┌────────────┐")
    print()
    print() 
    print("          ||           ")
    print("          \/             ")
    print()
    print()
    print("0               █s")
    print()
    print("           ")
    print("      ✋     ")
    print("           _     ")
    print("   |           ")
    print("   |           ")
    print("  H|           ")
    print("   |           ")
    print("   |           ")
    print("    ┌────────────┐")
    print()
    print()
    print("          ||           ")
    print("          \/             ")
    print()
    print()
    print("0               █s")
    print()
    print("      🖐️     ")
    print("   |      ↓")
    print("   |      _")   
    print("  H|        ")
    print("   |      ")
    print("   |      ")
    print("    ┌────────────┐")
    print()
    print()
    print("          ||           ")
    print("          \/             ")
    print()
    print()
    print("0               █s")
    print()
    print("      🖐️     ")
    print("   |      ")
    print("   |      ")   
    print("  H|        ")
    print("   |      ↓")
    print("   |      _")  
    print("    ┌────────────┐")
    print()
    print()
    print("          ||           ")
    print("          ||           ")
    print("         \  /           ")
    print("          \/             ")
    print()
    print()
    print("    NO MOVIL   ")
    print()
    print("1               █s")
    print("    -------─------")
    print()
    print()
    print("          ||           ")
    print("          ||           ")
    print("         \  /           ")
    print("          \/             ")
    print()
    print()
    print()
    print("    RECOGER")
    print("1               █s")
    print()
    print("      -👌    ")
    print("    ┌────────────┐")
    print()
    print()
    print("          ||           ")
    print("          ||           ")
    print("         \  /           ")
    print("          \/             ")
    print()
    print()
    print()
    print("    LEVANTAR")
    print("1               █s")
    print()
    print("      -👌     ")
    print("   |   ↑       ")
    print("   |           ")
    print("  H|           ")
    print("   |           ")
    print("   |           ")
    print("    ┌────────────┐")
    print()
    print()
    print("          ||           ")
    print("          ||           ")
    print("         \  /           ")
    print("          \/             ")
    print()
    print()
    print()
    print("    DEJAR CAER")
    print()
    print("1               █s")
    print("           ")
    print("      🫴     ")
    print("   |           ")
    print("   |           ")
    print("  H|           ")
    print("   |           ")
    print("   |           ")
    print("    ┌────────────┐")
    print()
    print() 
    print("          ||           ")
    print("          \/             ")
    print()
    print()
    print("1               █s")
    print()
    print("           ")
    print("      ✋     ")
    print("           _     ")
    print("   |           ")
    print("   |           ")
    print("  H|           ")
    print("   |           ")
    print("   |           ")
    print("    ┌────────────┐")
    print()
    print()
    print("          ||           ")
    print("          \/             ")
    print()
    print()
    print("1             █s")
    print()
    print("      🖐️     ")
    print("   |      ↓")
    print("   |      _")   
    print("  H|        ")
    print("   |      ")
    print("   |      ")
    print("    ┌────────────┐")
    print()
    print()
    print("          ||           ")
    print("          \/             ")
    print()
    print()
    print("1             █s")
    print()
    print("      🖐️     ")
    print("   |      ")
    print("   |      ")   
    print("  H|        ")
    print("   |      ↓")
    print("   |      _")  
    print("    ┌────────────┐")
    print()
    print()
    print()
    print()
    print("          ||           ")
    print("          ||           ")
    print("         \  /           ")
    print("          \/             ")
    print()
    print()
    
    print("   .     ")
    print("   .     ")
    print("   .     ")
    print("   .     ")
    print()
    print()
    print("█              █s")
    print()
    print()
    print("   .     ")
    print("   .     ")
    print("   .     ")
    print("   .     ")
    print()
    print()
    print("10              17s")
    print()
    print()
    print()
    print()
    print("="*60)    
    

    
    # Conversiones
    print()
    print("="*60)
    print()
    print("     SIMBOLOS UNIDADES NUMERICAS")
    print()
    print("     [0][1 2 3 4 5 6 7 8 9 10]")
    print("     [11 12 13 14 15 16 17 18 19 20]")
    print()
    print("="*60)
    print()
    print("    UNIDADES DE TIEMPO ENTRE oo")
    print()
    print()
    print("    • 1 oo (sol) = 24 horas (h)")
    print("    • 1 h = 60 mintuos (m)")
    print("    • 60 m = 60 segundos (s)")
    print("    • 1 oo = 1440 m ")
    print("    • 1 oo = 86400 s ")
    print("    • 1 h = 3600 s")
    print()
    print("="*60) 
    print()
    print("    CONVERSIONES:")
    print()
    print()
    print("    • Récord mundial: 17 segundos = 10 secuencias ")
    print("    • 10 secuencias = 17 segundos")
    print("    • 1 secuencia = 1.7 segundos")
    print("    • 5.882359 secuencias = 10 segundos (s)")
    print("    • 10 :-_ = 4.32 segundo (s)")
    print("    • 43.2 segundos = 100 :-_ ")
    print("    • 2.31481481 :-_ = 1 segundo")
    print("    • 86400 segundos = 200000 :-_ ")
    print("    • 1 oo = 20 : = 86400 s ")
    print("    • 1 : = 100 :- = 4320 s ")
    print("    • 1 :- = 100 :-_ = 43,2 s ")
    print("    • 1 : = 10000 :-_ = 4320 s ")
    print("    • 1 :-_ = 0.432 segundo (s)")
    print()
    print()
    print("="*60)

def convertir_tiempo(valor, desde, hacia):
    """Convierte entre unidades de tiempo :-_ y segundos"""
    factor_conversion1 = 0.432  # 1 :-_ = 0.432 segundos
    factor_conversion2 = 2.31481481  # 1 segundos = 2.31481481 :-_
    factor_conversion3 = 1/60 # 1 segundo = 1/60 minuto
    factor_conversion4 = 60 # 60 segundos = 1 minuto
    factor_conversion5 = 1/60 # 1 minuto = 1/60 hora
    factor_conversion6 = 60 # 60 minutos = 1 hora
    factor_conversion7 = 24 # 24 horas = 1 oo 
    factor_conversion8 = oo_dia # 1 dia = 24001 oo (hasta nuevas noticias)**
    factor_conversion9 = 365.25 # 365.25 dias = 1 año 
    factor_conversion10 = 1/60 # 1 segundo = 1/60 minuto
    factor_conversion11 = 60 # 60 segundos = 1 minuto
    factor_conversion12 = 1/60 # 1 minuto = 1/60 hora
    factor_conversion13 = 60 # 60 minutos = 1 hora
    factor_conversion14 = 24 # 24 horas = 1 oo 
    factor_conversion15 = oo_dia # 1 dia = 24001 oo (hasta nuevas noticias)**
    factor_conversion16 = 365.25 # 365.25 dias = 1 año **
    
    
    if desde == ":-_" and hacia == "segundos":
        return valor * factor_conversion2
    elif desde == "segundos" and hacia == ":-_":
        return valor * factor_conversion1
    elif desde == "segundos" and hacia == ":":
        return valor * factor_conversion2
    elif desde == ":" and hacia == "segundos":
        return valor * factor_conversion2
    elif desde == "segundos" and hacia == ":-":
        return valor * factor_conversion2
    elif desde == ":-" and hacia == "segundos":
        return valor * factor_conversion2
    else:
        return valor

def simular_lanzamientos(num_unidades=1):
    """Simula lanzamientos de moneda para medir tiempo"""
    print(f"\n🪙 SIMULANDO {num_unidades} UNIDAD(ES) :-_ ({num_unidades * 10} LANZAMIENTOS)")
    print("-" * 50)
    
    total_lanzamientos = num_unidades * 10
    tiempo_total_segundos = num_unidades * 0.432
    
    for unidad in range(num_unidades):
        print(f"\n📊 Unidad :-_ #{unidad + 1}:")
        
        for lanzamiento in range(10):
            # Simular resultado (cara o cruz)
            resultado = "○" if random.choice([True, False]) else "●"
            print(f"   Lanzamiento {lanzamiento + 1:2d}: {resultado}")
            time.sleep(0.05)  # Pequeña pausa para efecto visual
    
    print(f"\n✅ COMPLETADO:")
    print(f"   • Total lanzamientos: {total_lanzamientos}")
    print(f"   • Tiempo en :-_: {num_unidades}")
    print(f"   • Tiempo en segundos: {tiempo_total_segundos:.3f}s")
    print(f"   • A récord mundial: {tiempo_total_segundos:.3f}s")

def calculadora_tiempo():
    """Calculadora para conversiones de tiempo"""
    print("\n🧮 CALCULADORA DE TIEMPO :-_")
    print("-" * 30)
    
    while True:
        print("\n1. Convertir :-_ a segundos")
        print("2. Convertir segundos a :-_")
        print("3. Calcular lanzamientos por segundo")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción (1-4): ")
        
        if opcion == "1":
            valor = float(input("Ingresa unidades :-_: "))
            resultado = convertir_tiempo(valor, ":-_", "segundos")
            print(f"{valor} :-_ = {resultado:.6f} segundos")
            
        elif opcion == "2":
            valor = float(input("Ingresa segundos: "))
            resultado = convertir_tiempo(valor, "segundos", ":-_")
            print(f"{valor} segundos = {resultado:.6f} :-_")
            
        elif opcion == "3":
            lanzamientos_por_segundo = 10 / 0.432
            print(f"Velocidad récord: {lanzamientos_por_segundo:.3f} lanzamientos/segundo")
            
        elif opcion == "4":
            break
        else:
            print("Opción no válida")

def mostrar_ejemplos():
    """Muestra ejemplos de conversión"""
    print("\n📋 EJEMPLOS DE CONVERSIÓN:")
    print("-" * 25)
    
    ejemplos = [
        (1, ":-_"),
        (10, ":-_"),
        (60, "segundos"),
        (1, "segundos"),
        (17, "segundos")  # Récord mundial
    ]
    
    for valor, unidad in ejemplos:
        if unidad == ":-_":
            segundos = convertir_tiempo(valor, ":-_", "segundos")
            lanzamientos = valor * 10
            print(f"   {valor:3.0f} :-_ = {segundos:8.3f}s = {lanzamientos:3.0f} lanzamientos")
        else:
            tiempo_especial = convertir_tiempo(valor, "segundos", ":-_")
            lanzamientos = tiempo_especial * 10
            print(f"   {valor:3.0f}s = {tiempo_especial:8.3f} :-_ = {lanzamientos:6.1f} lanzamientos")

# Programa principal
if __name__ == "__main__":
    # Dibujar el sistema
    dibujar_sistema_tiempo()
    
    # Mostrar ejemplos
    mostrar_ejemplos()
    
    # Simular algunos lanzamientos
    simular_lanzamientos(2)
    
    # Calculadora interactiva
    calculadora_tiempo()