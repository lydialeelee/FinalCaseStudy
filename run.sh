#!/usr/bin/env bash
set -e

echo "Building image..."
docker build -t tip-api:latest .

echo "Running container..."
docker run --rm -p 8080:8080 --env-file .env.example tip-api:latest
