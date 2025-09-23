

# Slot: begins_at 


_The beginning of the location of the sequence alteration._





URI: [faldo:begin](http://biohackathon.org/resource/faldo#begin)
Alias: begins_at

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Region](Region.md) | (genomic) Region of a SequenceAlteration |  no  |






## Properties

* Range: [Integer](Integer.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faldo:begin |
| native | https://w3id.org/neugenfair/schema/begins_at |
| undefined | faldo:begin |




## LinkML Source

<details>
```yaml
name: begins_at
description: The beginning of the location of the sequence alteration.
from_schema: https://w3id.org/neugenfair/schema
mappings:
- faldo:begin
rank: 1000
domain: Region
slot_uri: faldo:begin
alias: begins_at
domain_of:
- Region
range: integer
required: true

```
</details>