filename ='C:\Temp\ACTIVEHEALTHYY1.txt'
filenamenew = filename.split('.')
with open(filename,'r') as ofileo, open(filenamenew[0]+'1.txt','w') as onewfileo:
    last='dummy'
    done = 20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001200000000000000000000000000000000000000
    for line in ofileo:
        dates = line.split('*')
        if dates[1] == '348':
            last = dates[3]
        elif dates[1] =='349':
            if dates[3]<last:
                line.replace(dates[3],last)
        onewfileo.write(line)
        done =done+1
        print(bin(done))
        
