

# Slot: value 


_The nucleic composition of the reference allele._





URI: [sio:000300](http://semanticscience.org/resource/SIO_000300)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReferenceAllele](ReferenceAllele.md) | Represents the ReferenceAllele, found on the reference sequence when performi... |  no  |
| [AlternateAllele](AlternateAllele.md) | Represents the AlternateAllele, found upon mapping (genome) read sequencing f... |  no  |






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
| native | https://w3id.org/neugenfair/schema/value |
| exact | sio:000300 |




## LinkML Source

<details>
```yaml
name: value
description: The nucleic composition of the reference allele.
from_schema: https://w3id.org/neugenfair/schema
exact_mappings:
- sio:000300
rank: 1000
slot_uri: sio:000300
alias: value
domain_of:
- AlternateAllele
- ReferenceAllele
range: string
required: true

```
</details>