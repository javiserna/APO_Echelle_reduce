Esta receta y script son el workflow para reducir espectros Echelle de APO.

Para usar este repo, debes tener las observaciones de tus objetos, bias, flat filtro abierto o red, flat filtro azul y lampara.

Primero descarga el repositorio en tu directorio de trabajo, descomprime si es necesario y dentro del folder, activa el entorno anaconda que tenga instalado pyraf.
Luego activa iraf en este directorio
ejecutando: mkiraf
con esto se creara un folder llamado uparm.

Luego mueve todas las observaciones como ilustracion o test (mueve el contenido del folder observations) al folder raw/DATE
y regresa al home del directorio de trabajo y ejecuta "python echelleReduction_py3.py DATE"

Espera unos minutos y en el directorio reduced/DATE encontraras los archivos con extension *.ec.fits los cuales son tus espectros reducidos.

Para graficar cualquier orden del espectro usar el codigo... luego lo compartire aqui por ahora esto es lo esencial.


Caveats:
Este script no corrige por darks, es algo en lo que estoy trabajando.
Tampoco aplana el continuo para los diferentes ordenes en los espectros reducidos, en principio tiene unas herramientas para hacerlo pero requiere ensayo y error de parte del usuario para que funcione
Estoy trabajando en la visualizacion de los ordenes de los espectros
