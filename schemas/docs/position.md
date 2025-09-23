

# Slot: position 


_Exact (genomic) Position of a SequenceAlteration._





URI: [faldo:position](http://biohackathon.org/resource/faldo#position)
Alias: position

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Position](Position.md) | (genomic) Position |  no  |






## Properties

* Range: [Integer](Integer.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faldo:position |
| native | https://w3id.org/neugenfair/schema/position |
| exact | geno:0000903 |




## LinkML Source

<details>
```yaml
name: position
description: Exact (genomic) Position of a SequenceAlteration.
from_schema: https://w3id.org/neugenfair/schema
exact_mappings:
- geno:0000903
rank: 1000
domain: Position
slot_uri: faldo:position
alias: position
domain_of:
- Position
range: integer
required: true

```
</details>