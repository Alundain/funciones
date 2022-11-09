a = 5
b = 4
def add(a,b):	
    x = a + b
    return (x)	


def sé_alegre(name='', repeat=2):
	print(f"buenos días {name}\n" * repeat)
sé_alegre()    # salida: buenos días (repetida en dos líneas)
sé_alegre("tim")    # salida: buenos días tim (repetida en dos líneas)
sé_alegre(name="john")    # salida: buenos días john (repetida en dos líneas)
sé_alegre(repeat=6)    # salida: buenos días (repetida en 6 líneas)
sé_alegre(name="michael", repeat=5)    # salida: buenos días michael (repetida en 5 líneas)
# NOTA: el nombre de los argumentos no importa si somos explícitos al enviarlos
sé_alegre(repeat=3, name="kb")    # salida: buenos días kb (repetida en 3 líneas)

def multiplicar(num_list, num):
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiplicar(a,5)
print(b)
# salida:
# [2,4,10,16]