## Questions...

"""
1. What advantages do Excel spreadsheets have over CSV spreadsheets?
2.What do you pass to csv.reader() and csv.writer() to create reader and writer objects?
3. What modes do File objects for reader and writer objects need to be opened in?
4. What method takes a list argument and writes it to a CSV file?
5. What do the keyword arguments delimiter and line terminator do?
6. What function takes a string of JSON data and returns a Python data structure?
7. What function takes a Python data structure and returns a string of JSON data?
"""

## Answers..

"""
1. Excel spreadsheets have more formatting options and support for formulas and charts, 
while CSV spreadsheets are simpler and more portable.

-------------------------------------------------------------------------------------------

2. To create reader and writer objects, you pass a File object containing CSV data to 
csv.reader() and csv.writer() functions, respectively.

-------------------------------------------------------------------------------------------

3. File objects for reader and writer objects need to be opened in 'r' (read) and 'w' 
(write) modes, respectively.

-------------------------------------------------------------------------------------------

4. The writerow() method takes a list argument and writes it to a CSV file.

-------------------------------------------------------------------------------------------

5. The delimiter keyword argument specifies the character used to separate fields in a 
CSV file (default is comma), while the lineterminator keyword argument specifies the 
character used to end each line in a CSV file (default is '\r\n').

-------------------------------------------------------------------------------------------

6. The json.loads() function takes a string of JSON data and returns a Python data structure.

-------------------------------------------------------------------------------------------

7. The json.dumps() function takes a Python data structure and returns a string of JSON data.

-------------------------------------------------------------------------------------------


"""