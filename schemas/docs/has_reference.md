

# Slot: has_reference 


_The reference sequence (contig, sequence, chromosome)._





URI: [faldo:reference](http://biohackathon.org/resource/faldo#reference)
Alias: has_reference

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Region](Region.md) | (genomic) Region of a SequenceAlteration |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faldo:reference |
| native | https://w3id.org/neugenfair/schema/has_reference |
| undefined | faldo:reference |




## LinkML Source

<details>
```yaml
name: has_reference
description: The reference sequence (contig, sequence, chromosome).
from_schema: https://w3id.org/neugenfair/schema
mappings:
- faldo:reference
rank: 1000
domain: Region
slot_uri: faldo:reference
alias: has_reference
domain_of:
- Region
range: string
required: true

```
</details>