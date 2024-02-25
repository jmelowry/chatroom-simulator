# Use Alpine Linux as the base image
FROM alpine:latest

# Install curl and ca-certificates
RUN apk add --no-cache curl ca-certificates bash

# Download kubectl
ARG KUBECTL_VERSION="v1.20.0"
RUN curl -LO "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl" \
    && chmod +x ./kubectl \
    && mv ./kubectl /usr/local/bin/kubectl

# Copy your kubeconfig file into the container
# Make sure to place the k3s kubeconfig file in the same directory as this Dockerfile
# and name it k3s-kubeconfig.yaml
COPY k3s-kubeconfig.yaml /root/.kube/config

# Set the KUBECONFIG environment variable
ENV KUBECONFIG=/root/.kube/config

# Set a default command for the container
CMD ["kubectl", "version", "--client"]