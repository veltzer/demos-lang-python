#! /usr/bin/python

greek = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta',
 	    'Eta', 'Theta', 'Iota', 'Kappa', 'Lambda', 'Mu',
        'Nu', 'Xi', 'Omicron', 'Pi', 'Rho', 'Sigma final',
        'Sigma', 'Tau', 'Upsilon', 'Phi', 'Chi', 'Psi', 'Omega'
        ]

         
# Format required:
#    The hex value of the character.
#    The character name (cname), left justified,
#    maximum 12 characters.
#    A colon separator.
#    The lowercase Greek character.
#    The uppercase Greek character.

for pos, chr_name in enumerate(greek, start=0x03B1):
    try:
        char = chr(pos)  
        print(chr_name, ":", char)
    except UnicodeEncodeError as err:
        print(chr_name, 'unknown')
