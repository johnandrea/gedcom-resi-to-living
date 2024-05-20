# given a GEDCOM file on stdinput,
# output a file with INDI LIVING events copied to RESI flags

import sys

in_indi = False
in_event = False
in_living = False
resi_data = []

def output_living( data ):
   print( '1 RESI' )
   for line in data:
       print( line, end='' )


for line in sys.stdin:
    parts = line.split()
    level = parts[0]
    tag = parts[1]

    if level == '0':
       # new person (or family or other top level thing)
       in_indi = ( len(parts) == 3 and parts[2] == 'INDI' )
       if resi_data:
          output_living( resi_data )
          resi_data = []
       in_event = False
       in_living = False

    if level == '1' and in_indi:
       # new section in individual
       if resi_data:
          output_living( resi_data )
          resi_data = []
       in_event = False
       in_living = False
           
       if tag == 'EVEN':
          in_event = True

    if level == '2' and in_event and tag == 'TYPE' and parts[2].upper() == 'LIVING':
       in_living = True

    if in_living and tag != 'TYPE':
       resi_data.append( line )

    print( line, end='' )
