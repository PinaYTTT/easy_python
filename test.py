import easy_python

easy_python.consola.escribir("Test")


easy_python.consola.escribir(easy_python.numeros.sumar(10,5))
easy_python.consola.escribir(easy_python.numeros.restar(6,2))
easy_python.consola.escribir(easy_python.numeros.multiplicar(4,4))
easy_python.consola.escribir(easy_python.numeros.dividir(10,2))

timezone = easy_python.extras.tiempo()
easy_python.consola.escribir(timezone)

c = easy_python.consola.recibir("How old are you?: ")
easy_python.consola.escribir(f"You are: {c} years old")