#fname=raw_input("Enter a file name:")
#fh=open(fname)
#for line in fh:
#    if line.startswith("X-DSPAM-Confidence:"):
#        print line

fname=raw_input("Enter a file name:")
fh=open(fname)
for line in fh:
    line=line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        words=line.split()
        flo=words[1]
        add=sum(flo)
        print add
