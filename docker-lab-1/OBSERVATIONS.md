# OBSERVATIONS.md — Docker Lab 1
**Name:** Selin Türkdoğan | **ID:** 2103060004 | **Image:** python:3.12-slim

## 1. Image Size
The image size is 179MB. I think it is quite small for a full Python 
environment. This is because the "slim" version is used — it does not 
include extra tools or documentation that we would not need anyway.

## 2. Layers
I counted 9 layers in total. The biggest one was 87.4MB and it was the 
Debian base system. After that, the Python installation layer was 41.4MB. 
The rest of the layers were tiny — they just set some environment variables 
like the Python version or language settings.

## 3. OS and Architecture
OS: linux  
Architecture: amd64

## 4. Python-Specific: import requests Error
When I tried to run `import requests` I got this error:
ModuleNotFoundError: No module named 'requests'

At first I was confused because I use requests all the time on my own 
computer. But then I understood — the container is completely separate from 
my machine. It only has Python's built-in modules. If I want requests 
inside Docker, I would have to install it manually with pip or write a 
Dockerfile.

## 5. What Surprised Me Most
Honestly what surprised me most was that when I ran the container without 
a command it just closed immediately. I expected it to stay open or do 
something. Also I did not expect that a package I always have on my computer 
simply would not exist inside the container — it really showed me how 
isolated containers actually are.