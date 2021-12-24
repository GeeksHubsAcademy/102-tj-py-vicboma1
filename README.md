<p align="center">
    <img src="https://github.com/GeeksHubsAcademy/2020-geekshubs-media/blob/master/image/logo.png" >	
</p>


    Considere el siguiente problema:

    Escriba un programa corto que permita calcular los números primos dado un input de entrada.
    
     N = 13 
  
     Resultado :
	 
     [2,3,5,7,11,13]


    Observe que su resultado es una array de una dimensión.
    El valor mínimo de entrada será 1, en este caso el resultado devolverá -1.    
    
    Se atiente al siguiente ejemplo:
   
    N = 1     N = 2      N = 5         N = 8         N = 14     ...    N
                
    Resultado:

	null	   [2]	     [2,3,5]      [2,3,5,7]     [2,3,5,7,11]   



    En la carpeta 'src/main/java/es/geekshubs/academy/Primos.java' se encuentra el fichero con la definición de nuestro
    método vacío.
    En la carpeta 'src/test/java/es/geekshubs/academy/PrimosTest.java' se encuentra el fichero con la suite de test.

    El modus operandi de trabajo es el siguiente:
    
    Debes 'forkear' el proyecto a tu cuenta.
    Puedes hacer PR's ilimitadas e ir validando poco a poco la solución contra nuestro respositorio con CI.
    Puedes trabajar en local y subir la solución haciendo un PR a nuestro repositorio.
    Cuando se envíe la PR final, debes indicar el tiempo de dedicación y los intentos que has hecho.
    También puedes añadir un comentario para dar cualquier tipo de feedback.
    
    En caso de duda, revisa en el apartado de 'Referencias'.

    A continuación se muestran los resultado que se tienen que obtener tras desarrollar el algoritmo.
    
    [Suite Tests]

    	PrimosTest
        
    collected 11 items                                                             
    tests/test_kata.py::Test_kata::test_test01 PASSED                        [  9%]
    tests/test_kata.py::Test_kata::test_test02 PASSED                        [ 18%]
    tests/test_kata.py::Test_kata::test_test03 PASSED                        [ 27%]
    tests/test_kata.py::Test_kata::test_test04 PASSED                        [ 36%]
    tests/test_kata.py::Test_kata::test_test05 PASSED                        [ 45%]
    tests/test_kata.py::Test_kata::test_test06 PASSED                        [ 54%]
    tests/test_kata.py::Test_kata::test_test07 PASSED                        [ 63%]
    tests/test_kata.py::Test_kata::test_test08 PASSED                        [ 72%]
    tests/test_kata.py::Test_kata::test_test09 PASSED                        [ 81%]
    tests/test_kata.py::Test_kata::test_test10 PASSED                        [ 90%]
    tests/test_kata.py::Test_kata::test_test11 PASSED                        [100%]
    ========================== 11 passed in 0.04 seconds ===========================
    The command "python -m pytest -vv tests/test_kata.py" exited with 0.



## Referencias

* [Tutorial - Testing Automatizado](https://github.com/GeeksHubsAcademy/2020-js-vanilla-testing-FFFF/blob/master/README.md)