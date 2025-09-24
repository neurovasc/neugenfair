import argparse
from neugenfair.mappers.model_mapper import load_schema, build_prefix_map
from neugenfair.parsers.vcf_parser import read_vcf_minimal, vcf_to_variants
from neugenfair.writer.rdf_writer import generate_graph_from_variants
import rdflib

def main():
    p = argparse.ArgumentParser()
    p.add_argument('vcf', help='Input VCF file')
    p.add_argument('--schema', default='schemas/neugenfairmodel.yaml', help='LinkML schema YAML')
    p.add_argument('--out', default='out.ttl', help='Output RDF (ttl) file')
    p.add_argument('--jsonld', help='Also write JSON-LD to this path')
    args = p.parse_args()

    schema = load_schema(args.schema)
    prefixes = build_prefix_map(schema)


    df = read_vcf_minimal(args.vcf)
    variants = vcf_to_variants(df)
    print(type(df))
    print(type(variants))

    g = generate_graph_from_variants(variants, schema, prefixes, base_ns="https://w3id.org/neugenfair/instance/")

    # write turtle
    g.serialize(destination=args.out, format='turtle')
    print("Wrote", args.out)
    if args.jsonld:
        g.serialize(destination=args.jsonld, format='json-ld')
        print("Wrote", args.jsonld)

if __name__ == '__main__':
    main()