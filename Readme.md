## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)
5. [FAQs](#faqs)
### General Info
***
Making use of the algorithm for converting Arabic numerals or "decimals" to Roman numerals, a system was developed capable of converting decimals to Romans that are within the range of 1 to 1,000,000.
## Technologies
***
A list of technologies used within the project:
* [Python](https://www.python.org): Version 3.10.4 
* [Unittest](https://example.com): Version 1234
## Installation
***
A little intro about the installation. 
```
$ git clone https://example.com
$ cd ../path/to/the/file
$ npm install
$ npm start
```

## Requerimientos

  ### Funcionales

  * Se sebe poder insertear valores en un rango mayor a 0 y menor a 2000000.
  
  * El sistema debe aceptar solo valores numéricos por pantalla.

  * El sistema debe presentar los valores decimal ingresados
  por pantalla, en números romanos. 

  ### No Funcionales

  * Los números romanos I, X, C, y M deben porder repetirse hasta 
  tres veces a la hora de escribir un número compuesto.

  * Los números V, L y D no pueden repetirse.

  * Los valores de los números romanos compuestos deben 
  sumarse siempre que el valor de la derecha sea menor
  al valor de la izquierda.

  * Los valores de los números romanos compuestos que tienen
  un número a la derecha mayor que el de izquierda y este sea
  I, X o C, entonces se deberá restar el de la izquierda a la derecha.

  * Los números romanos que tengan una comilla(`), 
  su valor se multiplica por mil.

## Historia de usuario
  
  * User story 1: Como usuario, quiero poder insertar valores de 0 a 1999999, 
  para convertirlos a números romanos y presentarlos en pantalla. 



## Criterios de Aceptación
----
---
  ### **User story 1**
  * Como usuario, quiero poder insertar valores de 0 a 1999999, 
  para convertirlos a números romanos y presentarlo en pantalla . 
----

----
  #### **Scenario 1: Ingresa un valor nulo.**
  
  * *Given*: Se presenta en pantalla "Inserte un número".
  
  * *Then*: El usuario inserta el número.
  
  * *When*: El usuario presiona enter.
  
  * *Then*: El sistema presenta en pantalla "ADVERTENCIA: número ingresado inválido"
---
  
  #### **Scenario 2: Ingresa un valor tipo texto.**
  
  * *Given*: Se presenta en pantalla "Inserte un número".
  
  * *Then*: El usuario inserta un valor de tipo texto.
  
  * *When*: El usuario presiona enter.
  
  * *Then*: sistema presenta en pantalla "ADVERTENCIA: número ingresado inválido"
  
----
   
  #### **Scenario 3: Se ingresa un valor menor a 0.**
  
  * *Given* :Se presenta en pantalla "Inserte un número".
   
  * *Then* : El usuario inserta un valor menor a 0.
   
  * *When*: El usuario presiona enter.
  
  * *Then*: El sistema presenta en pantalla "ADVERTENCIA: Ingresa un número menor a 20000000 y mayor a 0."
  
----
  
  #### **Scenario 4: Se ingresa un valor mayor a 1999999.**
  
  * *Given*: Se presenta en pantalla "Inserte un número".

  * *Then*: El usuario inserta un valor mayor a 1999999.
  
  * *And*: El usuario presiona enter.
  
  * *Then*: El sistema presenta en pantalla "ADVERTENCIA: Ingresa un número menor a 20000000 y mayor a 0."
  
  ----

  #### **Scenario 5: Se ingresa un valor menor a 20000000 y mayor a 0.**
  
  
  * *Given*: Se presenta en pantalla "Inserte un número".
  
  * *When*: El usuario ingresa un valor menor a 20000000 y mayor a 0.
  
  * *And*: El usuario presiona enter.
  
  * *Then*: El sistema presenta en pantalla el número insertado por el usuario en pantalla.
  
  ----
  
  
## Casos de prueba

  * Ingresar valores vacíos

  * Ingresar valores de tipo string

  * Ingresar valores de tipo decimal

  * Ingresar valores de tipo int

  * Ingresar valor 0 

  * Ingresar valores menores a 0

  * Ingresar valores mayores a 1999999

  * Ingresar un valores  mayores 0 y valores menores a 2000000

