---
layout: default
title: "Twin Peaks"
permalink: /twinpeaks
---

# Twin peaks
Define lpf(x) = the lowest prime factor of x.

Two integers *x* and *y* (both at least 2) are called "twin peaks" if they satisfy the following conditions:
- x<y
- lpf(x) = lpf(y)
- For all *z*, we have *x<z<y* implies lpf(z) < lpf(x).

If we drew the graph of y=lpf(x), it would look like this:

(pic)

There are many peaks and troughs, of many different heights. A twin peak can be defined as two "peaks" of *equal* height, with no higher peak between them.

The question is, are there any twin peaks?

After thinking for a bit, it might seem unlikely that they exist. The case lpf(x)=2 doesn't work, since there is always an odd number between any pair of even numbers, and that odd number will have an lpf of at least 3. The case lpf(x)=3 also doesn't work, because although one of the two in-between numbers would have an lpf of 2, the other one would be forced to have an lpf of more than 3.

However, there's a big problem. If p is anything other than 2, then the case lpf(x)=p poses an issue. Since x and y are divisible by p, then so is y-x, the distance between the peaks. But if y-x is odd, then one of x or y must be even, and thus would have an lpf of 2! So y-x must be an *even* multiple of p, not just any multiple of p. This makes our task much harder.

- If p=5, then there will be at least 9 integers between x and y. At most 5 of them could be even, leaving 4, and at most 2 out of those 4 could be divisible by p=3, which still leaves 2 integers unaccounted for that must have an lpf of >5.
- If p=7, then there will be at least 13 integers between x and y. At most 7 of them could be even, leaving 6, then at most 2 out of those 6 could be divisible by p=3, which leaves 4, and at most 2 out of those 4 could be divisible by p=5, which still leaves 2 integers unaccounted for that must have an lpf of >7.

Now, our task is seemingly impossible. But the perhaps surprising answer is that twin peaks do exist, and there are infinitely many of them! The *smallest* known one is as follows:
- p = 73
- x = 2061519317176132799110061
- y = 2061519317176132799110207 = x + 2p

Those numbers are 25 digits long. This is a great example that shows how the smallest counterexample to a proposition can sometimes be very large!

[Wolfram MathWorld](https://mathworld.wolfram.com/TwinPeaks.html) gives x=126972592296404970720882679404584182254788131 and p=113 as the first known example of a twin peak, which was discovered around 1997 by John H. Conway, Johan de Jong, Derek Smith, and Manjul Bhargava.

It is worth mentioning that if x and y form a twin peak for some prime p, then so will x+p# and y+p#, where p# is the primorial of p. So if you can determine just one twin peak, you immediately can generate infinitely many, just by adding multiples of p#. 

It has been shown by brute force that there are no solutions for p=2 up to p=67. The smallest p that works is p=71, which has the smallest solution x=7310131732015251470110369, only about 3.5x larger than the one for 73. This settles the question of minimizing p.

However, the question for minimizing x and y is far more complicated. We don't know for sure if the aforementioned twin peak for p=73 is actually the smallest one, over all possible p. It's possible that there's a larger p that produces a smaller twin peak, although that p would have to be at least 97. The amount of p-twin peaks grows very quickly as p increases. There are 240 "distinct" twin peaks for p=71 (not including ones that are a multiple of 71# plus another peak), 40296 for p=73, 164440 for p=79, and 6625240 for p=83. And there's no easy way to figure out the *smallest* of all these, without actually calculating all of them. It's possible that a research effort could brute force up to 2.06\*10^24 to prove that there are no smaller peaks, but even with distributed computing being available, there would need to be some optimizations done to the brute force algorithm to overcome the huge number of integers to check.



# Larger examples

One may define a kp-twin peak as a twin peak using some prime p, where the distance between the peaks is kp. So far, we have discussed 2p-twin peaks, but what about 4p, 6p, or higher? On [this page](https://briankehrig.github.io/twinpeaksexamples), I present the first known examples of 6p, 8p, and 10p-twin peaks, along with some small 4p-twin peaks.

Wolfram says that the (at the time) smallest known 4p-twin peak was discovered by Wilson, with p=1327. On the above page, I present 4p-twin peaks with p=1093, 1039, and 983. On [this page](https://briankehrig.github.io/twinpeaksfinding), I discuss my method to find these examples. I also give heuristics and estimates for what the *smallest* value of p is that admits a 4p-twin peak.

## Exotic examples

A "nested twin peak" exists, if some x,y form a twin peak that is entirely contained inside another peak, z,w. Although this sounds crazy, this is actually fairly easy to compute. If (x,y) is any 2-71-twin peak, then by the Chinese remainder theorem, there will always exist c such that c\*71# + x-2 is divisible by 73. Then, both (x+c\*71#, y+c\*71#) and (x+c\*71#-2, y+c\*71#+2) are twin peaks, the former for p=71 and the latter for p=73. The smallest example of this is (TODO)

