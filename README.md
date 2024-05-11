# Gestor de Notas

## Descripción
Este proyecto es una aplicación web desarrollada con Django que permite a los usuarios registrados gestionar sus propias notas. Los usuarios pueden crear, ver, editar y eliminar notas. Este gestor de notas es ideal para mantener organizada la información importante de manera eficiente y accesible.

## Funcionalidades
- **Autenticación de Usuarios**: Inicio de sesión y registro para gestionar accesos.
- **Gestión de Notas**: Usuarios pueden crear, leer, actualizar y eliminar notas.
- **Interfaz Responsive**: Diseñado para adaptarse a cualquier dispositivo.

## Tecnologías Utilizadas
- Django
- SQLite (base de datos por defecto de Django)
- HTML5
- CSS3

## Configuración del Proyecto
Para ejecutar este proyecto en tu máquina local, necesitas tener instalado Python y Django. Sigue los pasos a continuación para configurarlo.

### Clonar el Repositorio
Para obtener el proyecto, clona el repositorio en tu máquina local usando:

```bash
git clone https://github.com/LokiAngelMx/ProjectNotes.git project_notes
cd project_notes
```

### Instalación de Dependencias
Asegúrate de que Django está instalado. Si no, puedes instalarlo usando pip:
```bash
pip3 install django
```

### Configuración de la Base de Datos
Ejecuta las migraciones para configurar tu base de datos:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Crear un Superusuario
Para administrar la aplicación, deberás crear un superusuario:
```bash
python3 manage.py createsuperuser
```
Sigue las instrucciones en pantalla para completar la creación del superusuario.

### Ejecutar el Servidor
Para iniciar el servidor, ejecuta:
```bash
python3 manage.py runserver
```
Ahora puedes acceder a la aplicación en http://127.0.0.1:8000/.

### Ejecutar los Casos de Prueba
Sigue estos pasos para ejecutar los casos de prueba:
```bash
python3 manage.py test mynotes
```
