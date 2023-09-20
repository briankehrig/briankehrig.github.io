---
layout: default
title: "Primes in Centuries"
permalink: /primecenturies
---

# Twin peaks
Prime numbers decrease in density as you go along the number line. There are 25 prime numbers below 100, and 21 of them between 100 and 200. However, the third century 200-300 only has 16 primes. From there, the numbers continue to fall:
```
0-100: 25 primes
100-200: 21 primes
200-300: 16 primes
300-400: 16 primes
400-500: 17 primes
500-600: 14 primes
600-700: 16 primes
700-800: 14 primes
800-900: 15 primes
900-1000: 14 primes
1000-1100: 16 primes
1100-1200: 12 primes
1200-1300: 15 primes
1300-1400: 11 primes
1400-1500: 17 primes
1500-1600: 12 primes
1600-1700: 15 primes
1700-1800: 12 primes
1800-1900: 12 primes
1900-2000: 13 primes
2000-2100: 14 primes
2100-2200: 10 primes
2200-2300: 15 primes
2300-2400: 15 primes
2400-2500: 10 primes
2500-2600: 11 primes
2600-2700: 15 primes
2700-2800: 14 primes
2800-2900: 12 primes
2900-3000: 11 primes
```
(TODO: ADD GRAPH)

If you continue checking centuries and calculate how many primes they contain, you might notice that other than the first two, there doesn't appear to be any centuries that have any more than 17 primes. It doesn't *always* decrease, there are some jumps up and down. There are 11 primes between 1300 and 1400, but the next century has a whopping 17 primes! However, you could check the centuries up to 1,000,000,000,000, and not find a single one with more than 17 primes. So is that the limit?

Well, it turns out that it's not. The first century greater than 200 that contains at least 18 primes is: 122853771370900-122853771371000. Is there a reason why the smallest such century is so large?

Here is a list of all centuries below 2e17 that contain 18 primes:
```
122853771370900-122853771371000 (primes ending with 01,03,07,19,21,27,31,33,37,49,51,61,69,73,87,91,97,99)
2335286971401800-2335286971401900 (primes ending with 03,09,21,23,27,29,41,47,51,59,63,69,71,77,83,87,89,99)
2870323747426600-2870323747426700 (primes ending with 01,07,09,13,21,27,33,43,51,57,61,69,73,79,87,91,93,99)
14478586548170200-14478586548170300 (primes ending with 03,09,19,21,31,37,43,49,57,63,67,73,79,81,87,91,93,99)
16139492396644900-16139492396645000 (primes ending with 01,07,09,13,19,21,31,33,37,43,51,61,63,73,79,93,97,99)
16897570820963800-16897570820963900 (primes ending with 01,03,09,21,27,39,43,49,57,63,67,73,79,81,87,91,93,97)
17474880906689800-17474880906689900 (primes ending with 03,09,19,21,27,31,37,39,49,51,61,67,73,79,87,91,93,97)
20755224123135700-20755224123135800 (primes ending with 03,07,09,13,21,27,37,39,51,63,67,69,73,79,81,87,91,97)
27821517920553100-27821517920553200 (primes ending with 01,03,07,09,21,27,31,43,51,57,63,67,69,73,87,91,93,97)
31230332890972000-31230332890972100 (primes ending with 01,03,09,13,21,27,31,43,51,57,63,69,73,79,87,91,97,99)
59224898214387700-59224898214387800 (primes ending with 01,07,09,13,21,39,43,49,57,61,67,69,79,81,91,93,97,99)
81293988663453100-81293988663453200 (primes ending with 01,03,07,09,19,21,27,31,43,57,61,69,79,87,91,93,97,99)
93910078275201400-93910078275201500 (primes ending with 01,03,07,13,21,27,37,39,49,51,57,67,69,73,79,81,93,99)
98393029020902100-98393029020902200 (primes ending with 07,11,13,17,23,29,31,41,53,59,67,71,73,77,79,83,91,97)
111116149454427400-111116149454427500 (primes ending with 07,09,19,21,27,31,37,43,49,51,57,61,63,79,87,93,97,99)
140326343186616700-140326343186616800 (primes ending with 01,03,07,09,21,31,33,39,49,51,61,67,79,81,87,91,93,99)
147354751226571100-147354751226571200 (primes ending with 03,07,13,21,27,31,37,39,49,51,57,67,69,73,79,91,97,99)
176977548659322400-176977548659322500 (primes ending with 01,03,09,13,19,21,27,31,43,49,51,57,61,69,79,91,93,97)
193408516559355100-193408516559355200 (primes ending with 01,03,07,13,21,27,31,33,51,57,61,69,73,79,91,93,97,99)
```

There is one 15-digit century in the above list, but there are two with 16 digits, 11 with 17 digits, and an unknown number with 18 digits. This list is in the OEIS, as sequence [A361723](https://oeis.org/A361723).

We can of course go higher than 18 primes in a century. Here are all the centuries with 19 primes below 2e19:
```
1468867005116420800-1468867005116420900 (primes ending with 01,03,07,09,21,31,37,39,43,49,51,63,67,69,73,79,81,87,93)
11398672167696960100-11398672167696960200 (primes ending with 01,03,09,19,21,27,31,37,43,49,51,61,63,69,73,87,91,93,99)
14058990984162782500-14058990984162782600 (primes ending with 01,03,07,09,13,19,21,27,31,43,49,51,57,61,63,69,79,87,91)
15656500547607309400-15656500547607309500 (primes ending with 07,09,19,21,27,31,33,43,49,51,57,61,69,79,87,91,93,97,99)
16637004018292631500-16637004018292631600 (primes ending with 03,07,09,13,21,27,31,37,39,43,49,51,63,69,73,79,81,91,93)
```
(For some reason, OEIS didn't approve these values for a new sequence, even though they accepted the one for 18 primes in a century)

It is very likely that centuries exist with as many as 23 primes. It is known to be impossible to go higher than 23 (excluding the first century). However, there are only expected to be around 2 or 3 "prime-saturated" centuries below 1e34, so it will be very difficult to search for them. I have designed a highly efficient method of searching for large numbers of primes in centuries. I calculated the above lists for 18- and 19-prime centuries in a few days on my laptop GPU.

The algorithm only gets more efficient as the number of primes increases. For example, searching for centuries with 20 primes is estimated to be around 10x as efficient as 19 primes, but it is also expected that 20-prime centuries are 100x rarer than 19-prime centuries around the range when 20 primes start appearing. This means that overall, the search will produce results 10x slower. Similarly, 23 primes would be around 100x more efficient than 22 primes, but they are around 5000x rarer around the magnitude where they are expected to start appearing.

Using my laptop's GPU, it would take around 1.6 million years to exhaustively check for 23-prime centuries up to 1e34. With an RTX 4090 graphics card, that could be cut to around 100,000 years. Theoretically, if all the computing power of [GIMPS](https://mersenne.org) was assigned to this computation, it could possibly be computed in a (somewhat) reasonable amount of time.



# How do I test for primes in centuries?
Each century contains a specific "prime pattern". Let's consider the century 1300-1400, which contains the 11 primes 1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399. The prime pattern for this century is (01,03,07,19,21,27,61,67,73,81,99), consisting of the last two digits of each prime.

Given a specific number of primes in a century, in this case 11, it is possible to enumerate all the possible prime patterns that contain exactly that many primes. For the case of 11 primes, there are a total of 24942742 patterns. The amount of patterns for other prime counts are listed below:
```
Primes  Patterns
0		1
1		40
2		780
3		7528
4		47878
5		225044
6		830270
7		2459376
8		5900602
9		11555200
10		18634704
11		24942742
12		27836859
13		25913910
14		20053913
15		12815608
16		6699888
17		2829786
18		948729
19		245756
20		47150
21		6276
22		518
23		20

```

## Calculating prime patterns

As an example, there are 40 patterns for one prime, because the prime can be any number that ends in a 1,3,7, or 9, and there are 40 such numbers in a century.

How do we use prime patterns to increase our search efficiency? Well, it turns out that it is *very* efficient to search for a *specific* prime pattern, and it gets even more efficient the more primes are in that pattern.

To illustrate this, let's suppose we want to make a program that can efficiently test for prime quadruplets. A prime quadruplet is a sequence of four primes that are as close together as four primes can ever get (excluding very small primes like 2,3,5). The smallest prime quadruplets are (11, 13, 17, 19), (101, 103, 107, 109), (191, 193, 197, 199), and (821, 823, 827, 829). In all of these cases, the difference between the first and last prime in the quadruplet is 8, the smallest value possible. In general, a prime quadruplet must be of the form (n, n+2, n+6, n+8) for some n.

If we want to search for primes n such that (n, n+2, n+6, n+8) are all prime, the obvious place to start is to only consider odd n, since even n will never be prime (again, we can ignore "very small" primes like 2). n cannot be divisible by 3 for the same reason, but n also cannot be 1 more than a multiple of 3, because then n+2 would be divisible by 3. Thus, n *must* be 1 less than a multiple of 3.

What about divisibility by 5? There are 5 possible residues when n is divided by 5, and it turns out that 4 of them cause one of (n, n+2, n+6, n+8) to be divisible by 5, and thus block a prime quadruplet from existing there. The only residue that works is when n is 1 more than a multiple of 5.

Combining our results for divisibility by 2,3,5, we get that n must be congruent to 11 modulo 30. So if we have our program check every 30th number starting from 11, then it would be 30 times faster than checking every number! This is great, but we can do much better by looking at more divisibility rules, starting with 7.

For 7, it turns out that the residues that "work" are 2, 3, and 4 (mod 7). Combining this with our result of n=11 mod 30, we get that n must be congruent to 11, 101, or 191 mod 210. There are only three possibilities mod 210, so now our program is 70x faster than normal!

For 11, there are 7 residues that work. For 13, there are 9 that work, and for 17, there are 13 that work, and so on. In general, if the prime we are looking at is larger than the "diameter" of the tuple (the difference between the largest and smallest number in the tuple, which in this case is 8), then each of the members of the tuple will block exactly one residue from "working". So the number of residues that work for some p>8 is exactly p-4.

So what if we consider all primes up to 30, and make our divisibility rules based on all of them together? What would that look like? We get the following calculation:

```
Number of residues = 1*1*1*3*7*9*13*15*19*25 = 17506125
Modulus = 2*3*5*7*11*13*17*19*23*29 = 6469693230
Proportion of modulos that "work" = 17506125/6469693230 =~ 1/369.5674
```
Our program is now 370 times faster than it started. At this point, we start to see diminishing returns. Adding another prime, 31, will only speed it up by a factor of 31/27 = 1.15x, but now we will need to store 27x as many residues (472 million) instead of just 17.5 million. Memory very quickly becomes the limiting factor.

One small issue is that when we generate the big list of modulos for the first time, it will be in a completely random order. We should sort the list, so that when we iterate over it, we will be guaranteed to find the prime quadruplets in the correct order.
