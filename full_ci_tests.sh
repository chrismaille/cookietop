#!/usr/bin/env bash

# Test first with DynamoDB (default)
# then other options

COOKIECUTTER_CONFIG=./cookie_both.yml make ci && \
COOKIECUTTER_CONFIG=./cookie_rds.yml make ci && \
COOKIECUTTER_CONFIG=./cookie_dynamo.yml make ci && \
COOKIECUTTER_CONFIG=./cookie_none.yml make ci && \
COOKIECUTTER_CONFIG=./cookie_minimal.yml make ci && \