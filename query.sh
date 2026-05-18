#!/usr/bin/env bash

set -e

# --------------------------------------------------
# Check arguments
# --------------------------------------------------

if [ "$#" -ne 1 ]; then
    echo "Usage: ./query.sh path/to/query.sparql"
    exit 1
fi

QUERY_FILE="$1"

# --------------------------------------------------
# Check mapping file
# --------------------------------------------------

if [ ! -f "./mappings/full_mapping.ttl" ]; then
    echo "ERROR: ./mappings/full_mapping.ttl is missing."
    echo "Please run ./run.sh first."
    exit 1
fi

# --------------------------------------------------
# Check query file
# --------------------------------------------------

if [ ! -f "$QUERY_FILE" ]; then
    echo "ERROR: Query file '$QUERY_FILE' does not exist."
    exit 1
fi

# --------------------------------------------------
# Execute query
# --------------------------------------------------

echo "Executing SPARQL query..."

./ontop-cli-5/ontop query \
    --mapping mappings/full_mapping.ttl \
    --properties ontop.properties \
    --query "$QUERY_FILE"