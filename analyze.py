from os.path import join
from csv import DictReader
CLASSIFIED_DIR = join('tempdata', 'classified')
DATA_FILE_BASENAMES = ['2014-university-system.csv', '2014-community-colleges.csv']


for fname in DATA_FILE_BASENAMES:
    classified_datafile_path = join(CLASSIFIED_DIR, fname)
    print("")
    print("===========================================")
    print("Opening and reading", classified_datafile_path)
    # open and read that CSV into datarows
    datarows = []
    with open(classified_datafile_path) as f:
        # have to manually change each value of 'Total Pay & Benefits' to an integer
        for d in DictReader(f):
            d['Total Pay & Benefits'] = float(d['Total Pay & Benefits'])
            datarows.append(d)


    print("---------------------------------------------")
    print("Total demographics")
    everyone = {'M': 0, 'F': 0, 'NA': 0}
    for d in datarows:
        gd = d['gender']
        everyone[gd] += 1
    print("F:", everyone['F'], "M:", everyone['M'])



    print("---------------------------------------------")
    print("Analyzing leadership demographics")
    leaders = {'M': 0, 'F': 0, 'NA': 0}
    for d in datarows:
        title = d['Job Title'].upper()
        gd = d['gender']
        if 'PRESIDENT' in title or 'DEAN' in title:
            # but NOT an assistant
            if 'ASST' not in title and 'ASSIST' not in title and 'AST' not in title:
                leaders[gd] += 1

    print("F:", leaders['F'], "M:", leaders['M'])



    print("---------------------------------------------")
    print("Analyzing salary demographics")



    # now we can do an analysis:     # Analyze number of people by salary brackets

    # note: I deliberately did not use list comprehensions or anything too fancy below...
    #  so forgive the unpythonic style

    for salaryrange in [(0, 50000), (50001, 85000), (85001, 125000), (125001, 250000), (250000, 10000000)]:
        salmin, salmax = salaryrange
        filteredrows = []
        genderedrows = {'F': [], 'M': [], 'NA': []}
        for d in datarows:
            if d['Total Pay & Benefits'] > salmin and d['Total Pay & Benefits'] <= salmax:
                filteredrows.append(d)
        print("For the salary range of", salmin, 'to', salmax)

        female_rows = []
        for d in filteredrows:
            gd = d['gender']
            genderedrows[gd].append(d)

        print("\tNumber of F:", len(genderedrows['F']))
        print("\tNumber of M:", len(genderedrows['M']))
        print("\tNumber of NA:", len(genderedrows['NA']))

        print("\tF/M ratio:", round(100 * len(genderedrows['F']) / len(genderedrows['M']) ))
