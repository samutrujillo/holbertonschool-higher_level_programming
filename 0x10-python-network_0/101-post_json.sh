#!/bin/bash
# Script that sends a JSON POST
curl -s "{$1}" -X POST -H "Content-Type: application/json" -d @$2
