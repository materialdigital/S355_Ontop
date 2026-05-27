# Third-Party Notices

This project includes or depends on third-party software.

Project license recommendation implemented in this repository:
- Apache License 2.0 for original project code (see LICENSE).

Date of inventory: 2026-05-22

## 1) Bundled third-party components (Ontop CLI distribution)

The folder `ontop-cli-5/copyright` contains third-party license texts.

License summary (27 files):
- Apache-2.0: 16
- BSD-3-Clause: 3
- BSD-2-Clause: 1
- MIT: 2
- EPL-1.0: 1
- EPL-2.0: 1
- EDL-1.0: 1
- MPL-2.0: 1
- EPL-1.0 OR LGPL-2.1: 1

Component-to-license mapping based on bundled license files:
- AIRLINE: Apache-2.0
- ANTLR: BSD-3-Clause
- COMMONS: Apache-2.0
- FINDBUGSJSR305: Apache-2.0
- FUNCTIONALJAVA: BSD-3-Clause
- GSON: Apache-2.0
- GUAVA: Apache-2.0
- GUICE: Apache-2.0
- H2: MPL-2.0
- HIKARICP: Apache-2.0
- JACKSON: Apache-2.0
- JETTY: Apache-2.0
- JGRAPHT: EPL-2.0
- JSONLDJAVA: BSD-3-Clause
- JSQLPARSER: Apache-2.0
- JUNIT: EPL-1.0
- LOGBACK: EPL-1.0 OR LGPL-2.1
- OSGI: Apache-2.0
- OWLAPI: Apache-2.0
- PROTEGE: BSD-2-Clause
- R2RMLAPI: Apache-2.0
- RDF4J: EDL-1.0
- SLF4J: MIT
- SPRING: Apache-2.0
- TOM4J: MIT
- TOMCAT: Apache-2.0
- URLBUILDER: Apache-2.0

## 2) Node.js dependencies

Sources:
- `config/package.json`
- `config/package-lock.json`

Direct dependency:
- @rmlio/yarrrml-parser 1.12.2 (MIT)

Resolved lockfile inventory summary (122 packages):
- MIT: 67
- ISC: 42
- BlueOak-1.0.0: 8
- BSD-3-Clause: 2
- BSD-2-Clause: 1
- Unlicense: 1
- UNKNOWN: 1

Known unknown entry:
- bkit 2.1.3 (no license field in lockfile metadata and no license value from npm view)

## 3) Python dependencies

Source:
- `config/requirements.txt`

Direct dependencies:
- pyexcel==0.7.4 (New BSD)
- pyexcel-xlsx==0.6.1 (New BSD)

Declared transitive dependencies from package metadata:
- lml (New BSD)
- pyexcel-io (New BSD)
- texttable (MIT)
- openpyxl (MIT)

## 4) Compliance notes

- Keep all license files under `ontop-cli-5/copyright` in redistributions that include Ontop CLI.
- Preserve copyright and license notices for all bundled/redistributed third-party components.
- If modifying components under reciprocal licenses (for example MPL/EPL/LGPL), follow obligations specific to those modified components.
- Resolve or replace unknown-license dependencies (currently bkit 2.1.3) before external distribution.

## 5) Disclaimer

This notice is a technical inventory and not legal advice.
For production release or commercial distribution, have legal counsel review the final bill of materials and license obligations.
