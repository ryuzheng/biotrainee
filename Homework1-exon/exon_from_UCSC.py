import csv

ucsc_file="ucsc_cds.txt"
with open(ucsc_file,'r')as f1:
    exon_dict={}
    sum=0
    file=csv.reader(f1,delimiter="\t")
    next(file)
    for record in file:
        chr=record[1]
        exon_start_list=record[5].rstrip(",").split(",")
        exon_end_list=record[6].rstrip(",").split(",")
        pos=0
        while pos < len(exon_start_list):
            exon=chr+":"+exon_start_list[pos]+"-"+exon_end_list[pos]
            if exon not in exon_dict:
                exon_dict[exon]=""
                sum+=(int(exon_end_list[pos])-int(exon_start_list[pos]))
            pos+=1
print(sum)         

        