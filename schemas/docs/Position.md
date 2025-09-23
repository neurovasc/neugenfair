

# Class: Position 


_(genomic) Position._





URI: [faldo:ExactPosition](http://biohackathon.org/resource/faldo#ExactPosition)





```mermaid
 classDiagram
    class Position
    click Position href "../Position/"
      Position : position
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [position](position.md) | 1 <br/> [Integer](Integer.md) | Exact (genomic) Position of a SequenceAlteration | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Position](Position.md) | [position](position.md) | domain | [Position](Position.md) |
| [Region](Region.md) | [begins_at](begins_at.md) | range | [Position](Position.md) |
| [Region](Region.md) | [ends_at](ends_at.md) | range | [Position](Position.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faldo:ExactPosition |
| native | https://w3id.org/neugenfair/schema/Position |
| close | so:0000735 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Position
description: (genomic) Position.
from_schema: https://w3id.org/neugenfair/schema
close_mappings:
- so:0000735
attributes:
  position:
    name: position
    description: Exact (genomic) Position of a SequenceAlteration.
    from_schema: https://w3id.org/neugenfair/schema
    exact_mappings:
    - geno:0000903
    domain: Position
    slot_uri: faldo:position
    domain_of:
    - Position
    range: integer
    required: true
class_uri: faldo:ExactPosition

```
</details>

### Induced

<details>
```yaml
name: Position
description: (genomic) Position.
from_schema: https://w3id.org/neugenfair/schema
close_mappings:
- so:0000735
attributes:
  position:
    name: position
    description: Exact (genomic) Position of a SequenceAlteration.
    from_schema: https://w3id.org/neugenfair/schema
    exact_mappings:
    - geno:0000903
    domain: Position
    slot_uri: faldo:position
    alias: position
    owner: Position
    domain_of:
    - Position
    range: integer
    required: true
class_uri: faldo:ExactPosition

```
</details>