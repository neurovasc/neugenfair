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