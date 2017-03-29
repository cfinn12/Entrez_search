from Bio import Entrez

while True:
    choice = int(input('Which input mode? Manual input = 0, File input = 1: '))
    if choice == 0:
        print('Manual mode')
        Entrez.email = input('Enter e-mail address: ')
        org1 = input('What organism?: ')
        organism = org1 + str('[Organism] AND ')
        begin = input('Beginning Date: ')
        end = input('End Date: ') + str('[PDAT]')
        term_in = organism + begin + ':' + end
        handle = Entrez.esearch(db="nucleotide", term=term_in)
        record = Entrez.read(handle)
        print(str(record["Count"]) + ' GenBank Entries for ' + org1 + ' in that date range.'
                                                                      + ' Subject to addition of new entries')
        break
    elif choice == 1:
        print('File Input mode')
        fname = input('Enter file name: ')
        with open(fname) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        a, x, y, z = content
        Entrez.email = a
        organism = x + str('[Organism] AND ')
        begin = y
        end = z + str('[PDAT]')
        term_in = organism + begin + ':' + end
        handle = Entrez.esearch(db="nucleotide", term=term_in)
        record = Entrez.read(handle)
        print(str(record["Count"]) + ' GenBank Entries for ' + x + ' in that date range.'
                                                                   + ' Subject to addition of new entries')
        break
