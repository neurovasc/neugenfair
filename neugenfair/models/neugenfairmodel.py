# Auto generated from neugenfairmodel.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-09-24T10:51:48
# Schema: neugenfairSchema
#
# id: https://w3id.org/neugenfair/schema
# description: neugenfair schema data model for representing phenoclinical genomic data in the ICAN dataset
#   Schema for the neugenfair tool. Defines classes and attributes, supporting FAIR transformation of genomic and clinical data into Linked Data.
#
#   Schema for the AssemblySequence describing the chromosome or sequence that is the reference for the Region of the SequenceAlteration.
#
#   Schema for the Cohort class, describing the context in which the ICAN dataset was collected.
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
GO = CurieNamespace('go', 'http://semanticscience.org/resource/SIO_')
HPO = CurieNamespace('hpo', 'http://purl.obolibrary.org/obo/HP_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MONDO = CurieNamespace('mondo', 'http://purl.obolibrary.org/obo/MONDO_')
NCIT = CurieNamespace('ncit', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('obi', 'http://purl.obolibrary.org/obo/OBI_')
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
    Represents the AlternateAllele, found upon mapping (genome) read sequencing from a sample to the reference
    sequence.
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

    has_value: str = None
    label: Optional[str] = None
    same_as: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.has_value):
            self.MissingRequiredField("has_value")
        if not isinstance(self.has_value, str):
            self.has_value = str(self.has_value)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.same_as is not None and not isinstance(self.same_as, str):
            self.same_as = str(self.same_as)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Cohort(YAMLRoot):
    """
    Cohort role.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000252"]
    class_class_curie: ClassVar[str] = "obi:0000252"
    class_name: ClassVar[str] = "Cohort"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/Cohort")

    has_identifier: str = None
    is_described_by: Optional[str] = None
    is_source_of: Optional[Union[dict, "SequenceAlteration"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.has_identifier):
            self.MissingRequiredField("has_identifier")
        if not isinstance(self.has_identifier, str):
            self.has_identifier = str(self.has_identifier)

        if self.is_described_by is not None and not isinstance(self.is_described_by, str):
            self.is_described_by = str(self.is_described_by)

        if self.is_source_of is not None and not isinstance(self.is_source_of, SequenceAlteration):
            self.is_source_of = SequenceAlteration(**as_dict(self.is_source_of))

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

    position: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.position):
            self.MissingRequiredField("position")
        if not isinstance(self.position, int):
            self.position = int(self.position)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReferenceAllele(YAMLRoot):
    """
    Represents the ReferenceAllele, found on the reference sequence when performing variant calling.
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

    begins_at: Union[dict, Position] = None
    ends_at: Union[dict, Position] = None
    has_reference: Union[dict, AssemblySequence] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.begins_at):
            self.MissingRequiredField("begins_at")
        if not isinstance(self.begins_at, Position):
            self.begins_at = Position(**as_dict(self.begins_at))

        if self._is_empty(self.ends_at):
            self.MissingRequiredField("ends_at")
        if not isinstance(self.ends_at, Position):
            self.ends_at = Position(**as_dict(self.ends_at))

        if self._is_empty(self.has_reference):
            self.MissingRequiredField("has_reference")
        if not isinstance(self.has_reference, AssemblySequence):
            self.has_reference = AssemblySequence(**as_dict(self.has_reference))

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

    has_identifier: Union[dict, "VariantIdentifier"] = None
    has_alternate_part: Union[dict, AlternateAllele] = None
    location: Union[dict, Region] = None
    has_reference_part: Optional[Union[dict, ReferenceAllele]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.has_identifier):
            self.MissingRequiredField("has_identifier")
        if not isinstance(self.has_identifier, VariantIdentifier):
            self.has_identifier = VariantIdentifier(**as_dict(self.has_identifier))

        if self._is_empty(self.has_alternate_part):
            self.MissingRequiredField("has_alternate_part")
        if not isinstance(self.has_alternate_part, AlternateAllele):
            self.has_alternate_part = AlternateAllele(**as_dict(self.has_alternate_part))

        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, Region):
            self.location = Region(**as_dict(self.location))

        if self.has_reference_part is not None and not isinstance(self.has_reference_part, ReferenceAllele):
            self.has_reference_part = ReferenceAllele(**as_dict(self.has_reference_part))

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

    has_value: str = None
    has_source: Union[str, "Nomenclature"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.has_value):
            self.MissingRequiredField("has_value")
        if not isinstance(self.has_value, str):
            self.has_value = str(self.has_value)

        if self._is_empty(self.has_source):
            self.MissingRequiredField("has_source")
        if not isinstance(self.has_source, Nomenclature):
            self.has_source = Nomenclature(self.has_source)

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

slots.value = Slot(uri=SIO['000300'], name="value", curie=SIO.curie('000300'),
                   model_uri=DEFAULT_.value, domain=None, range=str)

slots.has_value = Slot(uri=SIO['000300'], name="has_value", curie=SIO.curie('000300'),
                   model_uri=DEFAULT_.has_value, domain=VariantIdentifier, range=str)

slots.label = Slot(uri=RDFS.label, name="label", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.label, domain=AssemblySequence, range=Optional[str])

slots.same_as = Slot(uri=OWL.sameAs, name="same_as", curie=OWL.curie('sameAs'),
                   model_uri=DEFAULT_.same_as, domain=AssemblySequence, range=Optional[str])

slots.is_described_by = Slot(uri=SIO['000557'], name="is_described_by", curie=SIO.curie('000557'),
                   model_uri=DEFAULT_.is_described_by, domain=Cohort, range=Optional[str])

slots.is_source_of = Slot(uri=SIO['000219'], name="is_source_of", curie=SIO.curie('000219'),
                   model_uri=DEFAULT_.is_source_of, domain=Cohort, range=Optional[Union[dict, "SequenceAlteration"]])

slots.has_identifier = Slot(uri=SIO['0000671'], name="has_identifier", curie=SIO.curie('0000671'),
                   model_uri=DEFAULT_.has_identifier, domain=SequenceAlteration, range=Union[dict, "VariantIdentifier"])

slots.position = Slot(uri=FALDO.position, name="position", curie=FALDO.curie('position'),
                   model_uri=DEFAULT_.position, domain=Position, range=int)

slots.begins_at = Slot(uri=FALDO.begin, name="begins_at", curie=FALDO.curie('begin'),
                   model_uri=DEFAULT_.begins_at, domain=Region, range=Union[dict, Position])

slots.ends_at = Slot(uri=FALDO.end, name="ends_at", curie=FALDO.curie('end'),
                   model_uri=DEFAULT_.ends_at, domain=Region, range=Union[dict, Position])

slots.has_reference = Slot(uri=FALDO.reference, name="has_reference", curie=FALDO.curie('reference'),
                   model_uri=DEFAULT_.has_reference, domain=Region, range=Union[dict, AssemblySequence])

slots.has_reference_part = Slot(uri=GENO['0000385'], name="has_reference_part", curie=GENO.curie('0000385'),
                   model_uri=DEFAULT_.has_reference_part, domain=SequenceAlteration, range=Optional[Union[dict, ReferenceAllele]])

slots.has_alternate_part = Slot(uri=GENO['0000382'], name="has_alternate_part", curie=GENO.curie('0000382'),
                   model_uri=DEFAULT_.has_alternate_part, domain=SequenceAlteration, range=Optional[Union[dict, AlternateAllele]])

slots.location = Slot(uri=FALDO.location, name="location", curie=FALDO.curie('location'),
                   model_uri=DEFAULT_.location, domain=SequenceAlteration, range=Optional[Union[dict, Region]])

slots.has_source = Slot(uri=SIO['000253'], name="has_source", curie=SIO.curie('000253'),
                   model_uri=DEFAULT_.has_source, domain=VariantIdentifier, range=Union[str, "Nomenclature"])

slots.alternateAllele__value = Slot(uri=SIO['000300'], name="alternateAllele__value", curie=SIO.curie('000300'),
                   model_uri=DEFAULT_.alternateAllele__value, domain=AlternateAllele, range=str)

slots.assemblySequence__has_value = Slot(uri=SIO['000300'], name="assemblySequence__has_value", curie=SIO.curie('000300'),
                   model_uri=DEFAULT_.assemblySequence__has_value, domain=AssemblySequence, range=str)

slots.assemblySequence__label = Slot(uri=RDFS.label, name="assemblySequence__label", curie=RDFS.curie('label'),
                   model_uri=DEFAULT_.assemblySequence__label, domain=AssemblySequence, range=Optional[str])

slots.assemblySequence__same_as = Slot(uri=OWL.sameAs, name="assemblySequence__same_as", curie=OWL.curie('sameAs'),
                   model_uri=DEFAULT_.assemblySequence__same_as, domain=AssemblySequence, range=Optional[str])

slots.cohort__is_described_by = Slot(uri=SIO['000557'], name="cohort__is_described_by", curie=SIO.curie('000557'),
                   model_uri=DEFAULT_.cohort__is_described_by, domain=Cohort, range=Optional[str])

slots.cohort__is_source_of = Slot(uri=SIO['000219'], name="cohort__is_source_of", curie=SIO.curie('000219'),
                   model_uri=DEFAULT_.cohort__is_source_of, domain=Cohort, range=Optional[Union[dict, "SequenceAlteration"]])

slots.cohort__has_identifier = Slot(uri=SIO['0000671'], name="cohort__has_identifier", curie=SIO.curie('0000671'),
                   model_uri=DEFAULT_.cohort__has_identifier, domain=Cohort, range=str)

slots.position__position = Slot(uri=FALDO.position, name="position__position", curie=FALDO.curie('position'),
                   model_uri=DEFAULT_.position__position, domain=Position, range=int)

slots.referenceAllele__value = Slot(uri=SIO['000300'], name="referenceAllele__value", curie=SIO.curie('000300'),
                   model_uri=DEFAULT_.referenceAllele__value, domain=ReferenceAllele, range=str)

slots.region__begins_at = Slot(uri=FALDO.begin, name="region__begins_at", curie=FALDO.curie('begin'),
                   model_uri=DEFAULT_.region__begins_at, domain=Region, range=Union[dict, Position])

slots.region__ends_at = Slot(uri=FALDO.end, name="region__ends_at", curie=FALDO.curie('end'),
                   model_uri=DEFAULT_.region__ends_at, domain=Region, range=Union[dict, Position])

slots.region__has_reference = Slot(uri=FALDO.reference, name="region__has_reference", curie=FALDO.curie('reference'),
                   model_uri=DEFAULT_.region__has_reference, domain=Region, range=Union[dict, AssemblySequence])

slots.sequenceAlteration__has_identifier = Slot(uri=SIO['0000671'], name="sequenceAlteration__has_identifier", curie=SIO.curie('0000671'),
                   model_uri=DEFAULT_.sequenceAlteration__has_identifier, domain=SequenceAlteration, range=Union[dict, "VariantIdentifier"])

slots.sequenceAlteration__has_reference_part = Slot(uri=GENO['0000385'], name="sequenceAlteration__has_reference_part", curie=GENO.curie('0000385'),
                   model_uri=DEFAULT_.sequenceAlteration__has_reference_part, domain=SequenceAlteration, range=Optional[Union[dict, ReferenceAllele]])

slots.sequenceAlteration__has_alternate_part = Slot(uri=GENO['0000382'], name="sequenceAlteration__has_alternate_part", curie=GENO.curie('0000382'),
                   model_uri=DEFAULT_.sequenceAlteration__has_alternate_part, domain=SequenceAlteration, range=Union[dict, AlternateAllele])

slots.sequenceAlteration__location = Slot(uri=FALDO.location, name="sequenceAlteration__location", curie=FALDO.curie('location'),
                   model_uri=DEFAULT_.sequenceAlteration__location, domain=SequenceAlteration, range=Union[dict, Region])

slots.variantIdentifier__has_value = Slot(uri=SIO['000300'], name="variantIdentifier__has_value", curie=SIO.curie('000300'),
                   model_uri=DEFAULT_.variantIdentifier__has_value, domain=VariantIdentifier, range=str)

slots.variantIdentifier__has_source = Slot(uri=SIO['000253'], name="variantIdentifier__has_source", curie=SIO.curie('000253'),
                   model_uri=DEFAULT_.variantIdentifier__has_source, domain=VariantIdentifier, range=Union[str, "Nomenclature"])

