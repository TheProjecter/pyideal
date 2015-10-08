# Propuesta de Metodos, Propiedades y Eventos del core principal #


Mi idea de lo más básico era exponer "pedazos" de código
para los plugin mediante propiedades y hacer cambio mediante
métodos.

## _Propiedades_ ##
  * Código entero
  * Nivel de identación de la línea actual
  * Bloque actual
  * Cabecera del bloque actual (declaratoria, parámetros)
  * Posición del cursor (caracter actual y vecinos)
  * Cláusulas import
  * Selección actual
  * código en AST
  * Lenguaje de codificación
  * Encoding
  * Línea de cógigo actual y siguiente (para el debugger)


## _Métodos_ ##
  * Identar: línea, bloque etc
  * Cambiar caracter
  * Tipear
  * Reescribir código
  * Posicionar el cursor
  * Guardar, Abrir archivo
  * ¿Parsear en archivos separados? (poner cada funcion en un archivo separado)
  * ¿Convertir en módulo?


## _Eventos_ ##
  * Tecla pulsada
  * Cambios realizados en el código (qué plugin los hizo y que hizo)
  * Plugin pide ejecución, en ejecución, ejecutado


De esta manera cada plugin podría hacer lo que quiere
por ejemplo, yo hago un plugín para poner automáticamente
el paréntesis de cierre, cuando mi plugin recibe el
evento de tecla pulsada y es un "(", mi plugin tipea ")"
y pone el cursor en medio.

Cambien, agreguen o quiten lo que les parezca