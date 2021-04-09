This is a CLI tool.  The way to use it is to get an API token from genius api and replace it in the code in line 10.

Once you have your own token you can call it from the command line like this:

python discography.py --count 5 

-- count is an optional flag.  If not specified it defaults to 1 song returned.

The above command prompts you to input an artist.  Once it has the name of the artist you are looking for, it reformats the name if necessary like "The Beatles" from "beatles", gets the number of songs you want from the optional flag --count (in my above example, five songs) and returns five beatles songs. 
