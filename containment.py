mylist=['CISCO', 'ARISTA','HP']
device = input('Enter your device vendore: ')
device= device.upper()
if device in mylist :
    print('Device founded ...\n\n')
    print( 'The device is '+ device)
else:
    print('#######Device not Found########')
    print('\n\n The device is : '+ device)