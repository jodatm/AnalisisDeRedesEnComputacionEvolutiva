# Foobar

Esta herramienta permite realizar pruebas para la mejora de algoritmos de optimización mediante el curso de redes complejas.E n este trabajo se plantea el desarrollo de un mecanismo de control para una estrategia de computacion evolutiva guiado por una red compleja dinamica para mejorar el desempeño del algoritmo.

## Instalación

### Descargar el repositorio

```bash
git clone https://github.com/jodatm/AnalisisDeRedesEnComputacionEvolutiva.git
```

Debe instalar Python 3, de: [Descarga python](https://www.python.org/download/releases/3.0/) o desde el gestor de paquetes de Windows.


Usando el administrador de paquetes [pip](https://pip.pypa.io/en/stable/) instale las dependencias

```bash
pip3 install networkx
pip3 install numpy
pip3 install pandas
```

En el caso de usar sistema operativo Windows, revisar [manual de uso pip Windows](https://recursospython.com/guias-y-manuales/instalacion-y-utilizacion-de-pip-en-windows-linux-y-os-x/)

### Versiones recomendadas


* Python 3.7,
* Spyder 3.3.3
* Networkx 2.4
* Mathematica 12

## Uso de la herramienta

En la consola de Windows, Linux o Mac ubicarse en el directorio principal de la aplicación.

### Funcion Ackley

```bash
#Evolutivo
python3 Funcion\ Ackley\ /Evolutivo.py
#SW
python3 Funcion\ Ackley\ /sw.py
#Swbest
python3 Funcion\ Ackley\ /swbest.py
#Swhd
python3 Funcion\ Ackley\ /swhd.py
```

### Funcion Esfera

```bash
#Evolutivo
python3 Funcion\ Esfera/Evolutivo.py
#SW
python3 Funcion\ Esfera/sw.py
#Swbest
python3 Funcion\ Esfera/swbest.py
#Swhd
python3 Funcion\ Esfera/swhd.py
```

### Problema de la mochila

```bash
#Evolutivo
python3 Mochila/main_evolutivo.py
#SW
python3 Mochila/main_sw.py
#Swbest
python3 Mochila/main_sw_best.py
#Swhd
python3 Mochila/main_sw_hd.py
```

## Contribución
Pull requests son bienvenidos, para cambios mayores, por favor abrir un issue y podemos discutir el cambio.

Please make sure to update tests as appropriate.

## Licencia
[MIT](https://choosealicense.com/licenses/mit/)
