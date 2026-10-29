"""
Enunciado:
Implementa la función 'calculate_max_and_min' que reciba como parámetro una
lista de números 'list_numbers', se deben considerar los casos en los que los
datos que se encuentran dentro de la lista sean de type string o que la lista
se encuentre vacía. 

Adicionalmente, la función debe ir imprimiendo cual es el número menor y el
número mayor según va avanzando en la lista siempre y cuando este sea distinto
al anterior resultado simulando la depuración por trazas.

Y finalmente, retornar un valor del número menor y del número mayor.

Parámetros:
list_numbers: Lista de números.

Ejemplo:
    Entrada: 
        [10, 5.1, 0, -2, 31, 55, 70, -10, 200, -55.55]
    Salida:
        'Greater:' 200
        'Lesser: ' -55.55

    Entrada:
        ['Hello', 1, 5, -20, 55.5]
    Salida:
        TypeError

    Entrada:
        []
    Salida:
        ValueError

Enunciat:
Implementa la funció 'calculate_max_and_min' que rebi com a paràmetre una
llista de números 'list_numbers', s'han de considerar els casos en què les
dades que es troben dins de la llista siguin de tipus string o que la llista
estigui buida.

Addicionalment, la funció ha d'anar imprimint quin és el name menor i el
name més gran segons va avançant a la llista sempre que aquest sigui diferent
a l'anterior resultat simulant la depuració per traces.

I finalment, retornar un valor del name més petit i del name més gran.

Paràmetres:
list_numbers: Llista de números.

Exemple:
     Entrada:
         [10, 5.1, 0, -2, 31, 55, 70, -10, 200, -55.55]
     Sortida:
         'Greater:' 200
         'Lesser: ' -55.55

     Entrada:
         ['Hello', 1, 5, -20, 55.5]
     Sortida:
         TypeError

     Entrada:
         []
     Sortida:
         ValueError

"""


def calculate_max_and_min(list_numbers):
    # Write here your code

    # La lista no debería estar vacía.
    if len(list_numbers) == 0:
        raise ValueError("ERROR. La lista no contiene elmentos.")

    # Le asigno el primer elemento a las variables de mayor y menor.
    mayor = menor = list_numbers[0]

    # Si encuentro un valor no numérico doy error y acabo. 
    # Mientras tanto voy acualizando el mayor y el menor.
    for val in list_numbers:
        if not isinstance(val, (int, float)):
            raise TypeError("ERROR. La lista contiene algún valor no numérico.")

        if val > mayor:
            mayor = val
        if val < menor:
            menor = val
        print(menor, mayor)

    print(menor, mayor)
    return menor, mayor

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

print(
     "\nResult: ", calculate_max_and_min([10, 5.1, 0, -2, 31, 55, 70, -10, 200, -55.55])
)
