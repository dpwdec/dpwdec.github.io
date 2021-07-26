---
title: Power Rule
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

The **power rule** of logarithms states that

\\[ log(a^b) = b \cdot log(a) \\]

## Proof

Given that 

\\[ log_b(a) = x \\]

It follows that

\\[ b^x = a \\]

Next, introduce another exponent \\( c \\) so both sides of this equation.

\\[ (b^x)^c = a^c \\]

\\[ b^{x \cdot c} = a^c \\]

This is essentially saying that if we raise \\( b \\) to \\( x \cdot c \\) we get \\( a^c \\). Another way of saying exactly that is using a \\( log \\) function with base \\( b \\). *This is what log functions tell you by definition!* So,

\\[ log_b(a^c) = x \cdot c \\]

We can now substitute into this equation, replacing \\( x \\) with \\( log_b(a) \\) as we stated above that \\( log_b(a) = x \\).

\\[ log_b(a^c) = log_b(a) \cdot c \\]

Re-arranged to

\\[ log_b(a^c) =  c \cdot log_b(a) \\]

Which proves the *power rule*.

This makes sense intuitively because whenever you take a log of a single value you are raising some base to that value. If you raise that value itself to an exponent that just involves raising the base *again*. And, as we can see from above, doing an exponent of an exponent results in multiplication.

## Supplementary Proof

*This was the previous proof that I had for this that was essentially summarised from a Khan explanation. I've left it in for completeness.*

Given that

\\[ log_x(a) = b \\]

It follows that

\\[ x^b = a \\]

Next we introduce a varaible \\( c \\) and apply it to the first equation above by multiplying both sides

\\[ (*) \ c \cdot log_x(a) = c \cdot b \\]

Then we can introduce \\( c \\) to the second equation by raising both sides to \\( c \\)

\\[ (x^b)^c = a^c \\]

\\[ x^{b \cdot c} = a^c \\]

We can *rewrite* this expression in terms of a logarithm of \\( x \\) - what do we raise \\( x \\) to to equal \\( a^c \\)? Well, its stated write there, as \\( b \cdot c \\\).

\\[ log_x(a^c) = b \cdot c \\]

Above we can see that the \\( (*) \\) star figure shows

\\[ c \cdot log_x(a) = c \cdot b \\]

Therefore we just proved that 

\\[ c \cdot log_x(a) = log_x(a^c) \\]

Because they both equal \\( c \cdot b \\).