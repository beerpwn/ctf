# WRITEUP BABYCSP

## Author: p4w @beerpwn team

![Image desc](./description.png)

As the descrption/title say we will probably need to bypass CSP to trigger some XSS.
Sufing to the index page we have this:
![Image desc](./index.png)

## Understanding the CSP
The directive ``````
So the CSP permit to use the script that are coming from *google.com
