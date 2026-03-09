# JavaScript vs Python -- Developer Cheat Sheet

A quick reference for developers transitioning from JavaScript to
Python.

------------------------------------------------------------------------

## Variables

### JavaScript

``` javascript
let name = "Yash";
const age = 31;
```

### Python

``` python
name = "Yash"
age = 31
```

------------------------------------------------------------------------

## Data Types

  Concept   JavaScript   Python
  --------- ------------ -----------
  Number    `10`         `10`
  String    `"Hello"`    `"Hello"`
  Boolean   `true`       `True`
  Array     `[]`         `list []`
  Object    `{}`         `dict {}`
  Null      `null`       `None`

------------------------------------------------------------------------

## Arrays vs Lists

### JavaScript

``` javascript
let arr = [1,2,3];
arr.push(4);
```

### Python

``` python
arr = [1,2,3]
arr.append(4)
```

  Operation   JavaScript     Python
  ----------- -------------- ------------
  Add         `push()`       `append()`
  Remove      `pop()`        `pop()`
  Length      `arr.length`   `len(arr)`

------------------------------------------------------------------------

## Objects vs Dictionaries

### JavaScript

``` javascript
let user = {
  name: "Yash",
  age: 31
};
```

### Python

``` python
user = {
 "name": "Yash",
 "age": 31
}
```

Access:

``` javascript
user.name
```

``` python
user["name"]
```

------------------------------------------------------------------------

## If Condition

### JavaScript

``` javascript
if(age > 18){
 console.log("Adult");
}
```

### Python

``` python
if age > 18:
    print("Adult")
```

Python uses indentation instead of braces.

------------------------------------------------------------------------

## Loops

### JavaScript

``` javascript
for(let i=0;i<5;i++){
 console.log(i)
}
```

### Python

``` python
for i in range(5):
    print(i)
```

Loop through list:

``` javascript
arr.forEach(item=>{
 console.log(item)
})
```

``` python
for item in arr:
    print(item)
```

------------------------------------------------------------------------

## Functions

### JavaScript

``` javascript
function add(a,b){
 return a+b;
}
```

### Python

``` python
def add(a,b):
    return a+b
```

------------------------------------------------------------------------

## Arrow Function vs Lambda

### JavaScript

``` javascript
const add = (a,b)=> a+b;
```

### Python

``` python
add = lambda a,b: a+b
```

------------------------------------------------------------------------

## Classes (OOP)

### JavaScript

``` javascript
class User{
 constructor(name){
  this.name = name
 }
}
```

### Python

``` python
class User:
    def __init__(self,name):
        self.name = name
```

------------------------------------------------------------------------

## Async Programming

### JavaScript

``` javascript
async function fetchData(){
 const res = await fetch(url)
}
```

### Python

``` python
async def fetch_data():
    res = await api_call()
```

------------------------------------------------------------------------

## Import Modules

### JavaScript

``` javascript
import axios from "axios"
```

### Python

``` python
import requests
```

------------------------------------------------------------------------

## Error Handling

### JavaScript

``` javascript
try{
 risky()
}catch(err){
 console.log(err)
}
```

### Python

``` python
try:
    risky()
except Exception as e:
    print(e)
```

------------------------------------------------------------------------

## List Comprehension (Python Feature)

``` python
nums = [x*x for x in range(5)]
```

Equivalent JavaScript:

``` javascript
let nums = Array.from({length:5}, (_,i)=> i*i)
```

------------------------------------------------------------------------

## Truthy / Falsy

### JavaScript Falsy

-   false
-   0
-   ""
-   null
-   undefined

### Python Falsy

-   False
-   0
-   ""
-   None
-   \[\]
-   {}

------------------------------------------------------------------------

## Console Output

### JavaScript

``` javascript
console.log("Hello")
```

### Python

``` python
print("Hello")
```

------------------------------------------------------------------------

## Quick Mental Mapping

  JavaScript    Python
  ------------- ------------
  Array         List
  Object        Dictionary
  console.log   print
  function      def
  null          None
  push          append
  length        len

------------------------------------------------------------------------

**Tip for JS Developers:**\
After Python basics and OOP, explore AI, automation, and data
engineering.
