fruits = ['banana', 'orange', 'mango', 'lemon', 'tomato', 'pear', 'apple']
# *res, second_fruit = fruits #* la variavle ' *res ' crea un nuevo array con los datos sobrantes.
# print(res)
# print(second_fruit)

'''
    unpack array con indice es cuando mediante el nombre del array seguido de [] y dentro poner de donde a donde quiere obtener los datos 
    ejemplo [1:2] se le pone dos puntos para decir que del ( 1 al 2 ) pero si despues de los puntos no se pone nada agarra de donde se le de
    de inicio hasta donde termina ejemplo >[1:]
'''
# print(fruits[1:]) # esto agarra del indice 1 hasta donde termina resuktado > [ 'orange', 'mango', 'lemon' ]
# print(fruits[1:2]) # en este caso no solo obtendra los datos del indice 1 al 2 [ 'orange']

'''
cuado se le pone los corchetes y doble vez ' : ' despues un numero ' n ' recorera el array cada ' n ' [::2] esto devolvera cada 2 
elemento del array 
'''
# print(fruits[::3])  # aqui el resultado es [ 'banana', 'lemon' ]

'''
cuado se le pone los corchetes y doble vez ' : ' despues un numero negativo ' -n ' recorera el array cada ' -n ' [::-1] esto devolvera todo
el array pero al reves ya que ira de -1 al -4 pero si le pones un numero negativo que sea mayor a '-1' un '-2' lo que ara es que te devolvera 
al reves pero cada dos pocisiones como en el ejemplo anterior pero de la ultima pocision a la primera    
'''
# print(fruits[::-2]) # el resultado de esto seria ['pear', 'lemon', 'orange']

'''
modificar el array solo se pone la pocision del que se quiere cambiar de valor array[position] = nuevo_valor
para modificar el ultimo valor del array se hace obteniendo el lenght del array y se le pone el -1 ejemplo array[len(fruits) - 1] = nuevo_valor
'''

# fruits[0] = 'avocado'
# fruits[len(fruits) - 1] = 'strawberry'
# print(fruits)

'''
checar si un valor existe en un array esto se hace con el operador ' in ' ejemplo > 'word_buscar' in array y esto retorna un bool 
'''
# print('aple' in fruits)

'''
añadir un nuevo valor del array se hace con la funcion de array.append('nuevo_valor') solo puede agregar un valor
pero esxite una forma mejor y mas rapida que es como el metodo spread de javascript es haci nuevo_array = [*array_anterio, nuevo_valor]
'''

# fruits.append('aple')
# print(fruits)
# print([*fruits, 'aple'])

'''
con el metodo de insert() se puede agregar al array un unico valor pero dando una pocision especifica y si ahi un valor ahi se desplazara
array.insert(pocision, nuevo_valor) si se le pone un valor superior al lenght del array se agregara al ultimo sin importar la pocision que se le dio
si es negativo y es menor a cero no importa se agrega al principio de el array
'''
# fruits.insert(-10, 'kiwi')
# print(fruits)

'''
eliminar un valor del array con la funcion pop() en este caso si se le manda como parametro un index eliminara el valor con el index dado pop(2)
pero si no se le da el valor eliminara el ultimo valor del array  y en los dos casos te retorna el valor eliminado del array
'''
# print(fruits.pop()) # en este caso eliminara el ultimo valor por que no se le da el index retornara el valor eliminado del array
# print(fruits.pop(0)) # en este caso eliminara el valor de la posicion que se le dio retornar el valor eliminado del array

'''
eliminar mediante la funcion 'del' si se le especifica la pocision eliminara solo eso pero si no se le especifica eliminara el array y sera como si 
no estubiera definida la variable:
estructura  'del array' esto eliminara el array por completo 
estructura 'del array[pocision]' esto solo eliminara el valor en esa posicion
'''
# del fruits[0] #solo eliminara el valor de esa posicion
# del fruits #esto lo que ara es q eliminara el array y la variable fruits sera indefinida
# print(fruits)

'''
limpiar el array por completo con la funcion de clear() lo que ara es que dejara vacio pero no eliminad e array
estructura array.clear() el resultado es array = []
'''
# fruits.clear()#vaciara al array sin importar cuantos valorers tenga y sera []
# print(fruits)

'''
copiar un array a una nueva variable ya que si copiamos de esta forma > list2 = list1 lo que hara es que cuando modifiquemos algo de 
list1 se modificara en la list2 para esto existe la funcion de copy():
estructura array.copy() 
'''
# copy_array = fruits.copy();
# print(copy_array)


'''
para unir dos o mas listas o mas conocido como concatenacion es con el signo plus ' + '
'''
# list1 = ['carlos', 'daniel',]
# list2 = ['cruz', 'perez']
# print(list1 + list2)

'''
unir listas con la funcion de extend() lo que hace es que de una lista le agrega otra lista:
estructura array.extend(array).
existe una forma mas que seria con haciendo una nueva variable que extraiga todos los valores de cada array:
estructura all_data = [*firt_array, *second_array, *third_array, ....]
'''
# vegetables = ['carrot', 'potato', 'onion', 'garlic']
# vegetables.extend((fruits))#lo que dara como resultado es todo el array de vegetables y en el mismo array agregara fruits
# print(vegetables)
# fruits_vegetables = [*vegetables, *fruits] #esto lo que hace es lo mismo de arriva pero sin usar funcion
# print(fruits_vegetables)

'''
para contar cuantos valores existen en un array se usa el metodo de count() lo que ara es que contara cuantos valores ahi con el 
valor que se le ando como parametro a la funcion count():
estructura array.count('valor_buscar') 
'''
# print(fruits.count('banana')) #retornara las veses que encontro ese valor en el array

'''
encontrar el index de un valor esto se hace con la funcion de index() el cual retornara el index de donde encontro el valor mandado por parametro:
estructura array.index('valor_buscar')
'''
# print(fruits.index('pear'))#retorna la posicion de donde encontro el valor

'''
para hacer que el array ordene al reves se usa la funcion de reverse():
estructura array.reverse().
aparte esta lo de poner array[::-1]
'''
# fruits.reverse()
# print(fruits)
# print(fruits[::-1])

'''
ordenar un array eso se hace con el metodo sort() que recive como argumento el reverse=true que esto ara que se ordene desendientemente y si no se manda 
se ordenara asendentemente:
estructura 
    array.sort() esto lo ordenara asendentemente
    array.sort(reverse=true) esto lo ordenara desendientemente
    
la funcion de sorted() hace lo mismo que el sort() pero este no modifica el array original y recibe como parametro el array a ordenar y el reverse 
si es que se quiere ordenar decendientemente:
estructura:
    sorted(array) esto lo ordenara asendentemente
    sorted(array, reverse=true) esto lo ordenara desendientemente
'''
# fruits.sort() #esto lo ordenar asendientemente
# fruits.sort(reverse=True) #esto lo ordenar desendientemente
# print(fruits)

