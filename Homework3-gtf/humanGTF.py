#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
/*
 * @Author: Ryu.Zheng 
 * @Date: 2017-02-12 22:10:08 
 * @Last Modified by: Ryu.Zheng
 * @Last Modified time: 2017-02-12 22:14:40
 */
'''
import gzip
import re

gtf_file = "Homo_sapiens.GRCh38.87.chr.gtf.gz"

with gzip.open(gtf_file, 'rt') as human_gtf:

    gene_dict={} #NOTE: {chr:[{gene1:coordinate1},{gene2:coordinate2}]}
    transcript_dict={} #NOTE: gene:transcript:coordinate
    exon_dict={} #NOTE: transcript:exon:coordinate
    cds_dict={} #NOTE: tarnascript:cds:coordinate
    for line in human_gtf:
        if "#!" not in line:
            content = line.strip().split("\t")
            # print(content)
            
            chro=content[0]
            coordinate=chro+":"+content[3]+"-"+content[4]

            gene_id = re.findall(r'gene_id "(.*?)";',content[8])[0] #NOTE: gene id must be found,so [0]
            transcript_id = re.findall(r'transcript_id "(.*?)";',content[8])
            exon_number = re.findall(r'exon_number "(.*?)";',content[8])
            cds_number = re.findall(r'exon_number "(.*?)";',content[8])


            # TITLE: generate data sets
            ## TITLE: analysis gene
            if content[2] == "gene":
                # print(gene_id)
                if chro in gene_dict:
                    gene_dict[chro].append({gene_id:coordinate})
                else:
                    gene_dict[chro]=[{gene_id:coordinate}]
                # print(gene_dict)

            ## TITLE: analysis transcript
            elif content[2] == "transcript":
                if gene_id in transcript_dict:
                    transcript_dict[gene_id].append({transcript_id[0]:coordinate})
                else:
                    transcript_dict[gene_id]=[{transcript_id[0]:coordinate}]
            
            ## TITLE: analysis exon_dict
            elif content[2] == "exon":
                if transcript_id[0] in exon_dict:
                    exon_dict[transcript_id[0]].append({exon_number[0]:coordinate})
                else:
                    exon_dict[transcript_id[0]]=[{exon_number[0]:coordinate}]
            
            elif content[2] == "CDS":
                if transcript_id[0] in cds_dict:
                    cds_dict[transcript_id[0]].append({cds_number[0]:coordinate})
                else:
                    cds_dict[transcript_id[0]]=[{cds_number[0]:coordinate}]

    # 计算每个染色体上的基因个数
    for k in gene_dict:
        print(k,len(gene_dict[k]))
    
    # 计算所有基因的转录本个数、平均个数
    gene_num=0
    transcript_num=0
    for k in transcript_dict:
        gene_num+=1
        transcript_num+=len(transcript_dict[k])
    # print(transcript_num,transcript_num)
    print(gene_num,transcript_num,"%.2f" % (transcript_num*1.0/gene_num))

    # 计算所有基因的外显子个数、平均个数
    transcript_num=0
    exon_num=0
    for k in exon_dict:
        transcript_num+=1
        exon_num+=len(exon_dict[k])
    # print(transcript_num,exon_num)
    print(transcript_num,exon_num,"%.2f" % (exon_num*1.0/transcript_num))

    transcript_num=0
    cds_number=0
    for k in cds_dict:
    	transcript_num+=1
    	cds_number+=len(cds_dict[k])
    # print(transcript_num,cds_number)
    print(transcript_num,cds_number,"%.2f" % (cds_number*1.0/transcript_num))