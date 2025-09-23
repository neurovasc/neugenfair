

# Slot: has_source 


_The nomenclature or database of the identifier (e.g. HGVS, dbSNP)._





URI: [sio:000253](http://semanticscience.org/resource/SIO_000253)
Alias: has_source

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VariantIdentifier](VariantIdentifier.md) | A unique identifier for a sequence alteration within a database or nomenclatu... |  no  |






## Properties

* Range: [Nomenclature](Nomenclature.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sio:000253 |
| native | https://w3id.org/neugenfair/schema/has_source |
| undefined | sio:000253 |




## LinkML Source

<details>
```yaml
name: has_source
description: The nomenclature or database of the identifier (e.g. HGVS, dbSNP).
from_schema: https://w3id.org/neugenfair/schema
mappings:
- sio:000253
rank: 1000
domain: VariantIdentifier
slot_uri: sio:000253
alias: has_source
domain_of:
- VariantIdentifier
range: Nomenclature
required: true

```
</details>