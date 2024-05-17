# given a GEDCOM file on stdinput,
# output a file with INDI RESI tags copied to LIVING events

import sys

in_indi = False
in_resi = False
resi_data = []

def output_living( data ):
   print( '1 EVEN' )
   print( '2 TYPE Living' )
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
       in_resi = False

    if level == '1' and in_indi:
       # new section in individual
       if resi_data:
          output_living( resi_data )
          resi_data = []
       in_resi = False
           
       if tag == 'RESI':
          in_resi = True

    if in_resi and level != '1':
       resi_data.append( line )

    print( line, end='' )
