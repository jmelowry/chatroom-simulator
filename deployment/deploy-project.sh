#!/bin/bash

# color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_green() {
    echo -e "${GREEN}$1${NC}"
}

print_yellow() {
    echo -e "${YELLOW}$1${NC}"
}

print_red() {
    echo -e "${RED}$1${NC}"
}

confirm_installation() {
    print_yellow "Proceed with installation? [Y/n]: "
    read -p "" response
    case "$response" in
        [nN][oO]|[nN]) exit 1 ;;
        *) ;;
    esac
}

check_and_install_homebrew() {
    if ! command -v brew &> /dev/null; then
        print_yellow "Homebrew is not installed."
        confirm_installation
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    else
        print_green "Homebrew is already installed."
    fi
}

check_docker() {
    if ! command -v docker &> /dev/null; then
        print_red "Docker is not installed."
        case "$OSTYPE" in
            darwin*)  INSTALL_URL="https://docs.docker.com/desktop/install/mac-install/" ;;
            linux*)   INSTALL_URL="https://docs.docker.com/desktop/install/linux-install/" ;;
            msys*)    INSTALL_URL="https://docs.docker.com/desktop/install/windows-install/" ;;
            *)        print_red "Unsupported OS. Please install Docker manually."; return ;;
        esac
        print_yellow "Please install Docker Desktop for your OS: $INSTALL_URL"
        print_yellow "After installation, press any key to continue..."
        read -n 1 -s -r
    else
        print_green "Docker is already installed."
    fi
}

check_docker_daemon() {
    if ! docker info &> /dev/null; then
        print_red "The Docker daemon is not running."
        print_yellow "Please start the Docker daemon before proceeding, then press any key to continue..."
        read -n 1 -s -r
        check_docker_daemon
    else
        print_green "The Docker daemon is running."
    fi
}

list_brewfile_dependencies() {
    print_yellow "Dependencies listed in Brewfile:"
    while read line; do
        if [[ "$line" =~ ^brew ]]; then
            print_green " - $(echo "$line" | cut -d '"' -f2)"
        elif [[ "$line" =~ ^cask ]]; then
            print_green " - $(echo "$line" | cut -d '"' -f2) (cask)"
        fi
    done < Brewfile
}
install_dependencies_with_brewfile() {
    print_yellow "Installing dependencies with Brewfile..."
    list_brewfile_dependencies
    confirm_installation
    brew bundle
}

build_image() {  
    local dockerfile_path="$1"  
    local image_tag="$2"  
    docker build -t "$image_tag" "$dockerfile_path"  
    echo "Image $image_tag has been built successfully."  
}

start_kind_cluster() {
    local config_file="$1"
    # Check if a Kind cluster by the name 'kind' already exists
    if kind get clusters | grep -q "^kind$"; then
        print_yellow "Kind cluster 'kind' already exists. Skipping creation."
    else
        kind create cluster --config "$config_file" || { echo "Failed to create Kind cluster"; exit 1; }
        print_green "Kind cluster has been set"
    fi
}

load_image_into_kind_cluster() {
    local image_tag="$1"
    kind load docker-image "$image_tag" --name chatroom-simulator || { echo "Failed to load image into Kind cluster"; exit 1; }
    print_green "Image $image_tag has been loaded into the Kind cluster"
}

deploy_project() { 
    echo "Checking and installing Homebrew..."  
    check_and_install_homebrew  
    
    echo "Checking Docker installation..."  
    check_docker

    echo "Checking Docker daemon..."  
    check_docker_daemon
    
    echo "Installing dependencies listed in Brewfile..."  
    install_dependencies_with_brewfile  
    
    echo "Creating the Kind cluster..."  
    start_kind_cluster "./k8s-config/kind-config.yaml"  
    
    echo "Building Docker image for chatroom simulator..."
    cd ../app || { echo "Failed to change directory"; exit 1; }
    build_image . "chatroom_simulator:latest"
    cd ../deployment || { echo "Failed to change directory"; exit 1; }

    echo "Loading the app image into the Kind cluster..."
    load_image_into_kind_cluster "chatroom_simulator:latest"

    echo "deploying app to cluster"
    kubectl apply -f ../k8s-config/deployment.yaml --context kind-chatroom-simulator

    echo "Project deployment complete."
}

deploy_project
