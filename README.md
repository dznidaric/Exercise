
## 1. Anagrams 

### Task
For a given word w and a list of words L, find the number of words in L that are anagrams of w. 

**Input**

List of words L will come in a textual file, one word per line. The program will be called from command line with a filename (to a list of words L) and a word w as arguments.

**Output**

The number of words in L that are anagrams of w.

Example input 1

~/ $ python anagram.py wl50.txt able


Example output 1

2


Example input 2

~/ $ python anagram.py wl50.txt abba


Example output 2

1


Example input 3

~/ $ python anagram.py wl50.txt a 

Example output 3 

0 


File used in example 

~/ $ cat wl50.txt 

aab

bab

aaron

abacus

abandon

abandoned

abandoning

abandonment

abandons

abate

abatement

abba

abbas

abbey

abbot

abbott

abbreviation

abbreviations

abdomen

abdominal

abduct

abducted

abduction

abel

aberdeen

aberration

abiding

abide

abigail

abilities

ability

able

abner

abnormalities

abnormally

aboard

abode

abolish

abolishing

abolition

abolitionist

abolitionists

abominable

abomination

aboriginal

abort

abortion

abortionists

abortions

abound



## 2. Mountain stream

### Task

You are given an infinite stream of points in the Cartesian coordinate system. At every moment, we can do 3 operations:

1. We can input another point by specifying its coordinates
2. We can query the program to give us C points closest to the origin of the coordinate system (point (0, 0))
3. We can terminate the program

**Input**

First line has an integer C which specifies the number of points closest to the origin that we need to print.

After that, we have a potentially infinite stream of 3 possible input lines:

* 1 X Y - adds the point (X, Y) to the stream.
* 2 - query the program for C closest points
* 3 - terminates the program

C, X and Y are all integers with the following constraints:

* C ∈ [1, 106]
* X, Y ∈ [-1000, 1000]


**Output**
For each query, print out the list containing C points closest to the origin in any ordering. Print each point on their own line as one space-separated pair of integers.

Example input

3

1

1 1

1

2 5

1

3 3

1

8 9

1

20 2

1

-5 3

2

1

0 -1

1

-2 0

2

2

1

0 0

1

1 1

2

3


Example output

1 1

3 3

2 5

0 -1

1 1

-2 0

0 -1

1 1

-2 0

0 0

0 -1

1 1

## 3. Getting them CMEs

### Task

Dr. House needs to collect a certain amount of CME credits per year in order to extend his
Medical licence. He has realised that VuMedi is a great platform that provides CME certification.
After watching a webinar and completing the post quiz, he is rewarded a given number of CME
credits. However, Dr. House has limited time to collect the CMEs and he needs to optimize it in
order to get the maximum number of credits.


**Input**

First line has integer T, the time available to do the certification. Next line provides number N,
the number of webinars that are available on VuMedi platform to get CME credits for. The
following line contains N integers that represent the time needed to certify for a given webinar
and the last line of input represents the number of CME credits awarded for each.


**Output**

First line should output the maximum number of CME credits Dr. House can obtain in time T.
Each next line outputs a webinar duration with the corresponding number of CMEs that Dr.
House has decided to obtain.


Example input

7

4

2 3 4 5

3 4 5 5


Example output
9

3 4

4 5
