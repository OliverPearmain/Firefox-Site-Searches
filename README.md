
# Manually Modifying Firefox Search Sites (mozlz4 format)

Update the hard-coded file paths in `./decompress.py` and `./compress.py` (if necessary)

Run `./bin/decompress` 

Modify the outputted `search.json.mozlz4.decompressed` in your Firefox profile folder

Close Firefox (not certain this is necessary but probably better safe than sorry)

Run `./bin/compress`

Restart Firefox and the changes to search should be loaded



PS credit for the python code here...
https://superuser.com/questions/1269805/how-to-edit-search-engines-in-firefox-quantum
