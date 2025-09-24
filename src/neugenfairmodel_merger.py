import sys
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.linkml_model.meta import SchemaDefinition, Prefix
from linkml_runtime.dumpers import yaml_dumper

if len(sys.argv) < 3:
    print("Usage: python neugenfairmodel_merger.py <input1.yaml> <input2.yaml> ... <output.yaml>")
    sys.exit(1)

# All arguments except the last are input files
schemas = sys.argv[1:-1]
# Last argument is the output file
outyaml = sys.argv[-1]

# Start with an empty merged schema
merged_schema = SchemaDefinition(
    id="https://w3id.org/neugenfair/schema",
    name="neugenfairSchema",
    description="neugenfair schema data model for representing phenoclinical genomic data in the ICAN dataset"
)

for f in schemas:
    s = yaml_loader.load(f, target_class=SchemaDefinition)
    
    # Merge classes, slots, enums
    merged_schema.classes.update(s.classes)
    merged_schema.slots.update(s.slots)
    merged_schema.enums.update(s.enums)

    # Merge imports
    if s.imports:
        if not merged_schema.imports:
            merged_schema.imports = []
        for imp in s.imports:
            if imp not in merged_schema.imports:
                merged_schema.imports.append(imp)

    # Merge prefixes
    if s.prefixes:
        if not merged_schema.prefixes:
            merged_schema.prefixes = {}
        for k, v in s.prefixes.items():
            # If v is a Prefix object, take its .prefix_reference
            if isinstance(v, Prefix):
                merged_schema.prefixes[k] = v.prefix_reference
            else:
                merged_schema.prefixes[k] = v

    # Merge other metadata if needed
    if hasattr(s, "description") and s.description:
        if merged_schema.description:
            merged_schema.description += "\n" + s.description
        else:
            merged_schema.description = s.description

# Normalize prefixes so they dump cleanly
normalized_prefixes = {}
for k, v in merged_schema.prefixes._items():
    if isinstance(v, Prefix):
        normalized_prefixes[k] = v.prefix_reference
    else:
        normalized_prefixes[k] = v
merged_schema.prefixes = normalized_prefixes

# Save merged schema
yaml_dumper.dump(merged_schema, outyaml)
print(f"Merged schema written to {outyaml}")
