from linkml_runtime.loaders import yaml_loader
from linkml_runtime.linkml_model.meta import SchemaDefinition
from linkml_runtime.dumpers import yaml_dumper

schemas = ["schemas/models/model_Individual.yaml", "schemas/models/model_Variant.yaml"]

# Start with an empty merged schema
merged_schema = SchemaDefinition(
    id="https://w3id.org/neugenfair/schema",
    name="NeugenFAIRSchema",
    description="Merged NeugenFAIR schema"
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
            merged_schema.prefixes[k] = v

    # Merge other metadata if needed
    if hasattr(s, "description") and s.description:
        if merged_schema.description:
            merged_schema.description += "\n" + s.description
        else:
            merged_schema.description = s.description

# Save merged schema
yaml_dumper.dump(merged_schema, "schemas/neugenfairmodel.yaml")
print("Merged schema written to schemas/neugenfairmodel.yaml")
