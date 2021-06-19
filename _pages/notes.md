---
layout: page
title: 📂
---
<style>
    ul {
        list-style: none;
        padding: 0;
        margin-bottom: 2px;
        margin-top: 0px;
    }

    label {
        cursor: pointer;
        border-bottom: none;
        font-weight: 450
    }

    input[type="checkbox"] {
        position: absolute;
        left: -9999px;
    }

    input[type="checkbox"]~ul {
        height: 0;
        transform: scaleY(0);
    }

    input[type="checkbox"]:checked~ul {
        height: 100%;
        transform-origin: top;
        transition: transform .2s ease-out;
        transform: scaleY(1);
    }

    /* turns the check into a closed folder by target labels AFTER an input */
    input+label:before {
        content: "📁";
        margin-right: 10px;
    }

    /* toggles to open folder on label when checked */
    input[type="checkbox"]:checked~label:before {
        content: "📂";
        margin-right: 10px;
    }
</style>
<ul>
    <div name="contents-index">

        <l>
            <input type="checkbox" id="Math" checked>
            <label for="Math">Math</label>
            <ul>
                <l>
                    <input type="checkbox" id="Exponentials">
                    <label for="Exponentials">Exponentials</label>
                    <ul>
                        <l><a href='/math/exponentials/e'>E</a></l><br>
                        <l><a href='/math/exponentials/exponents'>ExponentLogarithms</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="Single Variable Calculus">
                    <label for="Single Variable Calculus">Single Variable Calculus</label>
                    <ul>
                        <l><a href='/math/single_variable_calculus/chain_rule'>Chain Rule</a></l><br>
                        <l><a href='/math/single_variable_calculus/higher_derivatives'>Higher Derivatives</a></l><br>
                        <l><a href='/math/single_variable_calculus/implicit_derivatives'>Implicit Derivatives</a></l><br>
                        <l><a href='/math/single_variable_calculus/inverse_functions'>Inverse Functions</a></l><br>
                        <l><a href='/math/single_variable_calculus/product_rule'>Product Rule</a></l><br>
                        <l><a href='/math/single_variable_calculus/quotient_rule'>QuotienProduct Rule</a></l><br>
                        <l><a href='/math/single_variable_calculus/rational_exponents'>Rational Exponents</a></l><br>
                        <l><a href='/math/single_variable_calculus/reciprocals'>Reciprocals</a></l><br>
                        <l><a href='/math/single_variable_calculus/trig_function_derivatives'>Trigonometric Function Derivatives</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="Trigonometry">
                    <label for="Trigonometry">Trigonometry</label>
                    <ul>
                        <l><a href='/math/trigonometry/sum_and_difference_formulas'>Trigonometric Sum and Difference Formulas</a></l><br>
                    </ul>
                </l>
                <l><a href='/math/derivatives'>Derivatives</a></l><br>
                <l><a href='/math/limits'>Limits</a></l><br>
                <l><a href='/math/linear_algebra'>Linear Algebra</a></l><br>
                <l><a href='/math/logarithms'>Logarithms</a></l><br>
                <l><a href='/math/point_slope'>Point Slope Formula</a></l><br>
                <l><a href='/math/sets'>Sets</a></l><br>
                <l><a href='/math/tangent_lines'>Tangent Lines</a></l><br>
            </ul>
        </l>

    </div>
</ul>