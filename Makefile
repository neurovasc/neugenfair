# Makefile for neugenfair
# Run `make all` to regenerate models, SHACL, and docs

SCHEMAS_DIR=schemas
MODELS_DIR=neugenfair/models
SHACL_FILE=$(SCHEMAS_DIR)/model_shacl.ttl
DOCS_DIR=$(SCHEMAS_DIR)/docs
DOCS_FILE=$(DOCS_DIR)/model.html

# List of individual model schema files
MODEL_SCHEMAS=$(wildcard $(SCHEMAS_DIR)/model_*.yaml)

# Default target: run everything
all: models shacl docs

# Generate Python dataclasses: one class per file
models: $(MODEL_SCHEMAS)
	@mkdir -p $(MODELS_DIR)
	@for schema in $(MODEL_SCHEMAS); do \
		name=$$(basename $$schema .yaml | cut -d'_' -f2 | tr '[:upper:]' '[:lower:]'); \
		echo "Generating $$name.py from $$schema"; \
		poetry run linkml generate python $$schema > $(MODELS_DIR)/$$name.py; \
	done

# Generate SHACL constraints from all schemas
shacl:
	poetry run linkml generate shacl $(SCHEMAS_DIR)/model.yaml > $(SHACL_FILE)

# Generate HTML docs
docs: shacl
	poetry run linkml generate doc --directory ${DOCS_DIR} $(SCHEMAS_DIR)/model.yaml

# Cleanup generated files
clean:
	rm -f $(SHACL_FILE) $(DOCS_FILE)
	find $(MODELS_DIR) -type f ! -name '__init__.py' -delete
