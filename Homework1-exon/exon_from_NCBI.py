import csv

ncbi_file="CCDS.20160908.txt"
with open(ncbi_file,'r')as f1:
    file=csv.reader(f1,delimiter="\t")
    next(file)
    sum=0
    exon_dict={} # dict is faster than list
    for record in file:
        if record[9] != "-":
            chr=record[0]
            exon_list=record[9].lstrip("[").rstrip("]").split(", ")
            # print(exon_list)
            for range in exon_list:
                exon=chr+":"+range
                # print(exon)
                if exon not in exon_dict:
                    exon_dict[exon]=""
                    exon_start=int(range.split("-")[0])
                    exon_end=int(range.split("-")[1])
                    # print(exon_start)
                    sum+=exon_end-exon_start
print(sum)
# print(exon_dict)