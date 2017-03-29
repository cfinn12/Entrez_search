from Bio import Entrez

while True:
    choice = int(input('Which input mode? Manual input = 0, File input = 1: '))
    if choice == 0:
        print('Manual mode')
        org1 = input('What organism?: ')
        organism = org1 + str('[Organism] AND ')
        begin = input('Beginning Date: ')
        end = input('End Date: ') + str('[PDAT]')
        term_in = organism + begin + ':' + end
        handle = Entrez.esearch(db="nucleotide", term=term_in)
        record = Entrez.read(handle)
        print(str(record["Count"]) + ' GenBank Entries for ' + org1 + ' in that date range.')
        break
    elif choice == 1:
        print('File Input mode')
        fname = input('Enter file name: ')
        with open(fname) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        x, y, z = content
        organism = x + str('[Organism] AND ')
        begin = y
        end = z + str('[PDAT]')
        term_in = organism + begin + ':' + end
        handle = Entrez.esearch(db="nucleotide", term=term_in)
        record = Entrez.read(handle)
        print(str(record["Count"]) + ' GenBank Entries for ' + x + ' in that date range.')
        break
