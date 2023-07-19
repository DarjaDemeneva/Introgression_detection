#!/bin/bash

bcf_files=`echo bcf_files/ALL.chr{1..22}.phase3_shapeit2_mvncall_integrated_v5.20130502.genotypes.bcf | sed 's/ /,/g'`
ancestral=`echo ancestral/homo_sapiens_ancestor_{1..22}.fa | sed 's/ /,/g'`

hmmix create_outgroup -ind=individuals.json -vcf=$bcf_files -weights=strictmask.bed  -out=outgroup.txt -ancestral=$ancestral 

hmmix mutation_rate -outgroup=outgroup.txt -weights=strictmask.bed -window_size=100000 -out=mutrate.bed

hmmix create_ingroup -ind="NA19625" -vcf=$bcf_files -weights=strictmask.bed -out=obs -outgroup=outgroup.txt -ancestral=$ancestral

# "ingroup": ["HG00096", "HG00097", "HG00099", "HG00100"] + "HG02922" (in outgroup) + "NA19017" (LWK, not in outgroup) + "NA19625" (ASW, not in outgroup)

hmmix train -obs=obs.NA19625.txt -weights=strictmask.bed -mutrates=mutrate.bed -out=trained.NA19625.phased.json -haploid

hmmix decode -obs=obs.NA19625.txt -weights=strictmask.bed -mutrates=mutrate.bed -param=trained.NA19625.phased.json -out=NA19625.decoded -haploid