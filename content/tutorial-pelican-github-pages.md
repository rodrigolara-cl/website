Title: Tutorial Pelican con Github Places
Tags: pelican, github, github-pages
Category: Blog
Slug: tutorial-pelican-github-pages
Author: Rodrigo Lara
Summary: En este tutorial mostraré el workflow actualizado al 2022 para realizar páginas web en pelican y sincronizarlas con git hacia github.
Lang: es
Translation: false
Status: draft

# Tutorial para realizar página web con Pelican en Github pages

Hace años por allá el 2013 probé sitios web estáticos en github pages e intenté usar sin mucho éxito Jekyll y Pelican. En general la curiosidad no llega más lejos que la necesidad y si bien me ha tocado trabajar con sitios web en wordpress y ahora último prestashop debido a que son las tecnologías usadas en las páginas web de mis últimos dos trabajos, no son lo que necesito actualmente para crear mi página web personal. Utilicé Google Sites con éxito para un proyecto de baterías junto con un amigo, pero la selección fue restringida a que debía ser fácil de escribir contenido y configurar. Bueno ninguna de las opciones cumple con mis requisitos personales los cuales son:

- Posibilidad de integración de jupyter notebooks.

- Seguimiento de cambios con GitHub y uso de alojamiento gratuito de github pages.

- Capacidad de personalización en python a futuro.

Antes de volver a utilizar Pelican, vi tutoriales de Jekyll pero lamentablemente no logré instalar las librerías necesarias en OpenSuse que es el sistema que utilizo actualmente, por lo que volví al confiable python que tengo instalado gracias a Anaconda.
Los tutoriales que encontré no me permitieron ejecutar todos los pasos como corresponde y perdí bastante tiempo tratando de entender por qué no lograba subir el sitio a github.

En este tutorial mostraré el procedimiento actualizado al 2022 para realizar páginas web en pelican y sincronizarlas con git hacia github.

## Creación de repositorios en GitHub

Github Pages permite una sola página web personal con el formato [https://nombre.github.io](https://nombre.github.io) pero no restringe la cantidad de las páginas de proyecto que se accederían [https://nombre.github.io/nombre-proyecto](https://nombre.github.io/nombre-proyecto).

La mayoría de los tutoriales explican como realizarlo en las páginas de proyecto, y la documentación de pelican explica sólo la parte final de subir el sitio para ambos casos, por lo que existía un vacío y algunas incompatibilidades con el estado actual de github y los tutoriales.

El primer paso es crear dos repositorios en github, uno para alojar la página web, y otro para alojar el código de la página para realizar el seguimiento de cambios.

Al crear el repositorio para alojar la página web debemos colocar en el nombre del repositorio nombre-de-usuario.github.io, por ejemplo:

![Imagen 1]({static}/images/githubusuario.png)
