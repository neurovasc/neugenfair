

# Slot: location 


_Links the SequenceAlteration to its (genomic) Region._





URI: [faldo:location](http://biohackathon.org/resource/faldo#location)
Alias: location

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SequenceAlteration](SequenceAlteration.md) | A representation of a SequenceAlteration |  no  |






## Properties

* Range: [Region](Region.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faldo:location |
| native | https://w3id.org/neugenfair/schema/location |
| exact | faldo:location |




## LinkML Source

<details>
```yaml
name: location
description: Links the SequenceAlteration to its (genomic) Region.
from_schema: https://w3id.org/neugenfair/schema
exact_mappings:
- faldo:location
rank: 1000
domain: SequenceAlteration
slot_uri: faldo:location
alias: location
domain_of:
- SequenceAlteration
range: Region
required: false

```
</details>