#Nuevo planteo para el desarrollo

# **Descripción** #

**Un core centralizará los eventos y los proveerá a los plugins que se conecten a ellos** Los plugins se _categorizarán_ y tendrán que respetar cierta interface pública para que los plugins puedan comunicarse con ellos
**Los plugins se comunicarán directamente sin pasar por el core**


---

# **Detalles** #

## Categorías ##
### ProjectManajer ###
> _Eventos Públicos_
  * Archivo Abierto/Cerrado
  * Archivo Guardado
  * ¿?

> _Metodos Públicos_
  * Guardar archivo
  * Abrir archivo
  * ¿?

> _Propiedades Públicas_
  * Path del proyecto
  * Codificación
  * Lenguaje
  * ¿Recursos?
  * ¿?

### Code Editor ###
> _Eventos Públicos_
  * Tecla pulsada
  * Cambios realizados en el código (qué plugin los hizo y que hizo)
    * Cambio de Identación
    * inicio de bloque

> _Propiedades Públicas_
  * Archivo en edición
  * Posición del cursor
  * Nivel de identación del cursor
  * Texto de Linea actual, bloque actual
  * Cabecera actual (def, class)
  * ¿cláusulas import?
  * ¿archivo en AST?

### Non GUI Plguins ###
> _se emplearía por ejemplo para plugins de comunicaciones_
  * administración de mensajes

### ToolBar ###
  * Botón pulsado
  * Set/Get Estado de botones
  * Docking

### Menu ###
  * Items, Subitems
  * Set/Get Estado
  * Hotkeys




¿otras categorias?