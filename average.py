#!/opt/local/bin/python

atxt = open("/Users/fenghai/Documents/inforsince/overlayweaver/scenario/test-scenario-out","r+");
book = atxt.readlines();#read line
sum = 0;
i = 0;#number of digits
strin = "route[0] (length";#target line

for x in book:
	if x.find(strin) > -1:
		sum += int(filter(str.isdigit,x))
		i += 1;

print float(sum)/float(i)
print i

atxt.close()