# Demostración de creación de un paquete de Python



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
