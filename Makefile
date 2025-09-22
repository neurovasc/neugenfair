# Makefile for neugenfair
# Run `make all` to regenerate models, SHACL, and docs

SCHEMAS_DIR=schemas
MODELS_DIR=neugenfair/models
MODEL_YAML=$(SCHEMAS_DIR)/neugenfairmodel.yaml # merged model from hand-crafted YAML files in schemas/models/model_*.yaml
MODEL_TTL=$(SCHEMAS_DIR)/neugenfairmodel.ttl # generated RDF file, wirh linkml generate rdf
SHACL_FILE=$(SCHEMAS_DIR)/neugenfairmodel_shacl.ttl # generated SHACL file, with linkml generate shacl
MODEL_OWLTTL=$(SCHEMAS_DIR)/neugenfairmodel.owl.ttl # generated OWL TTL file, with linkml generate owl
DOCS_DIR=$(SCHEMAS_DIR)/docs
PLODE_DIR=$(SCHEMAS_DIR)/pylode
DOCS_FILE=$(DOCS_DIR)/model.html

# List of individual model schema files
MODEL_SCHEMAS=$(wildcard $(SCHEMAS_DIR)/models/model_*.yaml) # hand crafted YAML model files

# Default target: run everything
all: models shacl docs pylode

# Generate Python dataclasses: one class per file in models/ directory
# Generate RDF model as well, to be used by pyLODE
models: $(MODEL_SCHEMAS)
	@mkdir -p $(MODELS_DIR)
	@echo "Generating Python models → $(MODELS_DIR)"
	@for schema in $(MODEL_SCHEMAS); do \
		name=$$(basename $$schema .yaml | cut -d'_' -f2 | tr '[:upper:]' '[:lower:]'); \
		echo "Generating $$name.py from $$schema"; \
		poetry run linkml generate python $$schema > $(MODELS_DIR)/$$name.py; \
	done
	@echo "Merging schema files into $(MODEL_YAML)"
	poetry run python3 schemas/neugenfairmodel_merger.py
	@echo "Generating RDF model → $(MODEL_TTL)"
	poetry run linkml generate rdf $(MODEL_YAML) > $(MODEL_TTL)
	

# Generate SHACL constraints from all schemas
shacl:
	@mkdir -p $(SCHEMAS_DIR)
	@echo "Generating SHACL constraints → $(SHACL_FILE)"
	poetry run linkml generate shacl $(MODEL_YAML) > $(SHACL_FILE)

# Generate Markdown docs with LinkML doc generator
docs: 
	@mkdir -p $(DOCS_DIR)
	@echo "Generating LinkML markdown documentation → $(DOCS_DIR)"
	poetry run linkml generate doc --directory ${DOCS_DIR} $(MODEL_YAML)

# Generate ontology-style HTML docs with pyLODE, using the SHACL file
pylode: 
	@mkdir -p $(PLODE_DIR)
	@echo "Generating ontology documentation with pyLODE → $(PLODE_DIR)/index.html"
	poetry run linkml generate owl $(MODEL_YAML) > $(MODEL_OWLTTL)
	poetry run pylode $(MODEL_OWLTTL) -o $(PLODE_DIR)/index.html


# Cleanup generated files
clean:
	rm -f $(SHACL_FILE) $(DOCS_FILE)
	find $(MODELS_DIR) -type f ! -name '__init__.py' -delete
	rm -rf $(PLODE_DIR) $(DOCS_DIR)
