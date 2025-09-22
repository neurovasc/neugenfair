# Auto generated from neugenfairmodel.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-09-22T15:46:36
# Schema: NeugenFAIRSchema
#
# id: https://w3id.org/neugenfair/schema
# description: Merged NeugenFAIR schema
#   Schema for the neugenfair tool. Defines classes and attributes, supporting FAIR transformation of genomic and clinical data into Linked Data.
#
#   Schema for the Variant Identifier following several nomenclatures or database convention naming.
#
#   Schema for the neugenfair tool. Defines classes and attributes, supporting FAIR transformation of genomic and clinical data into Linked Data.
#
#   Schema for the neugenfair tool. Defines classes and attributes, supporting FAIR transformation of genomic and clinical data into Linked Data.
#
#   Schema for the neugenfair tool. Defines classes and attributes, supporting FAIR transformation of genomic and clinical data into Linked Data.
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
class SequenceAlteration(YAMLRoot):
    """
    A representation of a sequence alteration (so:0001059).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SO["0001059"]
    class_class_curie: ClassVar[str] = "so:0001059"
    class_name: ClassVar[str] = "SequenceAlteration"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/SequenceAlteration")

    has_identifier: Union[dict, "VariantIdentifier"] = None
    has_reference_allele: Optional[Union[dict, "ReferenceAllele"]] = None
    has_alternate_allele: Optional[Union[dict, "AlternateAllele"]] = None
    has_location: Optional[Union[dict, "VariationSite"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.has_identifier):
            self.MissingRequiredField("has_identifier")
        if not isinstance(self.has_identifier, VariantIdentifier):
            self.has_identifier = VariantIdentifier(**as_dict(self.has_identifier))

        if self.has_reference_allele is not None and not isinstance(self.has_reference_allele, ReferenceAllele):
            self.has_reference_allele = ReferenceAllele(**as_dict(self.has_reference_allele))

        if self.has_alternate_allele is not None and not isinstance(self.has_alternate_allele, AlternateAllele):
            self.has_alternate_allele = AlternateAllele(**as_dict(self.has_alternate_allele))

        if self.has_location is not None and not isinstance(self.has_location, VariationSite):
            self.has_location = VariationSite(**as_dict(self.has_location))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VariantIdentifier(YAMLRoot):
    """
    A unique identifier for a sequence alteration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["000675"]
    class_class_curie: ClassVar[str] = "sio:000675"
    class_name: ClassVar[str] = "VariantIdentifier"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/VariantIdentifier")

    hgvsid: str = None
    rsid: Optional[str] = None
    other: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.hgvsid):
            self.MissingRequiredField("hgvsid")
        if not isinstance(self.hgvsid, str):
            self.hgvsid = str(self.hgvsid)

        if self.rsid is not None and not isinstance(self.rsid, str):
            self.rsid = str(self.rsid)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VariationSite(YAMLRoot):
    """
    Represents the location of a sequence alteration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FALDO["Region"]
    class_class_curie: ClassVar[str] = "faldo:Region"
    class_name: ClassVar[str] = "VariationSite"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/VariationSite")

    begins_at: int = None
    ends_at: int = None
    has_reference: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.begins_at):
            self.MissingRequiredField("begins_at")
        if not isinstance(self.begins_at, int):
            self.begins_at = int(self.begins_at)

        if self._is_empty(self.ends_at):
            self.MissingRequiredField("ends_at")
        if not isinstance(self.ends_at, int):
            self.ends_at = int(self.ends_at)

        if self._is_empty(self.has_reference):
            self.MissingRequiredField("has_reference")
        if not isinstance(self.has_reference, int):
            self.has_reference = int(self.has_reference)

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


# Enumerations


# Slots
class slots:
    pass

slots.sequenceAlteration__has_identifier = Slot(uri=SIO['000674'], name="sequenceAlteration__has_identifier", curie=SIO.curie('000674'),
                   model_uri=DEFAULT_.sequenceAlteration__has_identifier, domain=None, range=Union[dict, VariantIdentifier])

slots.sequenceAlteration__has_reference_allele = Slot(uri=GENO['0000385'], name="sequenceAlteration__has_reference_allele", curie=GENO.curie('0000385'),
                   model_uri=DEFAULT_.sequenceAlteration__has_reference_allele, domain=None, range=Optional[Union[dict, ReferenceAllele]])

slots.sequenceAlteration__has_alternate_allele = Slot(uri=GENO['0000382'], name="sequenceAlteration__has_alternate_allele", curie=GENO.curie('0000382'),
                   model_uri=DEFAULT_.sequenceAlteration__has_alternate_allele, domain=None, range=Optional[Union[dict, AlternateAllele]])

slots.sequenceAlteration__has_location = Slot(uri=FALDO.location, name="sequenceAlteration__has_location", curie=FALDO.curie('location'),
                   model_uri=DEFAULT_.sequenceAlteration__has_location, domain=None, range=Optional[Union[dict, VariationSite]])

slots.variantIdentifier__hgvsid = Slot(uri=SIO['000300'], name="variantIdentifier__hgvsid", curie=SIO.curie('000300'),
                   model_uri=DEFAULT_.variantIdentifier__hgvsid, domain=None, range=str)

slots.variantIdentifier__rsid = Slot(uri=SIO['000300'], name="variantIdentifier__rsid", curie=SIO.curie('000300'),
                   model_uri=DEFAULT_.variantIdentifier__rsid, domain=None, range=Optional[str])

slots.variantIdentifier__other = Slot(uri=SIO['000300'], name="variantIdentifier__other", curie=SIO.curie('000300'),
                   model_uri=DEFAULT_.variantIdentifier__other, domain=None, range=Optional[str])

slots.variationSite__begins_at = Slot(uri=FALDO.begin, name="variationSite__begins_at", curie=FALDO.curie('begin'),
                   model_uri=DEFAULT_.variationSite__begins_at, domain=None, range=int)

slots.variationSite__ends_at = Slot(uri=FALDO.end, name="variationSite__ends_at", curie=FALDO.curie('end'),
                   model_uri=DEFAULT_.variationSite__ends_at, domain=None, range=int)

slots.variationSite__has_reference = Slot(uri=FALDO.reference, name="variationSite__has_reference", curie=FALDO.curie('reference'),
                   model_uri=DEFAULT_.variationSite__has_reference, domain=None, range=int)

slots.referenceAllele__value = Slot(uri=SIO['000300'], name="referenceAllele__value", curie=SIO.curie('000300'),
                   model_uri=DEFAULT_.referenceAllele__value, domain=None, range=str)

slots.alternateAllele__value = Slot(uri=SIO['000300'], name="alternateAllele__value", curie=SIO.curie('000300'),
                   model_uri=DEFAULT_.alternateAllele__value, domain=None, range=str)

