text = open("Voting.html",'r').read()

text.replace ( "\n\r", "\n" )
text.replace ( "\r\n", "\n" )
text.replace ( "\r", "\n" )

open("Voting.html",'w').write ( text )

