#!/bin/bash
set -e

platform="linux/amd64,linux/arm64/v8"
scope="marvindv"
image_name="immich-scripts"
tag=$(git rev-parse --short HEAD)

# Build the image for multiple platforms and directly publish them to Docker Hub using buildx.
function publish {
  docker buildx build --platform "$platform" --push -t $scope/$image_name:$tag -t $scope/$image_name:latest .

  echo ""
  echo "Docker images are now available on Docker Hub with $scope/$image_name:latest and $scope/$image_name:$tag for platforms $platform"
}

# Build the image for multiple platforms without publishing them.
function dry_run {
  docker buildx build --platform "$platform" .

  echo ""
  echo "Docker images are built successfully"
}

# Build the image for the local platform for development usage.
function build_local {
  docker build -t $image_name:$tag -t $image_name:latest .

  echo ""
  echo "Docker image is now available locally with $image_name:latest and $image_name:$tag"
}

echo "Do you want to build"
echo "  - a local (d)evelopment image, or"
echo "  - multi-platform images as a dry (r)un to see if the build works, or"
echo "  - multi-platform images for direct (p)ublish to Docker Hub?"
read -p "(D)evelopment/Dry (R)un/(P)ublish: " choice

case $choice in
[pP]*) publish ;;
[rR]*) dry_run ;;
[dD]*) build_local ;;
*) exit ;;
esac
