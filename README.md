# Gender analysis of Califorinia college payroll


## Preliminary findings

- More women then men overall as employees
- More men then women in high leadership positions (deans and presidents)
- Under $250,000 in salary, women maintain parity/majority with men in salaried jobs
- Above $250,000, women are outnumbered 2 to 1
- Way fewer people in the community colleges system make $250K or above.






# The scripts

TKTK TODOTOD

## fetch_gender_data.py

Downloads the latest batch of baby name data from the Social Security Administration and dumps it into the `tempdata/babynames` folder

## wrangle_gender_data.py

Reads a few files from `tempdata/babynames` and creates a new data file in `babynames/wrangledbabynames.json`, which is used by `gender.detect_gender()` to classify the gender of a name.

## fetch_salary_data.py

Downloads two data files TK

## classify_salary_data.py

Reads through the two salary files and appends new columns to them


## analyze.py



