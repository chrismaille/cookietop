#!/bin/bash

make build_dependencies

sam local start-api \
  --host 0.0.0.0 \
  --debug \
  -n local.json \
  --docker-volume-basedir /app \
  --docker-network lambda-local \
  --container-host host.docker.internal
