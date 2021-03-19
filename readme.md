# mixing_secrets 

A forked + updated repo of [MIXING SECRETS: A MULTI-TRACK DATASET FOR INSTRUMENT RECOGNITION IN POLYPHONIC MUSIC](https://musicinformatics.gatech.edu/wp-content_nondefault/uploads/2017/10/Gururani_Lerch_2017_Mixing-Secrets.pdf)
by Siddharth Gururani and Alexander Lerch, ISMIR2017 late-breaking/demo.


## What to do?

- I saved the page source on 2021-03-17.
- `$ python filter_out_zip_urls.py` to get `zip_urls.txt`
- I downloaded all the zip files `$ wget -i zip_urls.txt`
- Then, I ran this script to get `zip_contests.txt`  
```
for f in *.zip; do
  echo "Filename:$f" >> zip_contents.txt
  zip -sf $f  >> zip_contents.txt
done 
```
- `$ python select_vocal_files.py` to get the file paths of vocal stems
- Then I inspected the resulting files.
  - `filenames_non_vocal_songs.json` to make sure if i'm not missing anything.
  - `filenames_vocal.json` to make sure i selected vocals only.