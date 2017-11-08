
# I don't know what the fuck the question is asking about
# P.S., notice what the Python s.lstrip(substr) does: it removes any chars in substr from the
#   left end of s; a hidden fact is that it stops removing chars when the first char that doesn't
#   exist in substr appears in s!

class Codec:

    def encode(self, longUrl):

        return longUrl


    def decode(self, shortUrl):

        return shortUrl



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))