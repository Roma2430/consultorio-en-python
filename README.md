- Nombre: Rosa Maria Marin Grajales
- Codigo: 30395109

# Consultorio Odontológico

Programa en Python para el registro de clientes de un consultorio odontológico y el cálculo del valor de cada cita según el tipo de cliente y el servicio solicitado.

## Contenido del repositorio

- `cliente.py`: clase `Cliente`, con los datos básicos de cada persona registrada (cédula, nombre, teléfono, tipo de cliente, valor de la atención, cantidad, prioridad de atención y fecha de la cita).
- `consultorio.py`: lógica principal del programa. Pide los datos del cliente por consola, calcula el valor de la cita según el tipo de cliente y el servicio elegido, y guarda cada registro en una lista.

## Requisitos

- Python 3

No se necesitan librerías externas.

## Cómo ejecutarlo

```bash
python consultorio.py
```

El programa pregunta si se quiere registrar un cliente. Mientras la respuesta sea "si", pide:

1. Cédula
2. Nombre
3. Teléfono
4. Tipo de cliente: `particular`, `eps` o `prepagada`
5. Cantidad de servicios
6. Prioridad de atención: `normal` o `urgente`
7. Fecha de la cita
8. Servicio solicitado (según el tipo de cliente)

Al terminar el registro (cuando se responde "no"), el programa muestra:

- El total de clientes registrados.
- La cantidad de extracciones realizadas en total.
- El detalle de cada cliente registrado.
- Los ingresos totales del consultorio.

## Valores según tipo de cliente

**Particular** (valor base de la cita: $80.000)
- Limpieza: $60.000 (solo se permite una por cliente)
- Calzas: $80.000
- Extracción: $100.000
- Diagnóstico: $50.000 (solo se permite uno por cliente)

**EPS** (valor base de la cita: $5.000)
- Calzas: $40.000
- Extracción: $40.000

**Prepagada** (valor base de la cita: $30.000)
- Calzas: $10.000
- Extracción: $10.000

El valor final de cada cita corresponde al valor base más el valor del servicio, multiplicado por la cantidad.
