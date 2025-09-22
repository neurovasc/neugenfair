# Makefile for neugenfair
# Run `make all` to regenerate models, SHACL, and docs

# neurogenfair/
MODELS_DIR=neugenfair/models # directory containing generated python models
MODELS_PYTHON=neugenfair/models/neugenfairmodel.py # file containing generated python models
# schemas/
SCHEMAS_DIR=schemas
MODEL_YAML=$(SCHEMAS_DIR)/neugenfairmodel.yaml # merged model from hand-crafted YAML files in schemas/models/model_*.yaml
SHACL_FILE=$(SCHEMAS_DIR)/neugenfairmodel_shacl.ttl # generated SHACL file, with linkml generate shacl
MODEL_OWLTTL=$(SCHEMAS_DIR)/neugenfairmodel.owl.ttl # generated OWL TTL file, with linkml generate owl
# schemas/docs
DOCS_DIR=$(SCHEMAS_DIR)/docs
DOCS_FILE=$(DOCS_DIR)/model.html
# schemas/pylode
PLODE_DIR=$(SCHEMAS_DIR)/pylode

# List of individual model schema files
MODEL_SCHEMAS=$(wildcard $(SCHEMAS_DIR)/models/model_*.yaml) # hand crafted YAML model files

# Default target: run everything
all: mergemodels dataclasses shacl docs pylode

# Merge individual schema files into one big schema file
# For my own mental sanity, I like to keep individual model files separate
# But for linkML and pyLODE, it's better to have everything in a single file
mergemodels:
	@echo "Merging schema files into $(MODEL_YAML)"
	poetry run python3 schemas/neugenfairmodel_merger.py $(MODEL_YAML)

# Generate Python dataclasses with LinkML Python generator
dataclasses: 	
	@echo "Generating Python models → $(MODELS_DIR)"
	poetry run linkml generate python $(MODEL_YAML) > $(MODELS_PYTHON)

# Generate SHACL constraints with LinkML SHACL generator
shacl:
	@echo "Generating SHACL constraints → $(SHACL_FILE)"
	poetry run linkml generate shacl $(MODEL_YAML) > $(SHACL_FILE)

# Generate Markdown docs with LinkML doc generator
docs: 
	@mkdir -p $(DOCS_DIR)
	@echo "Generating LinkML markdown documentation → $(DOCS_DIR)"
	poetry run linkml generate doc --directory ${DOCS_DIR} $(MODEL_YAML)
	poetry run mkdocs build

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
