# Demostración de creación de un paquete de Python

**Nota:** Instalar requirements.txt en un ambiente virtual.

## Contenido a revisar en clase

* Estructura de los directorios

* Creación de modulos

* Instalación local del paquete

* Creación de la documentación de sphinx

 


## Uso de pip:

* Instalación:

```bash
$ pip install . 
```


* Desinstalación:

```bash
$ pip uninstall -y hello
```

## Uso del paquete:

```python3 
>>> import hello
>>> hello.hello()
Hello World!
```

```python3
>>> import hello
>>> hello.get_cars()
['renault', 'mazda', 'toyota', 'subaru', 'mitsubishi', 'dodge', 'jeep', 'chevrolet', 'volkswagen', 'honda', 'mclaren', 'porsche', 'ferrari', 'lamborghini', 'mercedes-benz', 'audi', 'volvo', 'bmw', 'jaguar']
```
