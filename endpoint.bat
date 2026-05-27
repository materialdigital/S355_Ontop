@echo off
setlocal

echo Setting up endpoint. Once finished visit the url "localhost:8080" to access it.

ontop-cli-5\ontop endpoint ^
	--mapping mappings/full_mapping.ttl ^
	--properties config/ontop.properties
