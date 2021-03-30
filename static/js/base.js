// I forgot how to do JavaScript Maths, used this page to remind me - https://www.w3resource.com/javascript-exercises/javascript-basic-exercise-10.php

function multiplyBy() {
    num1 = document.getElementById("width").value;
    num2 = document.getElementById("length").value;
    area = (num1 * num2);
    price = parseFloat(document.getElementById("price").innerHTML);
    total_price = (area * price);

    document.getElementById("area").innerHTML = num1 * num2 + ' M²';
    document.getElementById("selected_cost").innerHTML = '£' + total_price.toFixed(2);
}



// Found this here - https://tutorialdeep.com/knowhow/change-image-on-dropdown-select-option-jquery/

$(document).ready(function(){
    $('#myselection').on('change', function(){
    	var demovalue = $(this).val(); 
        $("div.myDiv").hide();
        $("#show"+demovalue).show();
        $("#product-img").hide();
    });
});

/* Hide/show Description or specification on Product Detail Page */

//Hide Specification by default

$("#specification").hide();

$('#spec_button').on('click', function() {
        $("#specification").show();
        $("#description").hide();
    });

$('#description_button').on('click', function() {
        $("#specification").hide();
        $("#description").show();
    });
    