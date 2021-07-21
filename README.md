# kittyMake
A simple buildSystem written in python

## Requirements:
- Python 3.8 or higher

## How to use:
- Make a new file named `kittymake.kme` (yes it should have THIS name only!)
- Write your commands
- While writing comments make sure they are like:
<br>This</br>
```
//comment
command to execute
```
<br> And NOT like this</br>
```
command to execute //comment
```
This will lead to errors!</br>
### Example usage:
- File kittymake.kme:
```
//this is a comment
//makes a directory called pussycat
mkdir pussycat
//makes the directory 'test' current
cd test
//executes a command(can be replaced with any command because it's just shell commands duh!)
python hello.py
```
- Then run the kittymake file with 
```
python kittymake.py
```
Assuming you have kittymake.py in the same directory as kittymake.kme file of course
