# Brainstorming #

Add your ideas here!!.


# Details #

La votacion de las ideas que estan en este documento esta en VotacionBrainstorming

No duden en editar esta pagina para comentar/agregar lo que consideren necesario para mejorar el proyecto y esta documentacion!! :)



Un resumen de lo que tenemos hasta ahora (Borrowed from http://python.org.ar/pyar/IDEal):

  * Resaltado de sintaxis
  * Autocompletado de código [Daniel](Daniel.md)->(a mi me gustaría que autocomplete con los datos importados también)
  * Shell integrado
  * Debugger
  * Integración con herramientas de documentación
  * Empaquetador de codigo: creación de .deb, .rpm, .exe, etc...
  * Liviano, es decir cargar rápido y no consumir muchos recursos
  * Multiplataforma
  * Integración con diseño de GUIs (qt4, gtk, wx, etc) - GuiSketchs
  * Integración con sistemas de control de versiones (subversion, mercurial, git, etc)
  * Posibilidad de uso y modificación de plantillas (templates, snippets)
  * Manejo de proyectos
  * Extensible en python
  * Sistema de plugins para extender

Hace falta definir:
  * Si sera independiente de la interfaz grafica o si se hara especificamente para alguna GUI.
  * Que arquitectura usaremos
    * Minimal core (inter plugins comm) y plugins?
    * Funcionalidad Base definida + plugins?
  * Que formara parte de la base y que se implementara como plugins


"Minimal Core, seria como un router de mensajes entre los plugins nada
mas. Es el punto donde expones los servicios existentes de tus plugins
para que otros lo puedan usar, y generas un "workflow" entre los
plugins para poder manejar la informacion.

(hice una propuesta de este estilo en [Propuesta\_1](Propuesta_1.md)  que está en medio
de estos dos sistemas) [Daniel](Daniel.md)

Funcionalidad Base definidida, seria, algo asi como tener un 'Notepad'
listo, y a esto pegarle los plugins alrededor."
Explicacion por: QliX=D! [EHB](aka.md)


# Cosas que podemos usar para el proyecyo #
(o proyectos para el proyecto :P)

**Pygments = Coloreado de sintaxis "multimarca" :P - http://pygments.org/
> Permite multiples lenguajes y tambien distintos formatos de salida como html, rtf(probablemente este funcione en multiples gui toolkits?), ASCII escape codes, etc.**

**rope = Refactoring de lenguaje python - http://rope.sourceforge.net/
> No lo revise mucho, pero se ve prometedor**

