

# Slot: ends_at 


_The end of the location of the sequence alteration._





URI: [faldo:end](http://biohackathon.org/resource/faldo#end)
Alias: ends_at

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Region](Region.md) | (genomic) Region of a SequenceAlteration |  no  |






## Properties

* Range: [Position](Position.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faldo:end |
| native | https://w3id.org/neugenfair/schema/ends_at |
| exact | faldo:end |




## LinkML Source

<details>
```yaml
name: ends_at
description: The end of the location of the sequence alteration.
from_schema: https://w3id.org/neugenfair/schema
exact_mappings:
- faldo:end
rank: 1000
domain: Region
slot_uri: faldo:end
alias: ends_at
domain_of:
- Region
range: Position
required: true

```
</details>