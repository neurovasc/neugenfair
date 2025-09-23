

# Slot: has_value 


_The value of the identifier._





URI: [sio:000300](http://semanticscience.org/resource/SIO_000300)
Alias: has_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VariantIdentifier](VariantIdentifier.md) | A unique identifier for a sequence alteration within a database or nomenclatu... |  no  |
| [AssemblySequence](AssemblySequence.md) | AssemblySequence is a chromosome or sequence in a reference genome |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sio:000300 |
| native | https://w3id.org/neugenfair/schema/has_value |
| undefined | sio:000300 |




## LinkML Source

<details>
```yaml
name: has_value
description: The value of the identifier.
from_schema: https://w3id.org/neugenfair/schema
mappings:
- sio:000300
rank: 1000
domain: VariantIdentifier
slot_uri: sio:000300
alias: has_value
domain_of:
- AssemblySequence
- VariantIdentifier
range: string
required: true

```
</details>