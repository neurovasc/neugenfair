

# Slot: has_reference 


_The reference sequence (contig, sequence, chromosome)._





URI: [faldo:reference](http://biohackathon.org/resource/faldo#reference)
Alias: has_reference

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VariationSite](VariationSite.md) | Represents the location of a sequence alteration |  no  |






## Properties

* Range: [Integer](Integer.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faldo:reference |
| native | https://w3id.org/neugenfair/schema/has_reference |




## LinkML Source

<details>
```yaml
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

```
</details>