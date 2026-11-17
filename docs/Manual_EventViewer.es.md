



# Visor de eventos de Windows
  
Módulo para leer y filtrar registros del Visor de eventos de Windows.  

*Read this in other languages: [English](Manual_EventViewer.md), [Português](Manual_EventViewer.pr.md), [Español](Manual_EventViewer.es.md)*
  
![banner](imgs/BANNEREVENTVIEWER.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Como usar este modulo
Este módulo permite leer y filtrar registros del Visor de eventos de Windows.

1. **Registro:** Selecciona el registro de Windows que deseas consultar. Ten en cuenta que el acceso al registro de **Seguridad** puede requerir permisos de administrador.

2. **Origen:** Permite filtrar los eventos según el nombre de su origen (por ejemplo, `UserModePowerService`).

3. **ID del evento:** Permite filtrar los registros por el identificador del evento.

4. **Tipo de evento:** Selecciona el tipo de evento que deseas incluir en los resultados.

5. **Desde:** Establece la fecha y hora inicial para incluir los eventos generados a partir de ese momento.

6. **Hasta:** Establece la fecha y hora límite para incluir los eventos generados hasta ese momento.

7. **Filtrado por mensaje:** El valor ingresado debe coincidir exactamente con el nombre del origen del evento (*Source*, por ejemplo, `UserModePowerService`) o con un código de error específico incluido en la descripción
 general del evento. Este filtro no admite búsquedas por palabras clave ni coincidencias parciales de texto.

8. **Máximo de registros a revisar:** Indica la cantidad máxima de registros que se consultarán, comenzando por los más recientes. Por defecto, se revisan 1000 registros.


## Descripción de los comandos

### Obtener eventos de Windows
  
Lee y filtra registros del Visor de eventos de Windows.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Registro|Selecciona el registro de Windows que deseas leer. Seguridad puede requerir permisos de administrador.|Seleccione registro|
|Origen contiene|Filtra eventos cuyo nombre de origen contiene este texto.|Opcional|
|ID del evento|Filtra por un ID de evento exacto.|Opcional|
|Tipo de evento|Selecciona el tipo de evento que deseas incluir en los resultados.|Seleccione tipo de evento|
|Desde (DD/MM/AAAA HHmmss)|Incluye eventos generados desde esta fecha y hora.|14/10/2026 10:57:15|
|Hasta (DD/MM/AAAA HHmmss)|Incluye eventos generados hasta esta fecha y hora.|14/10/2026 10:57:15|
|Filtro de mensaje|Filtra eventos por origen o código de error específico.|Opcional|
|Máximo de registros a revisar|Máximo de registros que se revisarán, empezando por los más recientes. Por defecto 1000.|1000|
|Asignar resultado a variable|Variable donde se guardarán los resultados del registro de eventos.|event_logs|
