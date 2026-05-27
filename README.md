# S355 Ontop Demo
A demonstration of the S355 dataset mapped with YARRRML and accessed through Ontop.

## Prerequisites
The following software must be installed and available in PATH:
- Java 17+
- Node.js 20+ (includes npm)
- Python 3.10+ with pip

## Quick Start

Linux/macOS:
```bash
chmod +x setup.sh materialize.sh query.sh endpoint.sh
./setup.sh
./materialize.sh
./query.sh queries/example.sparql
```

Windows:
```bat
setup.bat
materialize.bat
query.bat queries\example.sparql
```
## Running the Pipeline
For users to successfully run the complete process, first 
```bash
./setup.sh
```
should be executed (for Windows users `setup.bat`). This checks the prerequisites,
installs the npm and Python dependencies, and creates a Python virtual environment. 
After successful setup, the user should initially run
```bash
./materialize.sh
```
once to produce the R2RML mapping (For Windows users `materialize.bat`). 
During this step, the graph is also materialized into `graph.ttl`.

Afterwards, Ontop can be used to query the H2 database via
```bash
./query.sh <path to .sparql file>
```
or `./query.bat` on Windows.

## Description of the complete Pipeline
For users that have difficulties with using any of the provided scripts or are 
interested in a more detailed description of the process, we provide a detailed
step-by-step guide here.

The following commands are written for Linux/macOS shells. 
On Windows, equivalent commands can be executed in `cmd.exe`. 
In multiline commands, line continuations using `\` must be replaced by `^`.

### Producing the SQL file
In the first step, we produce an SQL file which can afterwards use to create
a relational database (here H2, though other systems are possible as well).
The `createDB.py` together with `charpyData.py`, `tensileData.py`, and `sonicResonanceSecondaryData.py`
achieve this using the python packages `pyexcel` and/or `pyexcel-xlsx`. 
For this one can create a virtual environment by running
```bash
python3 -m venv .venv
```
and activate it using
```bash
source .venv/bin/activate
```
To install the Python dependencies we first upgrade pip
```bash
pip install --upgrade pip
```
followed by
```bash
pip install -r config/requirements.txt
```
Once these steps were successful, running
```bash
python python_scripts/createDB.py
```
should produce a `s355.sql` file given the project structure as is.

### Creating a H2 database
Once the `s355.sql` file is produced we can use it to create a H2 database
by running:
```bash
java -cp ontop-cli-5/jdbc/h2.jar org.h2.tools.RunScript \
	-url jdbc:h2:./H2s355 \
	-user sa \
	-password "" \
	-script s355.sql
```
which should produce the database file `H2s355.mv.db`. Note: If the database already exists
running the above will not succeed. To rerun, the database file(s) must first be deleted
by running
```bash
rm -f H2s355.mv.db
rm -f H2s355.trace.db
```

### Producing the R2RML mapping
To use Ontop as a SPARQL endpoint for the relational database, we need to provide an R2RML mapping.
We use the `yarrrml-parser` to produce this mapping out of the `.yml` files provided in `/mappings`.
Since the `yarrrml-parser` is an npm package, it must first be installed via
```bash
npm --prefix ./config install
```
With the `yarrrml-parser` installed, we can produce the R2RML mapping by running
```bash
npx --prefix ./config yarrrml-parser \
	-i mappings/sheet1.yml \
	-i mappings/charpy.yml \
	-i mappings/tensile.yml \
	-i mappings/sonic_resonance.yml \
	-o mappings/full_mapping.ttl -f r2rml
```
which should produce the file `mappings/full_mapping.ttl`.

### Materializing the graph with Ontop
Finally, we can materialize a knowledge graph from the relational database using Ontop.
For this, we run
```bash
./ontop-cli-5/ontop materialize \
	--mapping mappings/full_mapping.ttl \
	--properties config/ontop.properties \
	--output graph.ttl \
	--format turtle 
```
which will produce the file `graph.ttl`.
The `ontop.properties` file contains the JDBC connection configuration for the H2 database.

### Querying with Ontop
As an alternative to materializing we can also directly query the relational database
using Ontop and the provided mapping.
We can write a SPARQL query, store it in some `.sparql` file and then run
```bash
./ontop-cli-5/ontop query \
  --mapping mappings/full_mapping.ttl \
  --properties config/ontop.properties \
  --query <location of .sparql file>
```

### Using Ontop as a Virtual Knowledge Graph
Ontop can be used as a virtual knowledge graph by using the `endpoint.sh` script (`endpoint.bat` on Windows).
Alternatively we can run
```bash
./ontop-cli-5/ontop endpoint \
	--mapping mappings/full_mapping.ttl \
	--properties config/ontop.properties 
```
Afterwards the endpoint can be accessed on `localhost:8080`, e.g. by typing it as an url in the web browser.