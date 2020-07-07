---  
layout:  post 
title:  "The everyday joy of testing" 
---

I coded a lot before I ever wrote an automated test for my code, and, had I not been forced to start testing (by attending a software development course that enforced code testing at every level) I may *never* have written any tests for my code and would not have known how much clarity, reliability and peace of mind I was missing. I can say that testing is one of the joys in development that I look forward to because I've experienced the hell that occurs if you *don't* test and I don't want to return to that.

## Before testing

All that "code" that I wrote before starting to test was a complete mess because it was almost impossible to debug effectively, find errors and sometimes to even know if errors had occurred. My feedback loop for finding errors in my code was something like this:

- Change the input values for my code manually
- Put a print statement somewhere in my code to get visibility on an output
- Run the entire program
- See if the output matches my expectation

This was a really terrible process for a number of reasons:

- It was really slow, *especially* if I needed to test multiple inputs to my code, I had to type them in manually and run the code each time
- It was susceptible to human error as often I would think the output of my code was correct when it was actually incorrect only to find out later my whole expectation what parts of my code did and did not work was wrong
- It littered the code with hundreds of print statements that were difficult and laborious to remove, especially if you needed to retest something later down the line you could either leave the print statement littering your code or re-add every time you wanted to test
- It gave no feedback on refactoring, when I refactored one part of my code that broke another part of my code, if I wasn't specifically thinking about testing that part of the code I would have no idea it was broken
- It often tested implementation and not behaviour. Frequently because there were no clearly defined end points for tests, only print statements in the production code I would find myself testing that a loop had run or that a particular variable had been initialised even if it was entirely irrelevant to the rest of my code base.

Futhermore, a lack of a test suite meant that I was constantly stressed out when writing larger code projects because I was never really sure if my code would break and if it did break where the error had occured or how I code even fix it.

## After testing

I noticed the difference that automated testing made to my development process almost immediately. Suddenly I didn't have to be constantly writing print statements into my code and running the code individually every time I could get a sense of whether my code was doing what it was supposed to do by running a single command and checking the output.

Another immediate effect of testing was that refactoring or extending my code became a lot less stressful. Before I started writing tests for my code I would dread having to refactor or extend my code because I had no reliable way of knowing whether the changes I made to my code would break it unexpected ways. One of joys of testing is that you can ensure that changes to your code actually work by simply running your test suite. The peace of mind this affords you cannot be understated.

## After after testing
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MTM2NjU4MzUsMjA1NDEwNDgxNCwzND
A5ODcyNCwyMjgyMjI5NTksMTgzMTUwNzgyNSwtMTU5NjU0NDkx
XX0=
-->