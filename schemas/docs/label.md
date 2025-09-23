

# Slot: label 


_A human-readable relatable name for the sequence (e.g. chr1)._





URI: [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)
Alias: label

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssemblySequence](AssemblySequence.md) | AssemblySequence is a chromosome or sequence in a reference genome |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:label |
| native | https://w3id.org/neugenfair/schema/label |
| exact | rdfs:label |




## LinkML Source

<details>
```yaml
name: label
description: A human-readable relatable name for the sequence (e.g. chr1).
from_schema: https://w3id.org/neugenfair/schema
exact_mappings:
- rdfs:label
rank: 1000
domain: AssemblySequence
slot_uri: rdfs:label
alias: label
domain_of:
- AssemblySequence
range: string

```
</details>