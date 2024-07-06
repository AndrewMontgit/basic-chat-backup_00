#!/bin/bash

# run.sh
# Helper script to run a `docker compose up` command with additional user (UID) and group (GID) environment variables.
# This enables the container to run as the same user and group in the host operating system, so that the game files that get mounted at runtime are accessible in the container.

set -e  # BASH debug mode. Exits on errors (-e).

# Get the current user's UID and GID
CURRENT_UID=$(id -u)
CURRENT_GID=$(id -g)

# Export these variables with custom names
export MY_UID=$CURRENT_UID
export MY_GID=$CURRENT_GID

# Run docker compose with the updated environment variables
# Use `docker compose run evennia` rather than `docker compose up` to ensure that the terminal is interactive.
MY_UID=$CURRENT_UID MY_GID=$CURRENT_GID docker compose run evennia
