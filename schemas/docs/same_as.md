

# Slot: same_as 


_Link to an external reference for the sequence (e.g. a URI from a genome browser or database)._





URI: [owl:sameAs](http://www.w3.org/2002/07/owl#sameAs)
Alias: same_as

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
| self | owl:sameAs |
| native | https://w3id.org/neugenfair/schema/same_as |
| exact | owl:sameAs |




## LinkML Source

<details>
```yaml
name: same_as
description: Link to an external reference for the sequence (e.g. a URI from a genome
  browser or database).
from_schema: https://w3id.org/neugenfair/schema
exact_mappings:
- owl:sameAs
rank: 1000
domain: AssemblySequence
slot_uri: owl:sameAs
alias: same_as
domain_of:
- AssemblySequence
range: string

```
</details>