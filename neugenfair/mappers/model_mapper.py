from linkml_runtime.loaders import yaml_loader
from linkml_runtime.linkml_model.meta import SchemaDefinition, Prefix
from rdflib import Namespace, URIRef

def load_schema(schema_path: str) -> SchemaDefinition:
    """Load a LinkML schema (SchemaDefinition) from YAML."""
    schema = yaml_loader.load(schema_path, target_class=SchemaDefinition)
    return schema

def build_prefix_map(schema: SchemaDefinition) -> dict:
    """Return mapping prefix->namespace URI (plain strings)."""
    pmap = {}
    if getattr(schema, "prefixes", None):
        for k, v in schema.prefixes.items():
            # v could be a string, or a jsonasobj2 JsonObj; cast to str
            pmap[k] = str(v)
    normalized_prefixes = normalize_prefixes(schema)
    return normalized_prefixes

def expand_curie(curie: str, prefix_map: dict) -> URIRef:
    """
    Expand a CURIE like 'sio:0000671' to a full URIRef using prefix_map.
    If curie already looks like a URI, return URIRef(curie).
    """
    if ':' in curie:
        prefix, local = curie.split(':', 1)
        ns = prefix_map.get(prefix)
        if ns:
            return URIRef(ns + local)
    # fallback: treat as URIRef
    return URIRef(curie)

def normalize_prefixes(schema):
    """
    Convert Prefix objects (or JsonObj-wrapped Prefix) into plain dict entries.
    Ensures RDF/JSON-LD exporters see valid prefix → IRI mappings.
    """
    normalized = {}
    if not schema.prefixes:
        return normalized

    for k, v in dict(schema.prefixes).items():
        if isinstance(v, Prefix):
            normalized[k] = v.prefix_reference
        elif hasattr(v, "prefix_reference"):  # JsonObj(Prefix)
            normalized[k] = v.prefix_reference
        else:
            normalized[k] = str(v)
    return normalized