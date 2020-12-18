mylist=[]
devno=int(input('How many devices : '))
for i in range(devno):
    mydev=input('Please Enter your device name : ')
    mylist.append(mydev)
print('*' * 10 + ' Device List ' + '*' * 10 + '\n\n' )
for i in range(devno):
    print('The Device No.' + str(i) + ' is: ' + str(mylist[i])+ '\n')
print('*' * 10 + ' End of Device  List ' + '*' * 10  )    
