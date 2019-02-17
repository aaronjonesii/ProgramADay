'''
Function:       Sniff packets of the current computer's local network
Date:           02.17.2019
Created By:     Anonymous Systems
Dependencies:   pyshark, tshark
'''
import pyshark
from datetime import datetime

def captureLivepackets(numberofpackets, filename, nic='en1'):
    print(f'Binding to Network Interface {nic}...')
    try:
        conn = pyshark.LiveCapture(interface=nic)
        print(f'Successfully binded to {nic}, now capturing {numberofpackets} packets')
        conn.sniff(packet_count=numberofpackets)
        print(f'Writing {numberofpackets} captured packets to {filename}')
        outstring = ''
        i = 1
        for packet in conn:
            outfile = open(filename.replace(' ', '_')+'.txt', 'w')
            outstring += f'Packet #{i}'
            outstring += '\n'
            outstring += str(packet)
            outstring += '\n'
            outfile.write(outstring)
            i = i + 1
        conn.close()
        print(f'All Done, open {filename} to view captured packets')
    except Exception as e:
        print(f'Was not able bind to {nic} => {e}')

if __name__ == '__main__':
    current_time = datetime.now().strftime('%c')
    captureLivepackets(numberofpackets=int(input('How many packets would you like to capture? ')), filename=current_time)
