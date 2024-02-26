
# Deployment Guide for Chatroom Simulator

Hey there! This folder is your go-to guide for getting the Chatroom Simulator up and running on k3s, which is pretty awesome for deploying Kubernetes stuff without the bloat. Perfect for when you want to keep things light and speedy.

## What's Inside?

- `/docker`: This is where the magic Dockerfile lives. It's what we use to bake our app into a neat container image.
- `/k8s`: Here be the Kubernetes manifest files. They're like the blueprint that tells k3s how to deploy and run our chatroom app.

## Getting Ready

Before you dive in, make sure you've got:
- k3s running somewhere. If not, check out [k3s.io](https://k3s.io/) to get it set up.
- Docker, because we need to containerize our app.
- `kubectl`, hooked up to your k3s cluster, so you can tell Kubernetes what to do.

## Building the App

1. Head over to `/docker` and build our app's Docker image:
    ```bash
    docker build -t your-registry/chatroom-simulator:latest .
    ```
2. Push that shiny new image to your Docker registry:
    ```bash
    docker push your-registry/chatroom-simulator:latest
    ```

## Deploying to k3s

1. Update the image path in the Kubernetes manifests under `/k8s` to point to your Docker image.
2. Let k3s know about our app by applying the manifests:
    ```bash
    kubectl apply -f k8s/
    ```
3. Check if everything's cool and running:
    ```bash
    kubectl get all
    ```

## Testing It Out

After deployment, try hitting the app through the service's ClusterIP or the Ingress endpoint, if you've set that up. `kubectl` is your friend for finding out IPs and stuff.

## Tidying Up

Done playing? Clean up by removing the stuff you deployed:
```bash
kubectl delete -f k8s/
```

## Wanna Contribute?

Got ideas to make this deployment smoother? Jump into the main project's CONTRIBUTING.md and let us know!
