





# The scripts


## fetch_gender_data.py

Downloads the latest batch of baby name data from the Social Security Administration and dumps it into the `tempdata/babynames` folder

## wrangle_gender_data.py

Reads a few files from `tempdata/babynames` and creates a new data file in `babynames/wrangledbabynames.json`, which is used by `gender.detect_gender()` to classify the gender of a name.

## fetch_salary_data.py

Downloads two data files TK

## classify_salary_data.py

Reads through the two salary files and appends new columns to them


## analyze.py



