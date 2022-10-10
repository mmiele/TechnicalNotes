---
author: michael
last update: 10/09/2022
---

# Python cheatsheet  

- [Basic file operations](#basic-file-operations)
  - [Read an existing file](#read-an-existing-file)
  - [Create a new file and overwrite existing content](#create-a-new-file-and-overwrite-existing-content)
  - [Append text to an existing file without overwriting](#append-text-to-an-existing-file-without-overwriting)
  - [Both append and read a file](#both-append-and-read-a-file)
- [References](#references)

## Basic file operations

### Read an existing file

```python
with open("file.txt") as file:
    content = file.read()
```

### Create a new file and overwrite existing content

```python
with open("file.txt", "w") as file:
    content = file.write("Sample text")
```

### Append text to an existing file without overwriting

```python
with open("file.txt", "a") as file:
    content = file.write("More sample text")
```

### Both append and read a file

```python 
with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()
```


## References
- [Practical python projects](https://practicalpython.yasoob.me/toc.html)
