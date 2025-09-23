

# Class: ReferenceAllele 


_Represents the ReferenceAllele, found on the reference sequence when performing variant calling._





URI: [geno:0000036](http://purl.obolibrary.org/obo/GENO_0000036)





```mermaid
 classDiagram
    class ReferenceAllele
    click ReferenceAllele href "../ReferenceAllele/"
      ReferenceAllele : value
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The nucleic composition of the reference allele | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReferenceAllele](ReferenceAllele.md) | [value](value.md) | domain | [ReferenceAllele](ReferenceAllele.md) |
| [SequenceAlteration](SequenceAlteration.md) | [has_reference_part](has_reference_part.md) | range | [ReferenceAllele](ReferenceAllele.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | geno:0000036 |
| native | https://w3id.org/neugenfair/schema/ReferenceAllele |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReferenceAllele
description: Represents the ReferenceAllele, found on the reference sequence when
  performing variant calling.
from_schema: https://w3id.org/neugenfair/schema
attributes:
  value:
    name: value
    description: The nucleic composition of the reference allele.
    from_schema: https://w3id.org/neugenfair/schema
    exact_mappings:
    - sio:000300
    domain: ReferenceAllele
    slot_uri: sio:000300
    domain_of:
    - AlternateAllele
    - ReferenceAllele
    range: string
    required: true
class_uri: geno:0000036

```
</details>

### Induced

<details>
```yaml
name: ReferenceAllele
description: Represents the ReferenceAllele, found on the reference sequence when
  performing variant calling.
from_schema: https://w3id.org/neugenfair/schema
attributes:
  value:
    name: value
    description: The nucleic composition of the reference allele.
    from_schema: https://w3id.org/neugenfair/schema
    exact_mappings:
    - sio:000300
    domain: ReferenceAllele
    slot_uri: sio:000300
    alias: value
    owner: ReferenceAllele
    domain_of:
    - AlternateAllele
    - ReferenceAllele
    range: string
    required: true
class_uri: geno:0000036

```
</details>