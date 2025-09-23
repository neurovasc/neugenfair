# Enum: Nomenclature 




_The nomenclature or database system used for the identifier._



URI: [https://w3id.org/neugenfair/schema/Nomenclature](https://w3id.org/neugenfair/schema/Nomenclature)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| HGVS | None | Human Genome Variation Society nomenclature |
| dbSNP | None | Database of Single Nucleotide Polymorphisms |
| rsID | None | Reference SNP cluster ID from dbSNP |
| ClinVar | None | Clinical significance database for variants |
| COSMIC | None | Catalogue Of Somatic Mutations In Cancer |
| Ensembl | None | Ensembl database identifier |
| HUGO | None | Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC)-approved ... |
| Other | None | Other nomenclature or database not listed |




## Slots

| Name | Description |
| ---  | --- |
| [has_source](has_source.md) | The nomenclature or database of the identifier (e |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/neugenfair/schema






## LinkML Source

<details>
```yaml
name: Nomenclature
description: The nomenclature or database system used for the identifier.
from_schema: https://w3id.org/neugenfair/schema
rank: 1000
permissible_values:
  HGVS:
    text: HGVS
    description: Human Genome Variation Society nomenclature.
  dbSNP:
    text: dbSNP
    description: Database of Single Nucleotide Polymorphisms.
  rsID:
    text: rsID
    description: Reference SNP cluster ID from dbSNP.
  ClinVar:
    text: ClinVar
    description: Clinical significance database for variants.
  COSMIC:
    text: COSMIC
    description: Catalogue Of Somatic Mutations In Cancer.
  Ensembl:
    text: Ensembl
    description: Ensembl database identifier.
  HUGO:
    text: HUGO
    description: Human Genome Organization (HUGO) Gene Nomenclature Committee (HGNC)-approved
      gene nomenclature.
  Other:
    text: Other
    description: Other nomenclature or database not listed.

```
</details>