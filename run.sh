#!/usr/bin/env bash

set -e

echo "creating sql-file..."
source .venv/bin/activate
python python_scripts/createDB.py

echo "removing old H2 database..."
rm -f H2s355.mv.db
rm -f H2s355.trace.db

echo "creating H2 database..."
java -cp ontop-cli-5/jdbc/h2.jar org.h2.tools.RunScript \
  -url jdbc:h2:./H2s355 \
  -user sa \
  -password "" \
  -script s355.sql

echo "parsing YARRRML files to create r2rml mapping..."
npx --prefix ./config yarrrml-parser \
	-i mappings/sheet1.yml \
	-i mappings/charpy.yml \
	-i mappings/tensile.yml \
	-i mappings/sonic_resonance.yml \
	-o mappings/full_mapping.ttl -f r2rml

echo "materializing graph with ontop..."
./ontop-cli-5/ontop materialize \
	--mapping mappings/full_mapping.ttl \
	--properties config/ontop.properties \
	--output graph.ttl \
	--format turtle 

echo "graph successfully materialized to graph.ttl"