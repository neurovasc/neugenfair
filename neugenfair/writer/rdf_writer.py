# rdf_writer.py
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS
from urllib.parse import quote
import pandas as pd


def expand_uri_like(value, prefix_map):
    """
    Expand CURIE like 'sio:000300' into a full URIRef using prefix_map.
    """
    if isinstance(value, str) and ":" in value:
        prefix, local = value.split(":", 1)
        if prefix in prefix_map:
            return URIRef(prefix_map[prefix] + local)
    return URIRef(value)


def make_seqalt_iri(base_ns, chrom, pos, ref, alt):
    slug = f"{chrom}-{pos}-{ref}-{alt}"
    return URIRef(base_ns + "SequenceAlteration/" + quote(slug, safe=""))


def make_node(base_ns, kind, slug):
    return URIRef(base_ns + kind + "/" + quote(slug, safe=""))


def generate_graph_from_variants(df: pd.DataFrame, schema, prefix_map: dict,
                           base_ns: str = "https://w3id.org/neugenfair/instance/") -> Graph:
    """
    Generate RDF Graph from variants DataFrame according to the LinkML schema.

    Expected df columns: chrom, pos, ref, alt, id
    """
    g = Graph()

    # bind prefixes
    for pfx, ns in prefix_map.items():
        g.bind(pfx, ns)

    # resolve key class URIs
    seqalt_uri = expand_uri_like(schema.classes["SequenceAlteration"].class_uri, prefix_map)
    refallele_uri = expand_uri_like(schema.classes["ReferenceAllele"].class_uri, prefix_map)
    altallele_uri = expand_uri_like(schema.classes["AlternateAllele"].class_uri, prefix_map)
    pos_uri = expand_uri_like(schema.classes["Position"].class_uri, prefix_map)
    region_uri = expand_uri_like(schema.classes["Region"].class_uri, prefix_map)
    assembly_uri = expand_uri_like(schema.classes["AssemblySequence"].class_uri, prefix_map)
    varid_uri = expand_uri_like(schema.classes["VariantIdentifier"].class_uri, prefix_map)

    # resolve slot URIs
    has_identifier = expand_uri_like(schema.slots["has_identifier"].slot_uri, prefix_map)
    has_reference_part = expand_uri_like(schema.slots["has_reference_part"].slot_uri, prefix_map)
    has_alternate_part = expand_uri_like(schema.slots["has_alternate_part"].slot_uri, prefix_map)
    location = expand_uri_like(schema.slots["location"].slot_uri, prefix_map)
    begins_at = expand_uri_like(schema.slots["begins_at"].slot_uri, prefix_map)
    ends_at = expand_uri_like(schema.slots["ends_at"].slot_uri, prefix_map)
    has_reference = expand_uri_like(schema.slots["has_reference"].slot_uri, prefix_map)
    position_prop = expand_uri_like(schema.slots["position"].slot_uri, prefix_map)
    value_prop = expand_uri_like(schema.slots["value"].slot_uri, prefix_map)
    has_value = expand_uri_like(schema.slots["has_value"].slot_uri, prefix_map)
    has_source = expand_uri_like(schema.slots["has_source"].slot_uri, prefix_map)

    for _, v in df.iterrows():
        # SequenceAlteration
        sa = make_seqalt_iri(base_ns, v["chrom"], v["pos"], v["ref"], v["alt"])
        g.add((sa, RDF.type, seqalt_uri))
        g.add((sa, RDFS.label, Literal(f"{v['chrom']}:{v['pos']} {v['ref']}>{v['alt']}")))

        # Identifier (if any)
        if v.get("id") and v["id"] != ".":
            ident = make_node(base_ns, "variantid", v["id"])
            g.add((ident, RDF.type, varid_uri))
            g.add((ident, has_value, Literal(v["id"])))
            # For now, assume dbSNP (you could parametrize this)
            g.add((ident, has_source, Literal("dbSNP")))
            g.add((sa, has_identifier, ident))

        # ReferenceAllele
        ref_node = make_node(base_ns, "ReferenceAllele", f"{v['chrom']}-{v['pos']}-{v['ref']}")
        g.add((ref_node, RDF.type, refallele_uri))
        g.add((ref_node, value_prop, Literal(v["ref"])))
        g.add((sa, has_reference_part, ref_node))

        # AlternateAllele
        alt_node = make_node(base_ns, "AlternateAllele", f"{v['chrom']}-{v['pos']}-{v['alt']}")
        g.add((alt_node, RDF.type, altallele_uri))
        g.add((alt_node, value_prop, Literal(v["alt"])))
        g.add((sa, has_alternate_part, alt_node))

        # Position
        pos_node = make_node(base_ns, "Position", f"{v['chrom']}-{v['pos']}")
        g.add((pos_node, RDF.type, pos_uri))
        g.add((pos_node, position_prop, Literal(int(v["pos"]))))
        # Region
        reg_node = make_node(base_ns, "Region", f"{v['chrom']}-{v['pos']}")
        g.add((reg_node, RDF.type, region_uri))
        g.add((reg_node, begins_at, pos_node))
        g.add((reg_node, ends_at, pos_node))
        # AssemblySequence
        asm_node = make_node(base_ns, "assembly", v["chrom"])
        g.add((asm_node, RDF.type, assembly_uri))
        g.add((asm_node, RDFS.label, Literal(v["chrom"])))
        g.add((asm_node, has_value, Literal(v["chrom"])))
        g.add((reg_node, has_reference, asm_node))
        g.add((sa, location, reg_node))

    return g