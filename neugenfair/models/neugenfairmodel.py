# Auto generated from neugenfairmodel.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-09-23T13:15:10
# Schema: neugenfairSchema
#
# id: https://w3id.org/neugenfair/schema
# description: neugenfair schema data model for representing phenoclinical genomic data in the ICAN dataset
#   Schema for the neugenfair tool. Defines classes and attributes, supporting FAIR transformation of genomic and clinical data into Linked Data.
#
#   Schema for the AssemblySequence describing the chromosome or sequence that is the reference for the Region of the SequenceAlteration.
#
#   Schema for the (genomic) Position describing the start or the end of the Region where the SequenceAlteration is located.
#
#   Schema for the neugenfair tool. Defines classes and attributes, supporting FAIR transformation of genomic and clinical data into Linked Data.
#
#   Region class schema for the neugenfair tool. Defines Region where the SeqeunceAlteration occured as defined in FALDO ontology.
#
#   SequenceAlteration class schema for the neugenfair tool. Defines SequenceAlteration and the relations to other adjacent concepts.
#
#   VariantIdentifier class. The identifiers can following several nomenclatures or database convention naming (HGVSid, dbsnp, rsid). On SequenceAlteration can have several identifiers. One identifier can refer to several SequenceAlterations (complex alterations e.g. copy number variation).
#
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Namespaces
AIC = CurieNamespace('aic', 'https://example.org/aiccohortvariants#')
EX = CurieNamespace('ex', 'http://example.org/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
GENO = CurieNamespace('geno', 'http://purl.obolibrary.org/obo/GENO_')
GO = CurieNamespace('go', 'http://example.org/UNKNOWN/go/')
HPO = CurieNamespace('hpo', 'http://purl.obolibrary.org/obo/HP_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MONDO = CurieNamespace('mondo', 'http://purl.obolibrary.org/obo/MONDO_')
NCIT = CurieNamespace('ncit', 'http://purl.obolibrary.org/obo/NCIT_')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SIO = CurieNamespace('sio', 'http://semanticscience.org/resource/SIO_')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SO = CurieNamespace('so', 'http://purl.obolibrary.org/obo/SO_')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/neugenfair/schema/')


# Types

# Class references



@dataclass(repr=False)
class AlternateAllele(YAMLRoot):
    """
    Represents the alternate allele (geno:0000002).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENO["0000002"]
    class_class_curie: ClassVar[str] = "geno:0000002"
    class_name: ClassVar[str] = "AlternateAllele"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/AlternateAllele")

    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssemblySequence(YAMLRoot):
    """
    AssemblySequence is a chromosome or sequence in a reference genome.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SO["0000353"]
    class_class_curie: ClassVar[str] = "so:0000353"
    class_name: ClassVar[str] = "AssemblySequence"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/AssemblySequence")

    has_value: Optional[str] = None
    label: Optional[str] = None
    same_as: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.has_value is not None and not isinstance(self.has_value, str):
            self.has_value = str(self.has_value)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.same_as is not None and not isinstance(self.same_as, str):
            self.same_as = str(self.same_as)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Position(YAMLRoot):
    """
    (genomic) Position.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FALDO["ExactPosition"]
    class_class_curie: ClassVar[str] = "faldo:ExactPosition"
    class_name: ClassVar[str] = "Position"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/Position")

    position: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.position is not None and not isinstance(self.position, str):
            self.position = str(self.position)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReferenceAllele(YAMLRoot):
    """
    Represents the reference allele (geno:0000036).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENO["0000036"]
    class_class_curie: ClassVar[str] = "geno:0000036"
    class_name: ClassVar[str] = "ReferenceAllele"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/ReferenceAllele")

    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Region(YAMLRoot):
    """
    (genomic) Region of a SequenceAlteration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FALDO["Region"]
    class_class_curie: ClassVar[str] = "faldo:Region"
    class_name: ClassVar[str] = "Region"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/Region")

    begins_at: Optional[str] = None
    ends_at: Optional[str] = None
    has_reference: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.begins_at is not None and not isinstance(self.begins_at, str):
            self.begins_at = str(self.begins_at)

        if self.ends_at is not None and not isinstance(self.ends_at, str):
            self.ends_at = str(self.ends_at)

        if self.has_reference is not None and not isinstance(self.has_reference, str):
            self.has_reference = str(self.has_reference)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SequenceAlteration(YAMLRoot):
    """
    A representation of a SequenceAlteration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SO["0001059"]
    class_class_curie: ClassVar[str] = "so:0001059"
    class_name: ClassVar[str] = "SequenceAlteration"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/SequenceAlteration")

    has_identifier: Optional[str] = None
    has_reference_part: Optional[str] = None
    has_alternate_part: Optional[str] = None
    location: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.has_identifier is not None and not isinstance(self.has_identifier, str):
            self.has_identifier = str(self.has_identifier)

        if self.has_reference_part is not None and not isinstance(self.has_reference_part, str):
            self.has_reference_part = str(self.has_reference_part)

        if self.has_alternate_part is not None and not isinstance(self.has_alternate_part, str):
            self.has_alternate_part = str(self.has_alternate_part)

        if self.location is not None and not isinstance(self.location, str):
            self.location = str(self.location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VariantIdentifier(YAMLRoot):
    """
    A unique identifier for a sequence alteration within a database or nomenclature.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["000675"]
    class_class_curie: ClassVar[str] = "sio:000675"
    class_name: ClassVar[str] = "VariantIdentifier"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/VariantIdentifier")

    has_value: Optional[str] = None
    has_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.has_value is not None and not isinstance(self.has_value, str):
            self.has_value = str(self.has_value)

        if self.has_source is not None and not isinstance(self.has_source, str):
            self.has_source = str(self.has_source)

        super().__post_init__(**kwargs)


# Enumerations
class Nomenclature(EnumDefinitionImpl):
    """
    The nomenclature or database system used for the identifier.
    """
    HGVS = PermissibleValue(
        text="HGVS",
        description="Human Genome Variation Society nomenclature.")
    dbSNP = PermissibleValue(
        text="dbSNP",
        description="Database of Single Nucleotide Polymorphisms.")
    rsID = PermissibleValue(
        text="rsID",
        description="Reference SNP cluster ID from dbSNP.")
    ClinVar = PermissibleValue(
        text="ClinVar",
        description="Clinical significance database for variants.")
    COSMIC = PermissibleValue(
        text="COSMIC",
        description="Catalogue Of Somatic Mutations In Cancer.")
    Ensembl = PermissibleValue(
        text="Ensembl",
        description="Ensembl database identifier.")
    HUGO = PermissibleValue(
        text="HUGO",
        description="""Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC)-approved gene nomenclature.""")
    Other = PermissibleValue(
        text="Other",
        description="Other nomenclature or database not listed.")

    _defn = EnumDefinition(
        name="Nomenclature",
        description="The nomenclature or database system used for the identifier.",
    )

# Slots
class slots:
    pass

slots.has_value = Slot(uri=SIO['000300'], name="has_value", curie=SIO.curie('000300'),
                   model_uri=DEFAULT_.has_value, domain=VariantIdentifier, range=str)

slots.label = Slot(uri=RDFS.label, name="label", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.label, domain=AssemblySequence, range=Optional[str])

slots.same_as = Slot(uri=OWL.sameAs, name="same_as", curie=OWL.curie('sameAs'),
                   model_uri=DEFAULT_.same_as, domain=AssemblySequence, range=Optional[str])

slots.relation_one = Slot(uri=FALDO.position, name="relation_one", curie=FALDO.curie('position'),
                   model_uri=DEFAULT_.relation_one, domain=Position, range=int)

slots.begins_at = Slot(uri=FALDO.begin, name="begins_at", curie=FALDO.curie('begin'),
                   model_uri=DEFAULT_.begins_at, domain=Region, range=Union[dict, Position])

slots.ends_at = Slot(uri=FALDO.end, name="ends_at", curie=FALDO.curie('end'),
                   model_uri=DEFAULT_.ends_at, domain=Region, range=Union[dict, Position])

slots.has_reference = Slot(uri=FALDO.reference, name="has_reference", curie=FALDO.curie('reference'),
                   model_uri=DEFAULT_.has_reference, domain=Region, range=Union[dict, AssemblySequence])

slots.has_identifier = Slot(uri=SIO['0000671'], name="has_identifier", curie=SIO.curie('0000671'),
                   model_uri=DEFAULT_.has_identifier, domain=SequenceAlteration, range=Union[dict, "VariantIdentifier"])

slots.has_reference_part = Slot(uri=GENO['0000385'], name="has_reference_part", curie=GENO.curie('0000385'),
                   model_uri=DEFAULT_.has_reference_part, domain=SequenceAlteration, range=Optional[Union[dict, ReferenceAllele]])

slots.has_alternate_part = Slot(uri=GENO['0000382'], name="has_alternate_part", curie=GENO.curie('0000382'),
                   model_uri=DEFAULT_.has_alternate_part, domain=SequenceAlteration, range=Optional[Union[dict, AlternateAllele]])

slots.location = Slot(uri=FALDO.location, name="location", curie=FALDO.curie('location'),
                   model_uri=DEFAULT_.location, domain=SequenceAlteration, range=Optional[Union[dict, Region]])

slots.has_source = Slot(uri=SIO['000253'], name="has_source", curie=SIO.curie('000253'),
                   model_uri=DEFAULT_.has_source, domain=VariantIdentifier, range=Union[str, "Nomenclature"])

slots.alternateAllele__value = Slot(uri=SIO['000300'], name="alternateAllele__value", curie=SIO.curie('000300'),
                   model_uri=DEFAULT_.alternateAllele__value, domain=None, range=str)

slots.assemblySequence__has_value = Slot(uri=DEFAULT_.has_value, name="assemblySequence__has_value", curie=DEFAULT_.curie('has_value'),
                   model_uri=DEFAULT_.assemblySequence__has_value, domain=None, range=Optional[str])

slots.assemblySequence__label = Slot(uri=DEFAULT_.label, name="assemblySequence__label", curie=DEFAULT_.curie('label'),
                   model_uri=DEFAULT_.assemblySequence__label, domain=None, range=Optional[str])

slots.assemblySequence__same_as = Slot(uri=DEFAULT_.same_as, name="assemblySequence__same_as", curie=DEFAULT_.curie('same_as'),
                   model_uri=DEFAULT_.assemblySequence__same_as, domain=None, range=Optional[str])

slots.position__position = Slot(uri=DEFAULT_.position, name="position__position", curie=DEFAULT_.curie('position'),
                   model_uri=DEFAULT_.position__position, domain=None, range=Optional[str])

slots.referenceAllele__value = Slot(uri=SIO['000300'], name="referenceAllele__value", curie=SIO.curie('000300'),
                   model_uri=DEFAULT_.referenceAllele__value, domain=None, range=str)

slots.region__begins_at = Slot(uri=DEFAULT_.begins_at, name="region__begins_at", curie=DEFAULT_.curie('begins_at'),
                   model_uri=DEFAULT_.region__begins_at, domain=None, range=Optional[str])

slots.region__ends_at = Slot(uri=DEFAULT_.ends_at, name="region__ends_at", curie=DEFAULT_.curie('ends_at'),
                   model_uri=DEFAULT_.region__ends_at, domain=None, range=Optional[str])

slots.region__has_reference = Slot(uri=DEFAULT_.has_reference, name="region__has_reference", curie=DEFAULT_.curie('has_reference'),
                   model_uri=DEFAULT_.region__has_reference, domain=None, range=Optional[str])

slots.sequenceAlteration__has_identifier = Slot(uri=DEFAULT_.has_identifier, name="sequenceAlteration__has_identifier", curie=DEFAULT_.curie('has_identifier'),
                   model_uri=DEFAULT_.sequenceAlteration__has_identifier, domain=None, range=Optional[str])

slots.sequenceAlteration__has_reference_part = Slot(uri=DEFAULT_.has_reference_part, name="sequenceAlteration__has_reference_part", curie=DEFAULT_.curie('has_reference_part'),
                   model_uri=DEFAULT_.sequenceAlteration__has_reference_part, domain=None, range=Optional[str])

slots.sequenceAlteration__has_alternate_part = Slot(uri=DEFAULT_.has_alternate_part, name="sequenceAlteration__has_alternate_part", curie=DEFAULT_.curie('has_alternate_part'),
                   model_uri=DEFAULT_.sequenceAlteration__has_alternate_part, domain=None, range=Optional[str])

slots.sequenceAlteration__location = Slot(uri=DEFAULT_.location, name="sequenceAlteration__location", curie=DEFAULT_.curie('location'),
                   model_uri=DEFAULT_.sequenceAlteration__location, domain=None, range=Optional[str])

slots.variantIdentifier__has_value = Slot(uri=DEFAULT_.has_value, name="variantIdentifier__has_value", curie=DEFAULT_.curie('has_value'),
                   model_uri=DEFAULT_.variantIdentifier__has_value, domain=None, range=Optional[str])

slots.variantIdentifier__has_source = Slot(uri=DEFAULT_.has_source, name="variantIdentifier__has_source", curie=DEFAULT_.curie('has_source'),
                   model_uri=DEFAULT_.variantIdentifier__has_source, domain=None, range=Optional[str])

