# Create main project folder
mkdir -p neugenfair

# Move into it
cd neugenfair

# Top-level files
touch pyproject.toml README.md .gitignore Makefile

# Tests folder
mkdir -p tests
touch tests/test_individual.py

# Main package folder
mkdir -p neugenfair/{models,parsers,mappers,exporters,validators}
touch neugenfair/__init__.py
touch neugenfair/pipeline.py

# Models
touch neugenfair/models/__init__.py \
      neugenfair/models/individual.py \
      neugenfair/models/variant.py \
      neugenfair/models/disease.py

# Parsers
touch neugenfair/parsers/__init__.py \
      neugenfair/parsers/csv_parser.py \
      neugenfair/parsers/vcf_parser.py

# Mappers
touch neugenfair/mappers/ontology_mapper.py

# Exporters
touch neugenfair/exporters/rdf_exporter.py

# Validators
touch neugenfair/validators/shacl_validator.py

# Schemas folder for LinkML + docs
mkdir -p schemas
touch schemas/model.yaml
