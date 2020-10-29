# Difficulty - Low

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/Weak%20Session/Sources/low.php)

This time we need a proxy like Burp.

We intercept the generate requests:

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/Weak%20Session/Pictures/1.png)

`dvwaSession` seems to be just integer numbers sorted (1, 2, 3,...).
Seems easy to guess. Send this to Sequencer to confirm it.


# Difficulty - Medium

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/Weak%20Session/Sources/medium.php)

After a few requests, `dvwaSession` looks like this:

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/Weak%20Session/Pictures/2.png)

`dvwaSession` is a sequence like:
1604525560, 1604525563, 1604525567, 1604525573, 1604525577, 1604525580, 1604525656...

This token seems to increase randomly.

In fact, those are the time that requests have been made.

This token should be easy to guess.

# Difficulty - High


[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/Weak%20Session/Sources/high.php)


`dvwaSession` is a sequence like:

c4ca4238a0b923820dcc509a6f75849b, c81e728d9d4c2f636f067f89cc14862c, eccbc87e4b5ce2fe28308fd9f2a7baf3...

Those seems like hashes so I googled them.
Using [this site](md5.gromweb.com) I found that:

c4ca4238a0b923820dcc509a6f75849b = 1

c81e728d9d4c2f636f067f89cc14862c = 2

eccbc87e4b5ce2fe28308fd9f2a7baf3 = 3


![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/Weak%20Session/Pictures/3.png)


So the token is just md5(1), md5(2), md5(3), ....
This should be easy to guess.

# Difficulty - Impossible

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/Weak%20Session/Sources/impossible.php)
