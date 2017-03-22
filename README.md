## RegTempHumd
Registro de Temperatura y Humedad de 20 dias con sensor DTH11 para Raspbian.

Cada 5 minutos, realiza una medición de temperatura y humedad. Registra los datos de medición actual asi como las mínimas y máximas hasta 20 días atrás. Con un nuevo día, el último registro se pierde y es desplazado para dejar un hueco libre para esos nuevos valores.

![](https://lh6.googleusercontent.com/I6PxIBxLdMscJZr6eolXbY5LQefRxqYh66YwN8hG7b7u2Jv15CM8w2e2dODfk6Dv17P_ZGOHkOF1PzQ=w1920-h950)

Como se puede apreciar, registra la **fecha** del día, **hora** de la última vez que registró los datos y valores **actual**, **máxima** y **mínima** de temperatura y humedad.

### Configuración de Pines
He usado el GPIO14, GPIO27 en BCM y el Pin# 2 de 5v.

![](https://lh3.googleusercontent.com/T0kUoP1BeESn91RYOjoWN2sC57ybCwfYiDVqfIdVedn8pBgXDGkY0LYnJHDzpkLEB7Xj9iEZ2Mo-TXc=w1920-h950)

De forma opcional, he instalado un led que me indica cuando se está realizando la medición. Al igual que el haber añadido dos transistores (uno para el led y otro para el sensor) para que no estén constantemente con alimentación dichos dispositivos.

### Instalación
