// I forgot how to do JavaScript Maths, used this page to remind me - https://www.w3resource.com/javascript-exercises/javascript-basic-exercise-10.php

function multiplyBy()
{
        num1 = document.getElementById("width").value;
        num2 = document.getElementById("length").value;
        area = (num1 * num2);
        price = parseFloat(document.getElementById("price").innerHTML);

        document.getElementById("area").innerHTML = num1 * num2;
        document.getElementById("total_cost").innerHTML = '£' + area * price;
}

