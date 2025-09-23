

# Class: ReferenceAllele 


_Represents the reference allele (geno:0000036)._





URI: [geno:0000036](http://purl.obolibrary.org/obo/GENO_0000036)





```mermaid
 classDiagram
    class ReferenceAllele
    click ReferenceAllele href "../ReferenceAllele/"
      ReferenceAllele : value
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The value of the reference allele | direct |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | geno:0000036 |
| native | https://w3id.org/neugenfair/schema/ReferenceAllele |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReferenceAllele
description: Represents the reference allele (geno:0000036).
from_schema: https://w3id.org/neugenfair/schema
attributes:
  value:
    name: value
    description: The value of the reference allele.
    from_schema: https://w3id.org/neugenfair/schema
    slot_uri: sio:000300
    domain_of:
    - AlternateAllele
    - ReferenceAllele
    range: string
    required: true
class_uri: geno:0000036

```
</details>

### Induced

<details>
```yaml
name: ReferenceAllele
description: Represents the reference allele (geno:0000036).
from_schema: https://w3id.org/neugenfair/schema
attributes:
  value:
    name: value
    description: The value of the reference allele.
    from_schema: https://w3id.org/neugenfair/schema
    slot_uri: sio:000300
    alias: value
    owner: ReferenceAllele
    domain_of:
    - AlternateAllele
    - ReferenceAllele
    range: string
    required: true
class_uri: geno:0000036

```
</details>