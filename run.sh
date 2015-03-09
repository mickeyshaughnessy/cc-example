#!/usr/bin/env bash

# first I'll load all my dependencies
#apt-get install python-pandas
sudo pip install mrjob
sudo apt-get install mrjob

# next I'll make sure that all my programs (written in Python in this example) have the proper permissions
chmod a+x my_word_count.py
chmod a+x my_running_median.py

# finally I'll execute my programs, with the input directory wc_input and output the files in the directory wc_output
python my_running_median.py med_result.txt wc_input/*
python my_word_count.py --output-dir wc_output/ wc_input/*
sed 's/"//g' wc_output/part-00000 > wc_output/wc_result.txt
rm wc_output/part-00000
### if multiple part* files are being produced, use this syntax instead of the line above:
#--------------------
# sed 's/"//g' wc_output/part-00000 > wc_output/wc_result.txt   # use the first to make the wc_result.txt file
# rm wc_output/part-00000
# FILES= wc_output/part*
# for f in $FILES
# do
#  echo "Processing $f file..."
#  sed 's/"//g' $f >> wc_output/wc_result.txt   # use the first to make the wc_result.txt file
#-----------------------------------------------



