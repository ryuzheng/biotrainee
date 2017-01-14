hg19_reference='hg19.fa'
# hg19_reference="test.fa"


with open(hg19_reference,'r')as genome,open("summary.txt",'w')as result:

    result.write("\t".join(("chromosome","length","N number","N percent","GC number","GC percent","\n")))
    summary=["",0.0,0.0,0.0] # chrom, length, #N, #GC
    for line in genome:
        # print(line)
        if line.startswith(">"):
            if summary[0] != "":
                len_seq="%d" % summary[1]
                len_N="%d" % summary[2]
                percent_N="%.02f" % (summary[2]/summary[1])
                len_GC="%d" % summary[3]
                percent_GC="%.02f" % (summary[3]/(summary[1]-summary[2]))
                result.write("\t".join((summary[0],len_seq,len_N,percent_N,len_GC,percent_GC,"\n")))
            print(line)
            summary=["",0.0,0.0,0.0]
            summary[0]=line.strip()
        else:
            summary[1]+=len(line.strip())
            summary[2]+=line.count("N")
            summary[3]+=line.count("G")+line.count("C")+line.count("g")+line.count("c")
    len_seq="%d" % summary[1]
    len_N="%d" % summary[2]
    percent_N="%.02f" % (summary[2]/summary[1])
    len_GC="%d" % summary[3]
    percent_GC="%.02f" % (summary[3]/(summary[1]-summary[2]))
    result.write("\t".join((summary[0],len_seq,len_N,percent_N,len_GC,percent_GC,"\n")))