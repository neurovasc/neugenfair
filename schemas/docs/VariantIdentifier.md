

# Class: VariantIdentifier 


_A unique identifier for a sequence alteration within a database or nomenclature._





URI: [sio:000675](http://semanticscience.org/resource/SIO_000675)





```mermaid
 classDiagram
    class VariantIdentifier
    click VariantIdentifier href "../VariantIdentifier/"
      VariantIdentifier : has_source
        
          
    
        
        
        VariantIdentifier --> "1" Nomenclature : has_source
        click Nomenclature href "../Nomenclature/"
    

        
      VariantIdentifier : has_value
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [has_value](has_value.md) | 1 <br/> [String](String.md) | The value of the identifier | direct |
| [has_source](has_source.md) | 1 <br/> [Nomenclature](Nomenclature.md) | The nomenclature or database of the identifier (e | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [VariantIdentifier](VariantIdentifier.md) | [has_value](has_value.md) | domain | [VariantIdentifier](VariantIdentifier.md) |
| [VariantIdentifier](VariantIdentifier.md) | [has_source](has_source.md) | domain | [VariantIdentifier](VariantIdentifier.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sio:000675 |
| native | https://w3id.org/neugenfair/schema/VariantIdentifier |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VariantIdentifier
description: A unique identifier for a sequence alteration within a database or nomenclature.
from_schema: https://w3id.org/neugenfair/schema
attributes:
  has_value:
    name: has_value
    description: The value of the identifier.
    from_schema: https://w3id.org/neugenfair/schema
    mappings:
    - sio:000300
    domain: VariantIdentifier
    slot_uri: sio:000300
    domain_of:
    - AssemblySequence
    - VariantIdentifier
    range: string
    required: true
  has_source:
    name: has_source
    description: The nomenclature or database of the identifier (e.g. HGVS, dbSNP).
    from_schema: https://w3id.org/neugenfair/schema
    mappings:
    - sio:000253
    domain: VariantIdentifier
    slot_uri: sio:000253
    domain_of:
    - VariantIdentifier
    range: Nomenclature
    required: true
class_uri: sio:000675

```
</details>

### Induced

<details>
```yaml
name: VariantIdentifier
description: A unique identifier for a sequence alteration within a database or nomenclature.
from_schema: https://w3id.org/neugenfair/schema
attributes:
  has_value:
    name: has_value
    description: The value of the identifier.
    from_schema: https://w3id.org/neugenfair/schema
    mappings:
    - sio:000300
    domain: VariantIdentifier
    slot_uri: sio:000300
    alias: has_value
    owner: VariantIdentifier
    domain_of:
    - AssemblySequence
    - VariantIdentifier
    range: string
    required: true
  has_source:
    name: has_source
    description: The nomenclature or database of the identifier (e.g. HGVS, dbSNP).
    from_schema: https://w3id.org/neugenfair/schema
    mappings:
    - sio:000253
    domain: VariantIdentifier
    slot_uri: sio:000253
    alias: has_source
    owner: VariantIdentifier
    domain_of:
    - VariantIdentifier
    range: Nomenclature
    required: true
class_uri: sio:000675

```
</details>