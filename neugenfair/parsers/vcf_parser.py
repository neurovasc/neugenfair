import pandas as pd
from typing import List, Dict
import re

def read_vcf_minimal(path: str) -> pd.DataFrame:
    """Read minimal VCF into a DataFrame; preserves header names."""
    # find header (#CHROM) line to get column names
    with open(path, 'r') as fh:
        header_line = None
        for line in fh:
            if line.startswith('#CHROM') or line.startswith('#CHROM\t') or line.startswith('#CHROM '):
                header_line = line.strip()
                break
    if header_line is None:
        raise ValueError("No header line '#CHROM' found in VCF.")
    colnames = re.split(r'\s+', header_line.lstrip('#'))
    df = pd.read_csv(path, sep='\t', comment='#', names=colnames, dtype=str, keep_default_na=False)
    return df

def vcf_to_variants(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert VCF dataframe rows into a DataFrame of variants.
    Each ALT allele becomes one row (one SequenceAlteration).
    Minimal fields provided: chrom, pos, ref, alt, id
    """
    variants: List[Dict] = []
    
    for _, row in df.iterrows():
        chrom = row.get('CHROM') or row.get('#CHROM')
        pos = row['POS']
        ref = row['REF']
        alt_field = row['ALT']
        vid = row.get('ID') or None
        
        # ALT may be comma separated
        alts = alt_field.split(',') if alt_field else []
        
        for alt in alts:
            variants.append({
                'chrom': chrom,
                'pos': int(pos),
                'ref': ref,
                'alt': alt,
                'id': vid
            })
    
    return pd.DataFrame(variants)