from os import makedirs
from os.path import join
from csv import DictReader, DictWriter
from gender import detect_gender
DATA_DIR = 'tempdata'
CLASSIFIED_DIR = join(DATA_DIR, 'classified')
makedirs(CLASSIFIED_DIR, exist_ok=True)
DATA_FILE_BASENAMES = ['2014-university-system.csv', '2014-community-colleges.csv']

# let's create a extract_usable_name function:
def extract_usable_name(namestr):
    nameparts = namestr.split(', ', 1)
    for nx in nameparts[-1].split(' '):
        if '.' not in nx:
            return nx  # returns the first thing that has no period
    # if we get to this point...then...just return nothing...
    return ""



for fname in DATA_FILE_BASENAMES:
    full_filename = join(DATA_DIR, fname)


    # open the salary data
    xf = open(full_filename, 'r')
    salary_rows = list(DictReader(xf))
    xf.close()

    # pick off the headers from any of the data rows
    # and add the headers ['gender', 'ratio']
    classified_headers = list(salary_rows[0].keys()) + ['gender', 'ratio', 'usable_name']
    # start the classified data file
    classified_filename = join(CLASSIFIED_DIR, fname)
    print("About to classify", len(salary_rows), 'rows into the file:', classified_filename)

    outfile = open(classified_filename, 'w')
    output_csv = DictWriter(outfile, fieldnames=classified_headers)
    output_csv.writeheader()



    # now, iterate through each salary row and attempt to detect gender
    xc = 0
    for row in salary_rows:
        xc += 1
        employee_name = row['Employee Name']
        print("On row", xc, employee_name)
        # skip rows in which row['Employee Name'] is "Not provided"
        if "Not provided" in employee_name:
            pass
        else:
            usablename = extract_usable_name(employee_name)
            xresult = detect_gender(usablename)
            row['gender'] = xresult['gender']
            row['ratio'] = xresult['ratio']
            row['usable_name'] = usablename
            # write to the csv file
            output_csv.writerow(row)

    outfile.close()
