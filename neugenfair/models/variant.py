# Auto generated from model_Variant.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-09-22T14:01:03
# Schema: NeugenFAIRSchema
#
# id: https://w3id.org/neugenfair/schema
# description: Schema for the NeugenFAIR tool. Defines Individuals and Variants, supporting FAIR transformation of genomic and clinical data into Linked Data.
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
EX = CurieNamespace('ex', 'http://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/neugenfair/schema/')


# Types

# Class references



@dataclass(repr=False)
class Variant(YAMLRoot):
    """
    A genomic variant observed in the study.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/Variant")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Variant"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/Variant")

    chrom: Optional[str] = None
    pos: Optional[int] = None
    ref: Optional[str] = None
    alt: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.chrom is not None and not isinstance(self.chrom, str):
            self.chrom = str(self.chrom)

        if self.pos is not None and not isinstance(self.pos, int):
            self.pos = int(self.pos)

        if self.ref is not None and not isinstance(self.ref, str):
            self.ref = str(self.ref)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.variant__chrom = Slot(uri=DEFAULT_.chrom, name="variant__chrom", curie=DEFAULT_.curie('chrom'),
                   model_uri=DEFAULT_.variant__chrom, domain=None, range=Optional[str])

slots.variant__pos = Slot(uri=DEFAULT_.pos, name="variant__pos", curie=DEFAULT_.curie('pos'),
                   model_uri=DEFAULT_.variant__pos, domain=None, range=Optional[int])

slots.variant__ref = Slot(uri=DEFAULT_.ref, name="variant__ref", curie=DEFAULT_.curie('ref'),
                   model_uri=DEFAULT_.variant__ref, domain=None, range=Optional[str])

slots.variant__alt = Slot(uri=DEFAULT_.alt, name="variant__alt", curie=DEFAULT_.curie('alt'),
                   model_uri=DEFAULT_.variant__alt, domain=None, range=Optional[str])

