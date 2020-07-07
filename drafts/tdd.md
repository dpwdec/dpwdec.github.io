---  
layout:  post 
title:  "The everyday joy of automated testing" 
---

I coded a lot before I ever wrote a test for my code, and, had I not been forced to start testing (by attending a software development course that enforced code testing at every level) I may *never* have written any tests for my code and would not have known how much clarity, reliability and peace of mind I was missing. I can say that testing is one of the joys in development that I look forward to because I've experienced the hell that occurs if you *don't* test and I don't want to return to that.

## Before Automated Testing

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

Futhermore, a lack of a test suite meant that I was constantly stressed out wh

<!--stackedit_data:
eyJoaXN0b3J5IjpbNTE0MDY1MTcyXX0=
-->