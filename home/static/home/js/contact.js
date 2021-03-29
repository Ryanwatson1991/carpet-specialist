/*This page contains the Javascript for contact-us.html page. Mostly concerns email.js contact form*/

//This function gets the form working
function sendMail(contactForm) {
    emailjs.send("carpet_specialist", "carpet_specialist", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "subject": contactForm.subject.value,
        "message": contactForm.message.value
    });
    return false;
}


/*The following disabled the 'Submit' button unless the required fields are filled out. Nescessary both for user experience and also because at one point before I disabled it, 
I kept clicking the button thinking it hadn't worked and then realised I had a LOT of emails sent to me.
I found the solution here: https://joomla.stackexchange.com/questions/4614/make-submit-button-inactive-until-fields-have-been-filled*/

$("#submit").prop('disabled', true);

let toValidate = $('#name, #email, #message'),
    valid = false;
toValidate.keyup(function () {
    if ($(this).val().length > 0) {
        $(this).data('valid', true);
    } else {
        $(this).data('valid', false);
    }
    toValidate.each(function () {
        if ($(this).data('valid') == true) {
            valid = true;
        } else {
            valid = false;
        }
    });
    if (valid === true) {
        $("#submit").prop('disabled', false);
    } else {
        $("#submit").prop('disabled', true);
    }
});