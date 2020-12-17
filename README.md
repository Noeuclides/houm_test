## Prueba Houm

### Requerimientos:

Tener una versión de python superior a 3.5 y el módulo "requests":
```sh
$ pip list | grep requests
requests           2.25.0 
```

En caso de que no esté instsalado:
```sh
$ pip install requests
```

### Ejecución:
```sh
$ git clone https://github.com/Noeuclides/houm_test.git
$ cd houm_test
```

1. Obtener cuantos pokemones poseen en sus nombres “at” y tienen 2 “a” en su nombre, incluyendo la primera del “at”.
```sh
$ python3 1-poke_name.py
```

2. ¿Con cuántas especies de pokémon puede procrear raichu? (2 Pokémon pueden procrear si están dentro del mismo egg group).
```sh
$ python3 2-poke_procreate.py
```

3. Entregar el máximo y mínimo peso de los pokémon de tipo fighting de primera generación (cuyo id sea menor o igual a 151).
```sh
$ python3 3-poke_weight.py
```
