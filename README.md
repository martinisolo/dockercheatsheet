# Docker Cheat Sheet

## Contenedores

```
docker container list --all
```
Lista los contenedores que están en uso.
- Con el parametro --all se muestran todos

```
docker start 7d11263ece2d
```
Inicia un contenedor. 7d11263ece2d es el 'CONTAINER_ID'

```
docker stop 7d11263ece2d
```
Detiene un contenedor. 7d11263ece2d es el 'CONTAINER_ID'

```
docker container remove 7d11263ece2d
```
Elimina un contenedor.

```
docker exec -it nombre-container /bin/bash
```
Abre una consola interactiva con un contenedor activo.

## Imagenes

```
docker image list --all
```
Lista las imagenes.
- Con el parametro --all se muestra todas las imagenes.

```
docker image remove c712b1aa90b7
```
Elimina una imagen. c712b1aa90b7 es la 'IMAGE_ID'

# Docker Compose Cheat Sheet

```
docker-compose up --detach
```
Inicia los servicios.
- Con el parametro --detach se inician en segundo plano.
- Con el parametro --build se contruyen las imagenes antes de iniciarlas.

```
docker-compose down
```
Detiene los servicios


# Laravel Cheat Sheet

```
php artisan migrate:refresh --seed
```
Regenera la BBDD con las migrations.
- El parameto --seed hace que tambien se añadan los datos a la tabla.


```
php artisan route:list
```
Muestra la lista de rutas.
