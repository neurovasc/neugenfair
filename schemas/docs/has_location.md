

# Slot: has_location 


_Links the sequence alteration to its location._





URI: [faldo:location](http://biohackathon.org/resource/faldo#location)
Alias: has_location

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SequenceAlteration](SequenceAlteration.md) | A representation of a sequence alteration |  no  |






## Properties

* Range: [VariationSite](VariationSite.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faldo:location |
| native | https://w3id.org/neugenfair/schema/has_location |
| exact | faldo:location |




## LinkML Source

<details>
```yaml
name: has_location
description: Links the sequence alteration to its location.
from_schema: https://w3id.org/neugenfair/schema
exact_mappings:
- faldo:location
rank: 1000
slot_uri: faldo:location
alias: has_location
domain_of:
- SequenceAlteration
range: VariationSite
required: false

```
</details>