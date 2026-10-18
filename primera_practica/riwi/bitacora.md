

             ////PUNTOS DE CONTROL. SOLO LAS RESPUESTAS\\\\


- la diferencia es que la ruta absoluta muetra la ubicación de un archivo desde la raíz del sistema, en cambio la ruta relativa sirve para trabjar en un directorio, por ejemplo como hicimos ahora creando "reportes" y sus subcarpetas.
- Cuando listamos con "ls" normal solo muestra archvos normales. cuando se pone -a, alias de all; especficas mostrar todo el contenido. como.control_interno es una carpeta oculta, solo se muestra si se solicita con "-all"
- para editar un archivo sin nano, se usa echo: echo "contenido del párrafo"> para cambiar todo el cotenido o para escribir la primera línea, ">>" solo se usa para agregar contenido a la última línea
- Si, al move un archivo usando "mv", el comando especifica que se mueva con todo y contenido. Aplica igual para carpetas.
- el comando "mv" es, por decirlo de una manera, como si tomras el archivo o directorio en las manos y decidieras si solo quieres dejarlo en la carpeta atual ccon el mismo nombre, o moverlo a otro directorio.
- Siempre que se use "cp" para carpetas, se dee de esecificar -f, alias de force o forzar. Este comando por defecto no copia el contenid completo de la carpeta, para copiar arcivos no es necesario forzar el copiado.
- para buscar archivos en los directorios se usa find, para bucar información en los archivos se usa grep. La difeencia es que son comandos con propósitos diferentes.
- rmdir solo borra carpetas por seguridad egún lo que consulté, ya que podrían haber archivos oculos importantes. Es como una especie de stop o alerta.


                      ///COMANDOS UTILIZADOS\\\


- pwd: Muestra ruta actual donde te encuentras parado.
- ls: Sirve para listar directorios. -l para ver contenido detallado y -a para ver únicamente los archivos ocultos.
- cd: Comando de navegación fundamental. cd ~ es para ir directamente al directorio raíz, ls .. es para ir l directorio automáticamente anterior.
- mkdir para crear una carpeta en directorio actual, con -p para hacerlo con subcarpetas especidicadas así: {carp1,carp2,carp3}
- touch se usa para crear archivos con o sin extención, o inclsive ocultos.
- con echo se agrega contenido a los archivos. si pones > se agrega la primera lína o se borra todo si es un archivo con contenido. con >> se ba automáticamente al último reglón.
- cat sirve para consultar el contenido de un archivo. No lo ejecuta y sirve para cualquier tipo de archivo.
- Head: es para consltar la o las primeras linea de un achivo
- tail: este, por el contrario consulta ls últimas.
- cp: sirve para copiar archivos y directrios, el -r para carpetas  directorios con cotenido de archivos.
- mv es parra mover archivos o modificar su nombre.
- rm y rmdir. rm para borrar archivos y/o carpeta, especilmente con -rf; en cambio rmdir solo para carpetas vacías.
- find es para bucar en los directorios del sistema un archivo o carpeta.
- greep: solo es para consultar contenido en archivos de manera masiva o absoluta, de acuerdo a la ruta o directorio especificado. .

