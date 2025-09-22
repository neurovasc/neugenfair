# Auto generated from model_Individual.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-09-22T14:01:00
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
class IndividualId(extended_str):
    pass


@dataclass(repr=False)
class Individual(YAMLRoot):
    """
    A study participant in a genomic/clinical cohort.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/Individual")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Individual"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/neugenfair/schema/Individual")

    id: Union[str, IndividualId] = None
    sex: Optional[str] = None
    age: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IndividualId):
            self.id = IndividualId(self.id)

        if self.sex is not None and not isinstance(self.sex, str):
            self.sex = str(self.sex)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.individual__id = Slot(uri=DEFAULT_.id, name="individual__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.individual__id, domain=None, range=URIRef)

slots.individual__sex = Slot(uri=DEFAULT_.sex, name="individual__sex", curie=DEFAULT_.curie('sex'),
                   model_uri=DEFAULT_.individual__sex, domain=None, range=Optional[str])

slots.individual__age = Slot(uri=DEFAULT_.age, name="individual__age", curie=DEFAULT_.curie('age'),
                   model_uri=DEFAULT_.individual__age, domain=None, range=Optional[int])

