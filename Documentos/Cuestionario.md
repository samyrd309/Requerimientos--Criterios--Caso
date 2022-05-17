# Cuestionario

**1. ¿Qué es un Coding Dojo? referencia https://lorenzosolano.com/what-is-coding-dojo/**

  Is an activity where a group of developers diced to reunite to work on programming challenges.
  This is known as a technique to reinforce your habílities about certain topics and know more 
  about people with similar tastes. The purpose of this event is not to develop a competitive 
  environment quite the opposite is to create a collaborative and fun environment in which to
  develop ideas.
  
----

**2. Diferencia entre Requerimientos, Criterios de Aceptación y Escenarios de Prueba. Dar ejemplos a partir de un problema distinto a la referencia. Referencia https://lorenzosolano.com/requirements-acceptance-criteria-and/**

The difference between requirement, acceptance criteria, and scenario focuses on the fact that 
the requirements look for what they are and what they do directly, the acceptance criteria 
provide a guide that validates the fact that a requirement fulfills its function and the 
scenario becomes an example where the behavior of the requirement is visualized and it can be 
determined if it is good or bad based on the criteria acceptance.

A simple example is that we are requested to develop a section that filters the 3 most recent 
items in my database. Our requirement is the section with its 3 elements. The acceptance 
criteria are that when adding a new item, it appears in the section required. The scenario can 
be adding 4 more items to my database.

----

**3. De dos ejemplos de requerimientos no-funcionales, y especifique cual es su categoría (seguridad, performance, portabilidad, etc.)**

Example of non-functional requirements: 
* Security 

  * An elevator should not continue to function in the event of a fire.

* Usability

  	* The system should count with the user manual correctly structured.

----

**4. ¿Qué es TDD?**

It's a methodology that seeks to focus on developing the test before developing the code.  
Something to clarify is the fact that TDD is not directly tested, but rather starts from the 
premise established by its creator Kent Beck where he states that the code must be constantly 
tested and refactored. The point is that by writing the test first we: 
1. Create documentation. 
2. Design code that is simpler and easier to test. 
3. Create an environment where it will be easy for you to make changes.

----

**5. ¿Que son pruebas unitarias automatizadas?**

They are software tools used to automate the verification and validation process of a process 
that is normally carried out manually. The objective of all this is to detect possible flaws 
in the developed code without the need for human intervention. In addition to allowing a large 
number of scenarios to be executed, optimizing the error identification time.

----
**6. ¿Cual fue el 1er framework de pruebas unitarias y para cual lenguaje fue creado?**



----
**7. Describa los componentes de la arquitectura xUnit**

xUnit architecture

1. *Test runner*
  
    A program that helps you test the code and presents you with a report of the results obtained from the test.

2. *Test case*

    Is a group of conditions and variables that would tell if a function works properly or not.

3. *Test fixture*

    is a set of preconditions that creates an environment to run a test. 

4. *Test suites*

    Is a set of test cases used to test that a software program has a specific set of behaviors.
    
5. *Test execution*

    Is an execution process of an individual unit test that creates a world to isolate an environment for testing, 
    then we proceed to make all the tests and we conclude the process by cleaning the environment.


6. *Test result formater*

   

7. *Assertions*

     Is a function that verify the state of an unit under test. 

----
**8. Indique al menos tres desventajas de las pruebas unitarias automatizadas**

* Requieren más tiempo de desarrollo
* Los miembros del equipo de prueba tiene que tener un mayor nivel en cuanto a habilidades
* Se necesitan muchas más herramientas para realizar la prueba
* Costos de implemetación alto

----
**9. Indique al menos tres ventajas de las pruebas unitarias automatizadas**

* Retroalimentación instantánea
* Revisión rápida del sistema
* Mayor integración entre el equipo de QA y desarrollo

----
**10. Tomando el algoritmo de conversión de números arábigos o "decimales" a números Romanos:**
  * **Cree un documento donde se listen los Requerimientos, Criterios de Aceptación y Casos de Prueba para una aplicación de consola**
  * **Los casos de prueba deben ser de dos categorías: End-To-End (desde el UI) y Unitarios (caja blanca, código, bajo nivel)**

  **Revisar el archivo Requerimiento, Criterios de aceptación y casos de prueba**
----
**11. Utilizando el lenguaje de su preferencia cree cinco o mas casos de prueba unitarios automatizados utilizando un framework de automatización de pruebas para el algoritmo en cuestion**

  
----