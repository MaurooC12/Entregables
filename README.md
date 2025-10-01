# ENTREGABLE ACTUAL: Taller de Repaso POO

## 📌 Descripción
Este taller aborda la **encapsulación en Programación Orientada a Objetos (POO) con Python**, repasando los conceptos fundamentales de:

- **Atributos públicos, protegidos y privados**.  
- Uso de **propiedades** mediante `@property` y `@setter`.  
- **Buenas prácticas** de diseño en POO para mantener la claridad y seguridad en el código.
  
## 📂 Contenido del Repositorio
- `Entregable - Taller de repaso.pdf` → Documento con las **respuestas y desarrollo del taller**.
- `Anteriores` → Carpeta con los entregables anteriores.
  
---

## Respuestas

---

### 1  
- A) `a.x`  
- B) `a._y`  
- D) `a._A__z`

---

### 2  
`False` `True`

---

### 3  
a) **Falso** – El guion bajo simple (`_atributo`) es solo convención: indica “esto es interno”, pero en realidad sí puedo acceder desde fuera.  

b) **Falso** – Con (`__atributo`) ocurre el *name mangling*: Python lo transforma internamente a `_Clase__atributo`. Eso lo vuelve menos accesible de manera accidental, pero no imposible; aún se puede acceder usando el nombre cambiado.  

c) **Verdadero** – El atributo (`__x`) en una clase `A` se guarda como (`_A__x`), mientras que en una clase `B` sería (`_B__x`). El nombre de la clase forma parte del atributo *mangled*.

---

### 4  
Imprime `abc` y no hay error de acceso porque en Python el prefijo con un solo guion bajo (`_token`) es solo convención de “uso interno”.  
El lenguaje no bloquea el acceso desde fuera de la clase ni desde una subclase.  
Por eso, `Sub` puede usar sin problema el atributo (`_token`) definido en `Base`.

---

### 5  
Imprime: `2 1`

---

### 6  
Da error, ya que `__slots__` solo está permitiendo el ingreso de una `x`.

---

### 7  
```python
self._b = 99
```

---

### 8  
Imprime: `True False True`

- `(_step)` existe tal cual — subrayado simple es solo convención → `True`  
- `(__tick)` no existe como tal porque fue *name mangled* → `False`  
- `(_M__tick)` sí existe, porque así fue renombrado internamente `__tick` en la clase `M` → `True`

---

### 9  
```python
print(s._S__data)
```

---

### 10  
Es más factible que aparezca `_D__a`, porque cuando se declara un atributo con (`__a`), Python aplica *name mangling*, transformándolo en (`_D__a`).  
Por eso, si se filtra `dir(d)` buscando `'a'`, el que se encuentra es el nombre transformado (`_D__a`).  
Ni (`__a`) ni (`a`) aparecen en la lista: `__a` porque fue renombrado, y `a` porque nunca existió en teoría.

---

### 11  
```python
@property
def saldo(self):
    return self._saldo

@saldo.setter
def saldo(self, value):
    if value < 0:
        raise ValueError("El saldo no puede ser negativo.")
    self._saldo = value
```

---

### 12  
```python
class Termometro:
    def __init__(self, temperatura_c):
        self._c = float(temperatura_c)

    @property
    def temperatura_f(self):
        return self._c * 9/5 + 32
```

---

### 13  
```python
@nombre.setter
def nombre(self, value):
    if not isinstance(value, str):
        raise TypeError("nombre debe ser str")
    self._nombre = value
```

---

### 14  
```python
class Registro:
    def __init__(self):
        self.__items = []

    def add(self, x):
        self.__items.append(x)

    @property
    def items(self):
        return tuple(self.__items)
```

---

### 15  
```python
class Motor:
    def __init__(self, velocidad):
        self.velocidad = velocidad

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, v):
        if not (0 <= v <= 200):
            raise ValueError("Velocidad debe estar entre 0 y 200")
        self._velocidad = v
```

---

### 16  
- `_atributo`: Es como decir “esto es privado, pero si alguien lo necesita, lo puede usar”.  
  No está hecho para mostrarse, pero tampoco está realmente oculto.

- `__atributo`: Aquí sí es como decir “esto no se puede usar directamente”.  
  Python le cambia el nombre internamente (*name mangling*) para que no sea fácil de encontrar.  
  Es una forma de esconder atributos y evitar accesos accidentales.

---

### 17  
En lugar de devolver la lista original, se debe devolver una **copia** o una **vista inmutable** (como una `tuple`).  
De esa forma, quien use el objeto podrá consultar los datos sin modificar la estructura interna.

---

### 18  
Falla en la llamada a `self.__x` dentro del método `get()`.

Ese acceso intenta encontrar `__x` en la clase `B`, lo cual se transforma en `_B__x` por el *name mangling*.  
Sin embargo, el atributo fue definido en la clase `A` como `__x`, lo cual se convirtió en `_A__x`.

Por eso, `B().get()` lanza un `AttributeError`.

**Solución:** Usar `_x` en lugar de `__x` en la clase base si se planea acceder desde subclases.

---

### 19  
```python
class _Repositorio:
    def guardar(self, k, v):
        return self.__repo.guardar(k, v)
```

---

### 20  
```python
class ContadorSeguro:
    def __init__(self):
        self._n = 0

    def inc(self):
        self._n += 1
        self.__log()

    @property
    def n(self):
        return self._n

    def __log(self):
        print("tick")
```

---

## 👥 Autor
- Mauricio Cepeda Villanueva  

---

## 📜 Licencia
Este proyecto se distribuye bajo la licencia **MIT**.  
Consulta el archivo [`LICENSE`](LICENSE) para más información.

