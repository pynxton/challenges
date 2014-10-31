Description
================

Working through the Bioinformatics Algorithms course on Coursera, one of their optional assignments 
seems like it would be an interesting short challenge for people not doing the course.

We are interested in strings that are 'k' long, that occur at least 't' times in any 
section of the data that's 'L' long.

So, for example, in the following data:

    CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA

If k = 5, L = 50 and t = 4, we want a list of the strings that are exactly 5 characters long, 
that occur >= 4 times in any 50 character slice of the data.

The output for that test data would be: CGACA GAAGA

Their suggested algorithm is to iterate over each set of L characters and loop again, counting the 
occurrences of each string. With a small string it's easy to make it quick, but the course then
asks us to use the data from here:

https://stepic.org/media/attachments/lessons/4/E-coli.txt

with:k = 9, L = 500, t = 3 


FAQs
=====

#. What happens when patterns overlap? For example, imagine you are scanning through 'GAGAG' and looking for 
   'GAG': does this k-mer occur once or twice?
   
   It occurs twice, according to the description in the course. 

Solution: 
=============
1904 distinct kmers
