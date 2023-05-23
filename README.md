# Crediting
If you use this repository in one of your other projects, please link back to this repository and give credit with my username.

If you use this code to help create graphics for a social media post, a link in the comments of the post to this github repo would be much appreciated. No need to @ as my social media presence is barren.

I don't ask for much more than that.

# Features
This is a repo designed to gather jury rank data from the official Eurovision website for 2023 (see below for expansion plans) and then convert it into a .csv.
If this is all you want, just run `py juryFullRank.py` or `python3 juryFullRank.py`. The output will be juryRank.csv. The rows of this file are the qualifying countries that can receive jury votes,
and the columns are every country's jury ranks. Since a country cannot vote for itself, there are 0 ranks for that country (e.g. Sweden gives Sweden a 0 rank). 
This is done to preserve the integer formatting of the file and makes it easier to use in other files in this repo.
You can change the name of the output file on the last line (line 71) of "juryFullRank.csv" to be whatever you want, as long as it ends with .csv.

Built using Selenium, pandas, and numpy, written in Python. You cannot run "juryFullRank.py" without at least having Selenium and pandas installed.

## Number of First/Last ranks
If you want to see which country got a first or last place from every country jury or how many times a country got first or last by a country jury, 
running `py juryFirstLast.py` after you have run `py juryFullRank.py` will produce a 2 .csv files. One is titled "juryFirstLast.csv", which shows what each country's jury put for first and last place.
The other is titled "juryCount.csv", which shows the number of times each country got a first place or last place from the jury. Again, these are editable output names, just change line 43 or 44 respectively.

If you have changed the .csv file name in "juryFullRank.py", you must change line 7 to be the same name in order to have the import work.

## More granular data analysis
"juryDataAnalysis.py" is currently in the development process. The goal is to have histograms for every country, with bucket edges being ranks 1-5, 6-10, 11-15, 16-20, and 21-26. 

Average ranks for each country and total sum of ranks (where lower is better) can already be handled by Excel or any other spreadsheet program and simply clicking the row of each country.
These are not priority features since it is easy to manipulate the data in that way. Histograms *do* exist in Excel, but the specifics of having those buckets do *not* easily exist, so I need to make them myself.

# Future Plans
Eventually, I want two things:
1. A Main program that handles everything and you tell it what files to generate.

   Say you only wanted the histogram charts. Currently, that is not possible because the whole DataFrame has to be exported into a .csv file before being imported again into a different file.  
   However, if it were being run in one single program, the DataFrame (or any object for that matter) merely needs to be output within the program before being transferred over into the next function. This is good because:  
   + Everyone who wants to use this program has to only run one file, not (at least) two.
   + Does not waste space generating useless files  
   
   This makes the program easier to use, which makes everyone happier, so you can get your data on faster.
2. Generalization for *every* year of Eurovision

   Currently, this program only works for the 2023 Eurovision year. I also have statically defined which countries qualified and which countries participated in the contest for this year alone.
     
   The problem is that Eurovision does not feature the same cast of countries, nor the same amount of countries, year over year (2024 already has one new country not seen in the 2023 contest, Luxembourg). 
   This means that the current solution of defining every country's participation/qualification manually is unworkable long term. Dynamically defining qualified and participating country arrays will be very useful. 
   It also opens the possibility for further data analysis, like average jury rank of a country across a certain time span, or how one country's jury ranks the Big 5 on average, over a certain time span.
   
Combine these two together, and there exists a robust program that gives massive amounts of jury rank data. Televote scores can also be added, as it wouldn't be too hard, but I am reluctant to do it right now
because televote scores seem to have a lot more to do with the song quality/performance vs the country the song comes from. (Yes, I did just fire shots at juries being incredibly biased for political reasons. Come at me EBU)
