# Difficulty - Low

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/JavaScript/Sources/low.php)


When I sent the `success` message I got the `invalid token` error. 
I looked in browser tools and the request was like that:
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/JavaScript/Pictures/1.png)


I googled what this token is and I found this:
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/JavaScript/Pictures/2.png)


That string is md5('PunatrZr'). PunatrZr is actually rot13('ChangeMe').
So, the message should be success and the token md5(rot13(success))
So:
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/JavaScript/Pictures/3.png)

And this is ok:
![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/JavaScript/Pictures/4.png)


# Difficulty - Medium

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/JavaScript/Sources/medium.php)

To validate the message, token should be like : `XXeMegnahCXX` ("XX" + reverse(success) + "XX").

So, in browser console:

```JS
document.getElementById("phrase").value="success";
do_elsesomething("XX");
````
Submit it and it will work.


# Difficulty - High

[Challange source code](https://github.com/PnzJust/DVWA-v1.10/blob/main/JavaScript/Sources/high.php)

I used [this site](https://lelinhtinh.github.io/de4js/) to deobfuscate the JS.
At the bottom I saw this:

```JS
function do_something(e) {
    for (var t = "", n = e.length - 1; n >= 0; n--) t += e[n];
    return t
}

function token_part_3(t, y = "ZZ") {
    document.getElementById("token").value = sha256(document.getElementById("token").value + y)
}

function token_part_2(e = "YY") {
    document.getElementById("token").value = sha256(e + document.getElementById("token").value)
}

function token_part_1(a, b) {
    document.getElementById("token").value = do_something(document.getElementById("phrase").value)
}
document.getElementById("phrase").value = "";
setTimeout(function () {
    token_part_2("XX")
}, 300);
document.getElementById("send").addEventListener("click", token_part_3);
token_part_1("ABCD", 44);
```

So I wrote this code:
```JS
document.getElementById("phrase").value="success";
token_part_1("ABCD", 44);
token_part_2("XX");
````
Run it in browser console and got the success message.


# Difficulty - Impossible

![...](https://github.com/PnzJust/DVWA-v1.10/blob/main/JavaScript/Pictures/5.png)
