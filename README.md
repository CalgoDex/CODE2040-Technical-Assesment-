# CODE2040-Technical-Assesment-
Challenge for CODE2040 program

Part 1 of the Technical application:

For this part of the assessment I just passed my dictionary of keys token and github into the request module, 
utilizing its post function in the process.

Q1 of the technical application:

This was rather straightforward, as all I did was invert the string using list comprehension and then posted it to the API.

Q2 of the technical application:

For this question, I first acquired the dictionary as a single string, then converted it to a dictionary using the ast module. Afterwards, I just iterated through the haystack, incrementing a counter each time a value in the list did not equal the value of the needle. Once a value in the array equaled the value of the needle, I simply set pos (for position) equal to the counter. This was the value I returned to the API

Q3 of the technical application:

For this question, once I got the dictionary all set up, I simply iterated through “array” and appended all the strings which did not have the prefix as a substring to list I had initiated earlier. I then added this list to a dictionary with an associated key of “array.” For some reason I kept getting a 400 error when I didn’t state json = not_prefix, which I assumed meant that “array,” which was actually a list, within my dictionary could only be interpreted as an array by setting json = not_prefix.

Q4 of the technical application

Thank the lord for Google. I had to look up lots of python documentation for this problem. In the end, I had to first convert to UTC, in which the time zone had the +00:00 suffix, and then substituted that substring for a Z by iterating over the UTC format I got before.

Reflection:

Fun project, never thought I'd be able to do it but I did thanks to some initial help from Frederick Kofi Tam
