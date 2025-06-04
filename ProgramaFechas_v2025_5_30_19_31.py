from datetime import datetime, date, timedelta

a1 = 0000000000
b1 = 9999999999
dias_year = 365.25


# Función alternativa más eficiente para búsqueda específica
def jueguecito():
    # Solicitar fecha de nacimiento
    print("\nIngrese ingrese un valor para conocer el resultado de ese valor * la constante 1.111111:")
    fecha_input = input("Formato DD/MM/AAAA (presione Enter para usar 06/12/1982): ").strip()
    print("\nIngrese su fecha de primera edad:")
    fecha_input2 = input("Formato DD/MM/AAAA (presione Enter para usar 06/12/1987): ").strip()


def calculadora_dias():
    # Obtener la fecha de hoy
    fecha_hoy = date.today() #date(2025, 5, 26)
    print(f"Fecha de hoy: {fecha_hoy.strftime('%d/%m/%Y')}")
    
    # Solicitar fecha de nacimiento
    print("\nIngrese su fecha de nacimiento:")
    fecha_input = input("Formato DD/MM/AAAA (presione Enter para usar 06/12/1982): ").strip()
    print("\nIngrese su fecha de primera edad:")
    fecha_input2 = input("Formato DD/MM/AAAA (presione Enter para usar 06/12/1987): ").strip()


    # Si no ingresa nada, usar fecha por defecto
    if not fecha_input:
        fecha_nacimiento = date(1982, 12, 6)
        print("Usando fecha por defecto: 06/12/1982")
    else:
        try:
            # Parsear la fecha ingresada
            fecha_nacimiento = datetime.strptime(fecha_input, "%d/%m/%Y").date()
            print(f"Fecha de nacimiento ingresada: {fecha_nacimiento.strftime('%d/%m/%Y')}")
        except ValueError:
            print("Formato de fecha inválido. Usando fecha por defecto: 06/12/1982")
            fecha_nacimiento = date(1982, 12, 6)

    # Si no ingresa nada, usar fecha por defecto
    if not fecha_input2:
        fecha_nacimiento2 = date(1987, 12, 6)
        print("Usando fecha por defecto: 06/12/1987")
    else:
        try:
            # Parsear la fecha ingresada
            fecha_nacimiento2 = datetime.strptime(fecha_input2, "%d/%m/%Y").date()
            print(f"Fecha de nacimiento ingresada: {fecha_nacimiento2.strftime('%d/%m/%Y')}")
        except ValueError:
            print("Formato de fecha inválido. Usando fecha por defecto: 06/12/1987")
            fecha_nacimiento2 = date(1987, 12, 6)
    
    # Validar que la fecha de nacimiento no sea en el futuro

    fecha_nacimiento3 = fecha_nacimiento2


    if fecha_nacimiento2 > fecha_hoy:
        print("⚠️  Error: La fecha de nacimiento no puede ser en el futuro. Usando fecha por defecto.")
        fecha_nacimiento3 = date(1982, 12, 6)
    
    # Calcular días desde la fecha de nacimiento hasta hoy
    diferencia = fecha_hoy - fecha_nacimiento3
    dias_transcurridos = diferencia.days
    #print(dias_transcurridos1)
    #dias_transcurridos = dias_transcurridos1 -365.25*4

    print(dias_transcurridos)
    
    print(f"\nDías transcurridos desde el nacimiento hasta hoy: {dias_transcurridos} días")
    
    # NUEVA FUNCIONALIDAD: Calcular fecha restando 6000 días a la fecha actual
    fecha_menos_6000_dias = fecha_hoy - timedelta(days=6000)
    print(f"\n📅 Fecha hace 6000 días (restando 6000 días a hoy): {fecha_menos_6000_dias.strftime('%d/%m/%Y')}")
    
    # Calcular diasoo: (días transcurridos * 24001) + 1
    diasoo = (dias_transcurridos * 24001) + 1

    oo_perdidos = diasoo - dias_transcurridos
    oo_perdidos_porcentaje = oo_perdidos * 100 / diasoo
    oo_sin_coma_porcentaje = 100 - oo_perdidos_porcentaje
    
    print(f"\nResultado oo's: {diasoo:,} oo")
    print(f"Fórmula utilizada: ({dias_transcurridos} × 24001) + 1 = {diasoo:,} oo")

    print(f"\nResultado oo's perdidos: {oo_perdidos:,} oo")
    print(f"\nResultado oo's perdidos en porcentaje: {oo_perdidos_porcentaje:,} oo / 100")
    print(f"\nResultado oo's no en coma inducido en porcentaje: {oo_sin_coma_porcentaje:,} oo / 100")
    
    
    print("\n" + "="*50)
    print("SIMBOLOS LENGUAJE ESPAÑOL (Castellano)")
    print("[Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Ññ Oo Pp Qq Rr Ss Tt Uu Ww Xx Yy Zz]")
    print("\n" + "="*50)
    print("SIMBOLOS UNIDADES NUMERICAS")
    print("[0][1 2 3 4 5 6 7 8 9 10]")
    print("[11 12 13 14 15 16 17 18 19 20]")
    print("\n" + "="*50)
    print("UNIDADES DE TIEMPO ENTRE oo")
    print("1 oo (sol) = 24 horas (h)")
    print("1 h = 60 mintuos (m)")
    print("60 m = 60 segundos (s)")
    print("1 oo = 1440 m ")
    print("1 oo = 86400 s ")
    print("1 h = 3600 s")
    print("\n" + "="*50)
    print("PROPUESTA UNIDAD DE TIEMPO")







    print("\n" + "="*50)
    print("Buscando números que cumplan la condición...")

    oo_year = 24001 * dias_year

    # Límites del rango
    a = a1
    b = b1

    # Variables para detectar grupos
    grupos_encontrados = []
    grupo_actual = []
    numeros_totales = 0
    max_numeros = 200000000

    print(f"Rango a analizar: {a:,} - {b:,}")
    print("="*50)

    # Bucle principal
    for c in range(a, b + 1):
        # Cálculos optimizados
        d = ((((c / oo_year) - 100) * oo_year) - 1) / 24001
        e = d - dias_transcurridos
        f = round(e)
        
        if f == 0:
            # Número cumple la condición
            grupo_actual.append(c)
            numeros_totales += 1
            
            # Limitar resultados
            if numeros_totales >= max_numeros:
                print(f"... (limitado a {max_numeros} resultados)")
                break
        else:
            # Si hay un grupo actual y el número no cumple, cerrar el grupo
            if grupo_actual:
                grupos_encontrados.append(grupo_actual.copy())
                grupo_actual = []
        
        # Mostrar progreso cada millón de iteraciones
        if (c - a) % 1000000 == 0 and c != a:
            progreso = ((c - a) / (b - a)) * 100
            print(f"Progreso: {progreso:.1f}% - Revisando: {c:,} - Grupos encontrados: {len(grupos_encontrados)}")

    # No olvidar el último grupo si termina al final del rango
    if grupo_actual:
        grupos_encontrados.append(grupo_actual)

    # Mostrar resultados
    print("="*50)
    print("RESULTADOS:")
    print("="*50)

    if not grupos_encontrados:
        print("❌ No se encontraron números que cumplan la condición en el rango especificado.")
    else:
        print(f"🎯 Total de grupos encontrados: {len(grupos_encontrados)}")
        print(f"🎯 Total de números encontrados: {numeros_totales}")
        print()
        
        for i, grupo in enumerate(grupos_encontrados, 1):
            primer_numero = grupo[0]
            ultimo_numero = grupo[-1]
            cantidad = len(grupo)
            
            print(f"📊 GRUPO {i}:")
            print(f"   ├─ Primer número: {primer_numero:,}")
            print(f"   ├─ Último número: {ultimo_numero:,}")
            print(f"   ├─ Cantidad: {cantidad:,} números")
            if cantidad > 1:
                print(f"   └─ Rango: {primer_numero:,} - {ultimo_numero:,}")
            else:
                print(f"   └─ Número único")
            print()

    print("="*50)
    # Devolver valores por si se necesitan para cálculos adicionales
    return {
        'fecha_hoy': fecha_hoy,
        'fecha_nacimiento': fecha_nacimiento,
        'fecha_primera_edad': fecha_nacimiento2,
        'dias_transcurridos': dias_transcurridos,
        'fecha_menos_6000_dias': fecha_menos_6000_dias,
        'diasoo': diasoo,
        #'numeros_encontrados': numeros_encontrados
    }

# Función alternativa más eficiente para búsqueda específica
def busqueda_optimizada(dias_transcurridos, rango_inicio=a1, rango_fin=b1):
    """
    Versión optimizada que calcula directamente los valores candidatos
    en lugar de iterar por todo el rango
    """
    print("\n🚀 BÚSQUEDA OPTIMIZADA:")
    print("-" * 30)
    
    oo_year = 24001 * dias_year
    resultados = []
    
    # En lugar de iterar, calculamos directamente
    for year_offset in range(99, 102):  # Probar algunos años alrededor de 100
        c_calculado = ((year_offset + (dias_transcurridos / oo_year)) * oo_year + 1) * 24001
        c_entero = round(c_calculado)
        
        if rango_inicio <= c_entero <= rango_fin:
            # Verificar que realmente cumple la condición
            d = ((((c_entero / oo_year) - 100) * oo_year) - 1) / 24001
            e = d - dias_transcurridos
            f = round(e)
            
            if f == 0:
                resultados.append(c_entero)
                print(f"✅ Número encontrado: {c_entero:,}")
    
    if not resultados:
        print("❌ No se encontraron números en la búsqueda optimizada.")
    
    return resultados

# Ejecutar el programa
if __name__ == "__main__":
    print("🗓️  CALCULADORA DE DÍAS Y DIASOO, Jueguecito y unidades de tiempo y longitud")
    print("="*40)
    
    resultados = calculadora_dias()
    
    # Opción de búsqueda optimizada
    print("\n🤔 ¿Desea probar la búsqueda optimizada? (s/n): ", end="")
    respuesta = input().strip().lower()
    
    if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
        busqueda_optimizada(resultados['dias_transcurridos'])

    
    
    # Mostrar resumen final (actualizado con la nueva información)
    print("\n📊 RESUMEN:")
    print(f"• Fecha de nacimiento: {resultados['fecha_nacimiento'].strftime('%d/%m/%Y')}")
    print(f"• Fecha actual: {resultados['fecha_hoy'].strftime('%d/%m/%Y')}")
    print(f"• Fecha hace 6000 días: {resultados['fecha_menos_6000_dias'].strftime('%d/%m/%Y')}")
    print(f"• Días existidos: {resultados['dias_transcurridos']:,} días")
    print(f"• oo's vividos: {resultados['dias_transcurridos']:,} días")
    print(f"• Debería haber vivido en oo's: {resultados['diasoo']:,} oo")
    
    print("\n✨ Programa completado")