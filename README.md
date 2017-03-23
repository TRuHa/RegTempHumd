## RegTempHumd
Registro de Temperatura y Humedad de 20 dias con sensor DTH11 para Raspbian.

Cada 5 minutos, realiza una medición de temperatura y humedad. Registra los datos de medición actual asi como las mínimas y máximas hasta 20 días atrás. Con un nuevo día, el último registro se pierde y es desplazado para dejar un hueco libre para esos nuevos valores.

![medicion](https://raw.githubusercontent.com/TRuHa/RegTempHumd/master/wiki/medicion.png)

Como se puede apreciar, registra la **fecha** del día, **hora** de la última vez que registró los datos y valores **actual**, **máxima** y **mínima** de temperatura y humedad.

### Configuración de Pines
He usado el GPIO14, GPIO27 en BCM y el Pin# 2 de 5v.
![temphumd](https://raw.githubusercontent.com/TRuHa/RegTempHumd/master/wiki/temphumd.png)

De forma opcional, he instalado un led que me indica cuando se está realizando la medición. Al igual que el haber añadido dos transistores NPN2222 (uno para el led y otro para el sensor) para que no estén constantemente con alimentación dichos dispositivos.

### Instalación
Copia carpeta "temphumd" a "~/temphumd"
Ejecutar o añadir a la lista de procesos a ejecutar en inicio
#
#### Agradeciminetos

Gracias a https://szazo.github.io/ por su gran aporte https://github.com/szazo/DHT11_Python
