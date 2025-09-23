# neugenfairSchema

neugenfair schema data model for representing phenoclinical genomic data in the ICAN dataset
Schema for the neugenfair tool. Defines classes and attributes, supporting FAIR transformation of genomic and clinical data into Linked Data.

Schema for the AssemblySequence describing the chromosome or sequence that is the reference for the Region of the SequenceAlteration.

Schema for the Cohort class, describing the context in which the ICAN dataset was collected.

Schema for the (genomic) Position describing the start or the end of the Region where the SequenceAlteration is located.

Schema for the neugenfair tool. Defines classes and attributes, supporting FAIR transformation of genomic and clinical data into Linked Data.

Region class schema for the neugenfair tool. Defines Region where the SeqeunceAlteration occured as defined in FALDO ontology.

SequenceAlteration class schema for the neugenfair tool. Defines SequenceAlteration and the relations to other adjacent concepts.

VariantIdentifier class. The identifiers can following several nomenclatures or database convention naming (HGVSid, dbsnp, rsid). On SequenceAlteration can have several identifiers. One identifier can refer to several SequenceAlterations (complex alterations e.g. copy number variation).


URI: https://w3id.org/neugenfair/schema

Name: neugenfairSchema



## Classes

| Class | Description |
| --- | --- |
| [AlternateAllele](AlternateAllele.md) | Represents the AlternateAllele, found upon mapping (genome) read sequencing f... |
| [AssemblySequence](AssemblySequence.md) | AssemblySequence is a chromosome or sequence in a reference genome |
| [Cohort](Cohort.md) | Cohort role |
| [Position](Position.md) | (genomic) Position |
| [ReferenceAllele](ReferenceAllele.md) | Represents the ReferenceAllele, found on the reference sequence when performi... |
| [Region](Region.md) | (genomic) Region of a SequenceAlteration |
| [SequenceAlteration](SequenceAlteration.md) | A representation of a SequenceAlteration |
| [VariantIdentifier](VariantIdentifier.md) | A unique identifier for a sequence alteration within a database or nomenclatu... |



## Slots

| Slot | Description |
| --- | --- |
| [begins_at](begins_at.md) | The beginning of the location of the sequence alteration |
| [ends_at](ends_at.md) | The end of the location of the sequence alteration |
| [has_alternate_part](has_alternate_part.md) | Links the SequenceAlteration to its AlternateAllele |
| [has_identifier](has_identifier.md) | Relation between a SequenceAlteration and its VariantIdentifier |
| [has_reference](has_reference.md) | The reference sequence (contig, sequence, chromosome) |
| [has_reference_part](has_reference_part.md) | Links the SequenceAlteration to its ReferenceAllele |
| [has_source](has_source.md) | The nomenclature or database of the identifier (e |
| [has_value](has_value.md) | The value of the identifier |
| [is_described_by](is_described_by.md) | Is described by (e |
| [is_source_of](is_source_of.md) | Is source of (e |
| [label](label.md) | A human-readable relatable name for the sequence (e |
| [location](location.md) | Links the SequenceAlteration to its (genomic) Region |
| [position](position.md) | Exact (genomic) Position of a SequenceAlteration |
| [same_as](same_as.md) | Link to an external reference for the sequence (e |
| [value](value.md) | The nucleic composition of the reference allele |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [Nomenclature](Nomenclature.md) | The nomenclature or database system used for the identifier |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
