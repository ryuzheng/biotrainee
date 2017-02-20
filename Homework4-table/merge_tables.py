#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
/*
 * @Author: Ryu.Zheng 
 * @Date: 2017-02-19 17:55:49 
 * @Last Modified by:   Ryu.Zheng 
 * @Last Modified time: 2017-02-19 17:55:49 
 */
'''

import os
from collections import defaultdict
import gzip
import csv

gene_table=defaultdict(dict)
##NOTE: {gene_table: 
#           {Gene_ID:{filename:value},{filename:value},...},
#           {Gene_ID:{filename:value},{filename:value},...},
#           ...
#           }

file_list=[]

for root,dirs,files in os.walk("GSE48213_RAW"):
    for name in files:
        # print(name)
        with gzip.open(os.path.join("GSE48213_RAW",name),'rt') as gene_file:
            header=next(csv.reader(gene_file,delimiter="\t"))
            print(header)
            file_list.append(header[1])

            genes = csv.DictReader(gene_file,delimiter="\t",fieldnames=header)
            for line in genes:
                # print(line)
                if line[header[0]] in gene_table:
                    gene_table[line[header[0]]][header[1]]=line[header[1]]
                else:
                    gene_table[line[header[0]]]={header[1]:line[header[1]]}


with open("merge_table.txt",'w',newline="")as f2:
    csvwrite=csv.writer(f2,delimiter="\t")
    csvwrite.writerow(["Genes"]+file_list)

    for gene in sorted(gene_table):
        ## header
        # for name in gene_table[gene]:
        content=[gene_table[gene][name] for name in file_list]
        csvwrite.writerow([gene]+content)