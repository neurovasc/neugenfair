

# Class: AlternateAllele 


_Represents the alternate allele (geno:0000002)._





URI: [geno:0000002](http://purl.obolibrary.org/obo/GENO_0000002)





```mermaid
 classDiagram
    class AlternateAllele
    click AlternateAllele href "../AlternateAllele/"
      AlternateAllele : value
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The value of the alternate allele | direct |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | geno:0000002 |
| native | https://w3id.org/neugenfair/schema/AlternateAllele |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AlternateAllele
description: Represents the alternate allele (geno:0000002).
from_schema: https://w3id.org/neugenfair/schema
attributes:
  value:
    name: value
    description: The value of the alternate allele.
    from_schema: https://w3id.org/neugenfair/schema
    rank: 1000
    slot_uri: sio:000300
    domain_of:
    - AlternateAllele
    - ReferenceAllele
    range: string
    required: true
class_uri: geno:0000002

```
</details>

### Induced

<details>
```yaml
name: AlternateAllele
description: Represents the alternate allele (geno:0000002).
from_schema: https://w3id.org/neugenfair/schema
attributes:
  value:
    name: value
    description: The value of the alternate allele.
    from_schema: https://w3id.org/neugenfair/schema
    rank: 1000
    slot_uri: sio:000300
    alias: value
    owner: AlternateAllele
    domain_of:
    - AlternateAllele
    - ReferenceAllele
    range: string
    required: true
class_uri: geno:0000002

```
</details>