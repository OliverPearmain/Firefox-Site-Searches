import lz4.block as lb

infile = '/Users/44134341/Library/Application Support/Firefox/Profiles/0i8jdlc8.default/search.json.mozlz4.decompressed'
outfile = '/Users/44134341/Library/Application Support/Firefox/Profiles/0i8jdlc8.default/search.json.mozlz4'

inf = open(infile, 'rb')
data = lb.compress(inf.read())
data = b'mozLz40\0' + data
outf = open(outfile, 'wb')
outf.write(data)
