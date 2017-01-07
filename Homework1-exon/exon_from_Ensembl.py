import csv

ensembl_file="mart_export.txt"
with open(ensembl_file,'r')as f1:
    file=csv.reader(f1,delimiter="\t")
    next(file)

    cds_sum=0
    exon_sum=0

    cds_dict={} # dict is faster than list
    exon_dict={}

    for record in file:
        chr=record[3]
        exon_start=record[5]
        exon_end=record[6]
        exon=chr+":"+exon_start+"-"+exon_end
        if exon not in exon_dict:
            exon_dict[exon]=""
            exon_sum+=(int(exon_end)-int(exon_start))

        if record[7] != "":
            cds_start=record[7]
            cds_end=record[8]
            cds=chr+":"+cds_start+"-"+cds_end
            if cds not in cds_dict:
                cds_dict[cds]=""
                cds_sum+=(int(cds_end)-int(cds_start))

print(cds_sum)
print(exon_sum)