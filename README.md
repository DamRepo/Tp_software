# Sistema de Gestión de Usuarios

Programa de consola en Python que implementa registro y login de usuarios con
validación de contraseñas según una política de seguridad básica.

## Contexto

Este proyecto fue desarrollado como parte del **Trabajo Práctico N° 4** de la
materia *Conceptos de Desarrollo de Software*, correspondiente a la
**Tecnicatura Universitaria en Ciberseguridad** (Universidad del Gran Rosario).

El objetivo del TP es experimentar con dos enfoques de testing:

- **Caja blanca**: análisis automático del código fuente mediante
  [SonarCloud](https://sonarcloud.io), identificando bugs, vulnerabilidades,
  code smells y security hotspots.
- **Caja negra**: diseño de casos de prueba funcionales a partir de la
  especificación del programa, sin mirar el código.

## Requisitos

- Python 3.8 o superior
- Sin dependencias externas (usa únicamente la librería estándar `hashlib`)

## Cómo ejecutar

```bash
python3 user_management.py
```

El programa muestra un menú interactivo por consola:

```
--- Sistema de Gestion de Usuarios ---
1. Registrar usuario
2. Iniciar sesion
3. Salir
```

## Reglas de validación

### Usuario

| Regla | Detalle |
|---|---|
| No puede estar vacío | Debe ingresarse algún valor |
| Longitud mínima | Al menos 4 caracteres |

### Contraseña

| Regla | Detalle |
|---|---|
| Longitud mínima | Al menos 8 caracteres |
| Mayúscula | Al menos una letra en mayúscula |
| Minúscula | Al menos una letra en minúscula |
| Número | Al menos un dígito |
| Carácter especial | Al menos uno de `!@#$%^&*()_+-=[]{}|;:,.<>?` |

## Estructura del proyecto

```
.
├── user_management.py   # Programa principal
└── README.md            # Este archivo
```

## Funciones principales

| Función | Descripción |
|---|---|
| `validar_password(password)` | Verifica que la contraseña cumpla la política de seguridad |
| `validar_usuario(username)` | Verifica el formato del nombre de usuario |
| `registrar_usuario(username, password)` | Registra un usuario nuevo si pasa las validaciones |
| `login(username, password)` | Verifica credenciales de un usuario registrado |

## Análisis de calidad

Este repositorio está vinculado a SonarCloud para análisis estático de
código. El proyecto incluye intencionalmente ejemplos de malas prácticas
comunes (uso de hashing débil, credenciales embebidas, manejo genérico de
excepciones) con fines didácticos, documentados en el informe del TP.

## Licencia

Proyecto académico sin fines de distribución comercial.
