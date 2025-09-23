

# Class: Region 


_(genomic) Region of a SequenceAlteration._





URI: [faldo:Region](http://biohackathon.org/resource/faldo#Region)





```mermaid
 classDiagram
    class Region
    click Region href "../Region/"
      Region : begins_at
        
          
    
        
        
        Region --> "1" Position : begins_at
        click Position href "../Position/"
    

        
      Region : ends_at
        
          
    
        
        
        Region --> "1" Position : ends_at
        click Position href "../Position/"
    

        
      Region : has_reference
        
          
    
        
        
        Region --> "1" AssemblySequence : has_reference
        click AssemblySequence href "../AssemblySequence/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [begins_at](begins_at.md) | 1 <br/> [Position](Position.md) | The beginning of the location of the sequence alteration | direct |
| [ends_at](ends_at.md) | 1 <br/> [Position](Position.md) | The end of the location of the sequence alteration | direct |
| [has_reference](has_reference.md) | 1 <br/> [AssemblySequence](AssemblySequence.md) | The reference sequence (contig, sequence, chromosome) | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Region](Region.md) | [begins_at](begins_at.md) | domain | [Region](Region.md) |
| [Region](Region.md) | [ends_at](ends_at.md) | domain | [Region](Region.md) |
| [Region](Region.md) | [has_reference](has_reference.md) | domain | [Region](Region.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | faldo:Region |
| native | https://w3id.org/neugenfair/schema/Region |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Region
description: (genomic) Region of a SequenceAlteration.
from_schema: https://w3id.org/neugenfair/schema
attributes:
  begins_at:
    name: begins_at
    description: The beginning of the location of the sequence alteration.
    from_schema: https://w3id.org/neugenfair/schema
    exact_mappings:
    - faldo:begin
    domain: Region
    slot_uri: faldo:begin
    domain_of:
    - Region
    range: Position
    required: true
  ends_at:
    name: ends_at
    description: The end of the location of the sequence alteration.
    from_schema: https://w3id.org/neugenfair/schema
    exact_mappings:
    - faldo:end
    domain: Region
    slot_uri: faldo:end
    domain_of:
    - Region
    range: Position
    required: true
  has_reference:
    name: has_reference
    description: The reference sequence (contig, sequence, chromosome).
    from_schema: https://w3id.org/neugenfair/schema
    exact_mappings:
    - faldo:reference
    domain: Region
    slot_uri: faldo:reference
    domain_of:
    - Region
    range: AssemblySequence
    required: true
class_uri: faldo:Region

```
</details>

### Induced

<details>
```yaml
name: Region
description: (genomic) Region of a SequenceAlteration.
from_schema: https://w3id.org/neugenfair/schema
attributes:
  begins_at:
    name: begins_at
    description: The beginning of the location of the sequence alteration.
    from_schema: https://w3id.org/neugenfair/schema
    exact_mappings:
    - faldo:begin
    domain: Region
    slot_uri: faldo:begin
    alias: begins_at
    owner: Region
    domain_of:
    - Region
    range: Position
    required: true
  ends_at:
    name: ends_at
    description: The end of the location of the sequence alteration.
    from_schema: https://w3id.org/neugenfair/schema
    exact_mappings:
    - faldo:end
    domain: Region
    slot_uri: faldo:end
    alias: ends_at
    owner: Region
    domain_of:
    - Region
    range: Position
    required: true
  has_reference:
    name: has_reference
    description: The reference sequence (contig, sequence, chromosome).
    from_schema: https://w3id.org/neugenfair/schema
    exact_mappings:
    - faldo:reference
    domain: Region
    slot_uri: faldo:reference
    alias: has_reference
    owner: Region
    domain_of:
    - Region
    range: AssemblySequence
    required: true
class_uri: faldo:Region

```
</details>