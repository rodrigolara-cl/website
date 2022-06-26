Title: Tutorial para realizar página web con Pelican en Github Pages
Date: 2022-06-25 22:46
Tags: pelican, github, github-pages
Category: Blog
Slug: tutorial-pelican-github-pages
Author: Rodrigo Lara
Summary: En este tutorial mostraré el workflow actualizado al 2022 para realizar páginas web en pelican y sincronizarlas con git hacia github.
Lang: es
Translation: false
Status: published

Hace años por allá el 2013 probé sitios web estáticos en github pages e intenté usar sin mucho éxito Jekyll y Pelican. En general la curiosidad no llega más lejos que la necesidad. Sólo me ha tocado trabajar con sitios web en wordpress y ahora último prestashop debido a que son las tecnologías usadas en las páginas web de mis últimos dos trabajos, sin embargo no son lo que necesito actualmente para crear mi página web personal. Utilicé Google Sites con éxito para un proyecto de baterías junto con un amigo, pero la selección fue restringida a que debía ser fácil de escribir contenido y configurar. Bueno ninguna de las opciones cumple con mis requisitos personales los cuales son:

- Posibilidad de integración de resultados de Jupyter Notebook.

- Seguimiento de cambios con GitHub y uso de alojamiento gratuito de Github Pages.

- Capacidad de personalización en Python a futuro.

Por lo que decidí probar denuevo Pelican, pero
el principal problema que tuve durante este proceso fue que los tutoriales que encontré acerca de Pelican y Github Pages no me permitieron ejecutar todos los pasos como corresponde y perdí bastante tiempo tratando de entender por qué no lograba subir el sitio a Github.

En este tutorial mostraré el procedimiento actualizado al 2022 para realizar páginas web en Pelican y sincronizarlas con Git hacia Github. Existen algunos comandos que sólo funcionan con python instalado con anaconda (crear y activar entornos virtuales) y en linux (el comando make puede que no funcione en windows, en ese caso probar fab).

## Creación de repositorios en GitHub

Github Pages permite una sola página web personal con el formato [https://nombre-usuario.github.io](https://nombre-usuario.github.io) pero no restringe la cantidad de las páginas de proyecto que se accederían [https://nombre-usuario.github.io/nombre-proyecto](https://nombre-usuario.github.io/nombre-proyecto).

La mayoría de los tutoriales explican como realizarlo en las páginas de proyecto, y la documentación de Pelican explica sólo la parte final de subir el sitio para ambos casos, por lo que existía un vacío y algunas incompatibilidades con el estado actual de Github y los tutoriales.

El primer paso es crear dos repositorios en Github, uno para alojar la página web, y otro para alojar el código de la página para realizar el seguimiento de cambios.

Al crear el repositorio para alojar la página web debemos colocar en el nombre del repositorio `nombre-de-usuario.github.io`, por ejemplo:

![Imagen 1]({static}/images/githubusuario.png)

Recomiendo no crear un readme ni gitignore ni licencia ya que no los necesitamos para este repositorio.

A continuación creamos el repositorio para el seguimiento del código del sitio web. En este puedes colocar cualquier nombre del proyecto y colocar un readme también.
Una vez realizado este repositorio el último paso es crear una llave de acceso personal en GitHub.
- Ingresar a configuracion/settings del usuario (no del proyecto)
- Al final de la lista de opciones se encuentra developer settings
- Ingresar a personal access token y generar un nuevo token, luego seleccionar la duración del token(si eliges duración tendrás que crear un nuevo token periódicamente) y finalmente elegir el scope, en particular yo seleccioné todos los permisos para evitar problemas de acceso pero probablemente no sean necesario todos.
- El token aparecerá una sola vez por lo que debes copiarlo y guardarlo.
- Este token lo utilizaremos para autenticarnos al realizar el push del repositorio local hacia github y para subir la página web.

## Configuración entorno virtual de Python e instalación de Pelican, Git y dependencias

Para instalar Pelican en Anaconda Python se recomienda crear un entorno virtual.

~~~
conda create -n nombre-entorno-virtual
~~~

Luego se debe activar el entorno virtual

~~~
conda activate nombre-entorno-virtual
~~~

Una vez activado instalar pip y opcionalmente git si es que no está instalado en el sistema operativo aún

~~~
conda install pip
conda install git
~~~

Luego instalar Pelican

~~~
pip install pelican
~~~

* Adicionalmente instalar las siguientes librerías
~~~
pip install markdown
pip install fabric3
pip install bs4
pip install ghp-import
~~~  



## Clonar repositorio del código fuente del sitio

En el terminal ir a la ubicación donde alojarás el sitio en forma local y clonar el repositorio donde se realizará el seguimiento del código.

~~~
git clone https://github.com/nombre-usuario/nombre-repositorio
~~~

Entrar a la carpeta del repositorio desde la terminal, esa será la ubicación principal desde donde trabajaremos. Para sincronizar el repositorio al realizar cambios desde distintos computadores, realizar primero un git pull antes de editar.
~~~
git pull origin main
~~~  



## Utilizar pelican-quickstart

Pelican brinda un script para crear los archivos necesarios para desarrollar el sitio
~~~
pelican-quickstart
~~~

Aquí muestro el contenido del script con las opciones que seleccioné

~~~text
Welcome to pelican-quickstart v4.7.2.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files needed by Pelican.


> Where do you want to create your new web site? [.]
> What will be the title of this web site? Demo
> Who will be the author of this web site? Rodrigo Lara
> What will be the default language of this web site? [en] es
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) Y
> What is your URL prefix? (see above example; no trailing slash) https://rodrigolara-cl.github.io
> Do you want to enable article pagination? (Y/n) Y
> How many articles per page do you want? [10] 5
> What is your time zone? [Europe/Rome] America/Santiago
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) y
> Do you want to upload your website using FTP? (y/N) n
> Do you want to upload your website using SSH? (y/N) n
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) n
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) y
Done. Your new project is available at /home/rodrigo/rodrigolara-cl/website
~~~  



## Crear contenido y subirlo a github pages

Crear un documento en markdown(.md) en la carpeta /content/.

En el encabezado se debe colocar la siguiente metadata:

~~~text
Title: Título del post
Date: 2022-06-25 21:05
Modified: 2022-06-25 22:30
Tags: pelican, publishing
Keywords:
Category: Python
Slug: mi-post
Author: Rodrigo Lara
Authors: Autor 1, Autor 2
Summary: Versión corta para el index y el feed
Lang: es
Translation: true or false
Status: draft, hidden or published
Template:
Save as:
Url:
~~~

En la [documentación de Pelican](https://docs.getpelican.com/en/latest/content.html) pueden ver un detalle de lo que significa cada ítem, no es necesario colocarlos todos, pero los obligatorios son el título y la fecha.

Una vez redactado el artículo para visualizarlo en el navegador de manera local.

~~~
make html
make serve
~~~

Podemos visualizar la página en [http://localhost:8000](http://localhost:8000) en el navegador.

Cuando esté listo para ser publicado utilizaremos el siguiente comando.

~~~
make publish
~~~

Sincronizaremos primero el repositorio del código fuente del sitio web.

~~~
git add .
git commit -m "descripcion cambios"
git pull origin main
~~~

Al realizar esto nos pedirá el usuario y la contraseña, que en este caso será el token de acceso que guardamos anteriormente.

Finalmente sincronizaremos la carpeta output hacia el main branch del repositorio que alojará la página web.

~~~text
ghp-import output -b gh-pages
git push https://token-de-acceso@github.com/nombre-usuario/nombre-usuario.github.io.git gh-pages:main
~~~

Luego hay que esperar unos minutos para que la página esté activa en la dirección [nombre-usuario.github.io](nombre-usuario.github.io).



## Comentarios finales

Los mayores problemas que tuve al configurar el sitio con Github Pages fueron debido a las nuevas restricciones de acceso de Github que dejan un poco obsoleto algunos tutoriales por unos pocos detalles. Sin embargo el flujo de trabajo varía un poco solamente y agradezco la información obtenida desde los siguientes enlaces.

- [https://pythonforundergradengineers.com/how-i-built-this-site-1.html](https://pythonforundergradengineers.com/how-i-built-this-site-1.html)
- [https://docs.getpelican.com/en/latest/tips.html](https://docs.getpelican.com/en/latest/tips.html)
- [https://trevorfox.com/2020/03/starting-an-seo-project-with-python-pelican-and-aws/](https://trevorfox.com/2020/03/starting-an-seo-project-with-python-pelican-and-aws/)
- [https://antonellocalamea.medium.com/step-by-step-guide-to-setup-a-web-site-using-pelican-and-gitpages-5de976ae44cb](https://antonellocalamea.medium.com/step-by-step-guide-to-setup-a-web-site-using-pelican-and-gitpages-5de976ae44cb)


Luego de tener el procedimiento probado y funcionando los siguientes pasos son elegir y configurar un tema, crear el contenido, utilizar las funciones de Pelican y de los temas, y utilizar plugins existentes o crear nuevos en caso de necesitar funciones especiales para crear el sitio web estático perfecto para ti.

<div class="commentbox"></div>
<script src="https://unpkg.com/commentbox.io/dist/commentBox.min.js"></script>
<script>commentBox('5676459674828800-proj')</script>
