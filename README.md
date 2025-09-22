## Coding project context and goals
### Approach
This repository contains model oriented code for a model based strategy of transforming the
ICAN dataset into Linked Data. Previous projects were based on functionnal programming and are hard to maintain.
Moreover the transformation process was split into \
VCF --> Linked Data and \
clinical CSV --> Linked Data. \
### Dataset
Here the approach tries to be more comprehensive. The focus is real data, with many missing values. The model needs to be
the driving force of the transformation because for maintenance purpose I cannot keep creating exceptions and exclusion criteria
in my 'if loops' in the previous repositories. \
### Previous work
The previous coding project with similar goals are: \
[etl4fairdata_AIC](https://gitlab.univ-nantes.fr/bodrug-a/etl4fairdata_AIC) and \
[etl4sphn_AIC](https://gitlab.univ-nantes.fr/bodrug-a/etl4sphn_aic) \
In addition to a model driven approach, this coding project shall satisfy the need for detailed documentation and creation of shacl constraints. This will be achieved by using LinkML. \
### Goals
The final Linked Data should be generated both in RDF and JSON-LD, for swift compatibility with the Beacon production implementation (Mongo database). Documentation and shacl constraints will be generated automatically.

## The real dataset: ICAN dataset
Blah. 

## Schema Documentation

[MkDocs](https://bodrug-a.univ-nantes.io/neugenfair) \
[pyLODE](https://bodrug-a.univ-nantes.io/neugenfair/pylode) \
[Alternative link](https://neugenfair-caffb5.univ-nantes.io/)

