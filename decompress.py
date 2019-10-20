import lz4.block as lb
import json

infile = '/Users/44134341/Library/Application Support/Firefox/Profiles/0i8jdlc8.default/search.json.mozlz4'
outfile = '/Users/44134341/Library/Application Support/Firefox/Profiles/0i8jdlc8.default/search.json.mozlz4.decompressed'

inf = open(infile, 'rb')
inf.read(8)
data = lb.decompress(inf.read())
parsed_json = json.loads(data)
pretty_data = json.dumps(parsed_json, indent=4, sort_keys=True)
print(pretty_data)
outf = open(outfile, 'w')
outf.write(pretty_data)