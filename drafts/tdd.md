---  
layout:  post 
title:  "The everyday joy of testing" 
---

I coded a lot before I ever wrote an automated test for my code, and, had I not been forced to start testing (by attending a software development course that enforced code testing at every level) I may *never* have written any tests for my code and would not have known how much clarity, reliability and peace of mind I was missing. I can honestly say that testing is one of the joys in development that I look forward to because I've experienced the hell that occurs if you *don't* test and I don't want to return to that.

## Before testing

All that code that I wrote before starting to test was a complete mess because it was almost impossible to debug effectively, find errors and sometimes to even know if errors had occurred. My feedback loop for finding errors in my code was something like this:

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

I noticed the difference that automated testing made to my development process almost immediately. After the initial investment of actually learning how to write tests and writing tests the speed at which I could develop and test a large number of input possibilities and edge cases increased by an order of magnitude. I was no longer writing multiple print statements into my code when I encountered bugs as I could just go straight to the source of error, as indicated by my tests. I no longer had to rerun by entire application when I wanted to verify an output but could run different parts of my program in isolation. Furthermore I could be much more certain of the quality of my code, I could be sure that simply did what it was meant to do.

Another immediate effect of testing was that refactoring or extending my code became a lot less stressful. Before I started writing tests for my code I would dread having to refactor or extend my code because I had no reliable way of knowing whether the changes I made to my code would break it unexpected ways. One of joys of testing is that you can ensure that changes to your code actually work by simply running your test suite. The peace of mind this affords you cannot be understated.

Just learning the basics of testing made coding a joy for me and removed a lot of the most stressful and laborious parts of writing software, I often wonder how I ever got much done before learning to test code effectively.

## After after testing

Writing automated tests is just the tip of the iceberg in terms of software testing and as time has passed I have found that testing *isn't* just a convenience for verifying your code's validity, it also leads to better structured application code overall.

One example of this, is the practice of dependency injecting functions or classes in your code with external code dependencies which enforces a transparent indication of the different dependencies that a part of your code has, making them clearer and less prone to untraceable errors due to dependencies failing. This also means you have a clear idea of what the responsibilities of an atomised part of your code has and what it relies on and more naturally allows you to respect single responsibility in your code.

In addition, you can use testing to guide the entire development process with TDD (Test Driven Development) and BDD (Behaviour Driven Development). These software methodologies focus on defining an expected output for a piece of code before doing *any* implementation. The advantage of this is that it forces you to clearly plan how you expect a piece of code to function, what will be its inputs and what will be its outputs before you start actually creating it, it forces you to actually plan your codes structure before you make it. As someone who spent a significant amount of time coding as a hobbyist and would always just jump straight into coding with only vaguest notion of what my code was supposed to do, this practice of explicitly defining in a test what I wanted my code to output was transformative to my productivity leading to much clearer and well defined applications.

Furthermore, the fact that TDD and BDD focus only on verifying the input and output of code means that you are always free to alter your code's implementation as long as it still produces the same output. By avoiding testing the implementation of some code I found I was free to produce creative implementations to solve problems while still maintaining the assurances offered by tests that in the end the code worked as expected.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcwNDMxNzg5OCwyMDU0MTA0ODE0LDM0MD
k4NzI0LDIyODIyMjk1OSwxODMxNTA3ODI1LC0xNTk2NTQ0OTFd
fQ==
-->