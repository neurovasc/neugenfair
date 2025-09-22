

# Class: VariationSite 


_Represents the location of a sequence alteration._





URI: [faldo:Region](http://biohackathon.org/resource/faldo#Region)





```mermaid
 classDiagram
    class VariationSite
    click VariationSite href "../VariationSite/"
      VariationSite : begins_at
        
      VariationSite : ends_at
        
      VariationSite : has_reference
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [begins_at](begins_at.md) | 1 <br/> [Integer](Integer.md) | The beginning of the location of the sequence alteration | direct |
| [ends_at](ends_at.md) | 1 <br/> [Integer](Integer.md) | The end of the location of the sequence alteration | direct |
| [has_reference](has_reference.md) | 1 <br/> [Integer](Integer.md) | The reference sequence (contig, sequence, chromosome) | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SequenceAlteration](SequenceAlteration.md) | [has_location](has_location.md) | range | [VariationSite](VariationSite.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faldo:Region |
| native | https://w3id.org/neugenfair/schema/VariationSite |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VariationSite
description: Represents the location of a sequence alteration.
from_schema: https://w3id.org/neugenfair/schema
attributes:
  begins_at:
    name: begins_at
    description: The beginning of the location of the sequence alteration.
    from_schema: https://w3id.org/neugenfair/schema
    rank: 1000
    slot_uri: faldo:begin
    domain_of:
    - VariationSite
    range: integer
    required: true
  ends_at:
    name: ends_at
    description: The end of the location of the sequence alteration.
    from_schema: https://w3id.org/neugenfair/schema
    rank: 1000
    slot_uri: faldo:end
    domain_of:
    - VariationSite
    range: integer
    required: true
  has_reference:
    name: has_reference
    description: The reference sequence (contig, sequence, chromosome).
    from_schema: https://w3id.org/neugenfair/schema
    rank: 1000
    slot_uri: faldo:reference
    domain_of:
    - VariationSite
    range: integer
    required: true
class_uri: faldo:Region

```
</details>

### Induced

<details>
```yaml
name: VariationSite
description: Represents the location of a sequence alteration.
from_schema: https://w3id.org/neugenfair/schema
attributes:
  begins_at:
    name: begins_at
    description: The beginning of the location of the sequence alteration.
    from_schema: https://w3id.org/neugenfair/schema
    rank: 1000
    slot_uri: faldo:begin
    alias: begins_at
    owner: VariationSite
    domain_of:
    - VariationSite
    range: integer
    required: true
  ends_at:
    name: ends_at
    description: The end of the location of the sequence alteration.
    from_schema: https://w3id.org/neugenfair/schema
    rank: 1000
    slot_uri: faldo:end
    alias: ends_at
    owner: VariationSite
    domain_of:
    - VariationSite
    range: integer
    required: true
  has_reference:
    name: has_reference
    description: The reference sequence (contig, sequence, chromosome).
    from_schema: https://w3id.org/neugenfair/schema
    rank: 1000
    slot_uri: faldo:reference
    alias: has_reference
    owner: VariationSite
    domain_of:
    - VariationSite
    range: integer
    required: true
class_uri: faldo:Region

```
</details>