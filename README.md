# Django Random Users

Aplicación web desarrollada en Django que consume la API pública **Random User Generator** para mostrar un catálogo de usuarios aleatorios con paginación y perfiles detallados.

## Descripción

Esta aplicación permite explorar usuarios generados aleatoriamente desde la API de Random User Generator. Los usuarios se muestran en tarjetas con información básica y se puede acceder a un perfil detallado de cada uno.

## Tecnologías

- Python 3.11+
- Django 5.2.17
- Requests 2.31.0
- Bootstrap 5
- Bootstrap Icons
- HTML5
- CSS3
- JavaScript

## Características

- **Catálogo de usuarios**: Visualiza 10 usuarios por página
- **Paginación real**: Cada página consume la API con diferentes valores de `page`
- **Perfiles detallados**: Información completa de cada usuario
- **Diseño responsivo**: Funciona en desktop, tablet y móvil
- **Manejo de errores**: Página amigable cuando la API no está disponible
- **Sin base de datos**: Los datos se obtienen directamente desde la API

## Estructura del Proyecto

```
prueba 1/
│
├── manage.py
├── db.sqlite3
│
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── templates/
│   ├── base.html
│   ├── users/
│   │   ├── user_list.html
│   │   └── user_detail.html
│   └── errors/
│       └── api_error.html
│
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── app.js
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/django-random-users.git
cd django-random-users
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar migraciones

```bash
python manage.py migrate
```

### 6. Iniciar servidor

```bash
python manage.py runserver
```

### 7. Abrir en el navegador

Visita: **http://127.0.0.1:8000/**

## API Utilizada

La aplicación consume la API de **Random User Generator**:

```
https://randomuser.me/api/?results=10&seed=abc&page={numero_pagina}
```

### Parámetros:

- `results=10`: Obtiene 10 usuarios por página
- `seed=abc`: Mantiene consistencia en los resultados (siempre igual)
- `page={numero}`: Número de página para la paginación

## Funcionamiento

### Paginación

La aplicación implementa paginación real:

- Página 1: `https://randomuser.me/api/?results=10&seed=abc&page=1`
- Página 2: `https://randomuser.me/api/?results=10&seed=abc&page=2`
- Página 3: `https://randomuser.me/api/?results=10&seed=abc&page=3`

Cada cambio de página hace una nueva petición a la API.

### Vista de Lista

- Muestra 10 usuarios en tarjetas
- Información básica: foto, nombre, username, correo, ciudad, país
- Botón para ver perfil detallado
- Navegación entre páginas

### Vista de Detalle

Muestra información completa del usuario organizada en secciones:

- **Información Personal**: Nombre, apellido, género, fecha de nacimiento, edad
- **Contacto**: Correo, teléfono, celular
- **Ubicación**: País, estado, ciudad, calle, código postal, coordenadas
- **Cuenta**: Username, UUID, fecha de registro, zona horaria

### Identificación de Usuarios

La aplicación utiliza `login.uuid` de la API para identificar de manera única a cada usuario. Gracias al parámetro `seed=abc`, los usuarios siempre son los mismos en cada página.

### Manejo de Errores

Si la API no está disponible o hay un error de conexión, se muestra una página amigable con un botón para volver al catálogo.

## Capturas de Pantalla

### Catálogo de Usuarios
La página principal muestra 10 usuarios en tarjetas con su información básica.

### Perfil de Usuario
Vista detallada con toda la información organizada en secciones con colores e iconos.

## Contribuir

Si deseas contribuir al proyecto:

1. Haz un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -m 'Agrega nueva característica'`)
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## Autor

Desarrollado como proyecto de demostración de consumo de APIs REST con Django.

## Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.
