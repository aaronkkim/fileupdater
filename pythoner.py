filename ='C:\Temp\ACTIVEHEALTHYY1.txt'
filenamenew = filename.split('.')
with open(filename,'r') as ofileo, open(filenamenew[0]+'1.txt','w') as onewfileo:
    last='dummy'
    for line in ofileo:
        dates = line.split('*')
        if dates[1] == '348':
            last = dates[3]
        elif dates[1] =='349':
            if dates[3][:8]<last[:8]:
               dates[3] = last
        onewfileo.write('*'.join(dates))
        