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

```
docker build -t test_image:tag .
```
Crea una imagen leyendo un dockerfile.
- test_image es el repo.
- tag es el tag.
- . es la ruta

```
docker run test_image:tag .
```
Crea un contenedor.
- Con el parametro -p se puede definir el puerto. Ej: -p 80:80  el primer número es el puerto del equipo, el segundo el del contenedor.

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

# Git Cheat Sheet

```
git branch -d localBranchName
```
Borra una rama local. localBranchName es el nombre de la rama.

```
git push origin --delete remoteBranchName
```
Borra una rama remota. remoteBranchName es el nombre de la rama.


# k8s

https://kubernetes.io/docs/tutorials/hello-minikube/

kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1


```
kubectl get nodes
kubectl create namespace default-mem-example
```

```
kubectl get pods --all-namespaces
kubectl describe pods
kubectl proxy
```

```
export POD_NAME="$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')"
echo Name of the Pod: $POD_NAME
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME:8080/proxy/
kubectl logs "$POD_NAME"
kubectl exec "$POD_NAME" -- env
kubectl exec -ti $POD_NAME -- bash
cat server.js
curl http://localhost:8080
```

```
kubectl get services
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
kubectl describe services/kubernetes-bootcamp
export NODE_PORT="$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')"
echo "NODE_PORT=$NODE_PORT"
curl http://127.0.0.1:"$NODE_PORT"
```

```
kubectl describe deployment
kubectl get pods -l app=kubernetes-bootcamp
export POD_NAME="$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')"
echo "Name of the Pod: $POD_NAME"
kubectl label pods "$POD_NAME" version=v1
kubectl describe pods "$POD_NAME"
kubectl get pods -l version=v1
```
```
kubectl delete service -l app=kubernetes-bootcamp
kubectl get services
curl http://127.0.0.1:"$NODE_PORT"
kubectl exec -ti $POD_NAME -- curl http://localhost:8080
```

```
kubectl expose deployment/kubernetes-bootcamp --type="LoadBalancer" --port 8080
kubectl get deployments
kubectl get rs
kubectl scale deployments/kubernetes-bootcamp --replicas=4
kubectl get deployments
kubectl get pods -o wide
kubectl describe deployments/kubernetes-bootcamp
```

```
kubectl scale deployments/kubernetes-bootcamp --replicas=2
kubectl get deployments
kubectl get pods -o wide
```


https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/
```
kubectl get deployments
kubectl get pods
kubectl describe pods
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=docker.io/jocatalin/kubernetes-bootcamp:v2
kubectl get pods
export NODE_PORT="$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')"
echo "NODE_PORT=$NODE_PORT"
curl http://127.0.0.1:"$NODE_PORT"
kubectl rollout status deployments/kubernetes-bootcamp
kubectl describe pods
```

```
kubectl delete deployments/kubernetes-bootcamp services/kubernetes-bootcamp
```

```
kubectl describe services/kubernetes-bootcamp
export NODE_PORT="$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')"

echo NODE_PORT=$NODE_PORT
curl http://127.0.0.1:"$NODE_PORT"
```


```
kubectl get svc --namespace default -w moodle-1731150377
```
```
kubectl get all -A
```
# helm

```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm search repo bitnami
helm install bitnami/moodle --generate-name

sudo helm uninstall --kubeconfig=/etc/rancher/k3s/k3s.yaml moodle-1731150377 
```

# Kompose

```
curl -L https://github.com/kubernetes/kompose/releases/download/v1.34.0/kompose-linux-amd64 -o kompose
chmod +x kompose
sudo mv ./kompose /usr/local/bin/kompose
```

# docker registry

https://www.docker.com/blog/how-to-use-your-own-registry-2/

```
docker run -d -p 5000:5000 --name registry registry:2.8.3
```

```
kubectl create secret docker-registry <nombre-del-secreto> --docker-server=http://192.168.0.19:5000 --docker-username=<usuario> --docker-password=<contraseña>
```

https://docs.github.com/es/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-with-a--data-variablesproductpat_v1-

```
export CR_PAT=YOUR_TOKEN
echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin
docker push ghcr.io/NAMESPACE/IMAGE_NAME:latest

```