Experimenting with python and Google/Github/pastebin 'dorks'

Goals:

- Automatically identify information such as api keys, login credentials,
other stuff that accidently gets put into code segments pasted to the internet.

- Attempt to contact person involved and get them to fix it (Github)

- Expand to encompass some sort of plugin / new dork you can add that
enables to check for something new over the different scopes of searches.

- Use python class / recommended program structure in order to improve one's
own knowledge of python

- Each dork is initialized with an array of strings and they inherit on 
the  base dork class, which will provide specific methods we might
need and necessary overrides so it is easy to add a new dork.

- A source can then operate on either a generic method that will perform
 the correct searching for the dorks regardless of which specific class
 they are, or each implement a seperate method for the searching.

 - We can combine two things into one so each can be added easily and they
 all work with each other.

 - Each source will have a google specific url for scrapeing and also
 a site url that uses their internal search system.