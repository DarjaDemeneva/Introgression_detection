#!/bin/bash

bcf_files=`echo bcf_files/ALL.chr{1..22}.phase3_shapeit2_mvncall_integrated_v5.20130502.genotypes.bcf | sed 's/ /,/g'`
ancestral=`echo ancestral/homo_sapiens_ancestor_{1..22}.fa | sed 's/ /,/g'`
reference=`echo reference37/chr{1..22}.fa | sed 's/ /,/g'`
# admixref=

# hmmix create_outgroup -ind=individuals.json -vcf=$bcf_files -weights=strictmask.bed  -out=outgroup.txt -ancestral=$ancestral -refgenome=$reference

# hmmix mutation_rate -outgroup=outgroup.txt -weights=strictmask.bed -window_size=100000 -out=mutrate.bed

# hmmix create_ingroup -ind=individuals.json -vcf=$bcf_files -weights=strictmask.bed -out=obs -outgroup=outgroup.txt -ancestral=$ancestral

hmmix train -obs=obs.HG00437.txt -weights=strictmask.bed -mutrates=mutrate.bed -out=trained.HG00437.phased.json -haploid

hmmix decode -obs=obs.HG00437.txt -weights=strictmask.bed -mutrates=mutrate.bed -param=trained.HG00437.phased.json -out=HG00437.decoded -haploid 