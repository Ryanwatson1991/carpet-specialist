/*
    Remember to include credit to Stripe css & accept a payment page
*/


var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
  base: {
    color: '#000',
    fontSize: '16px',
    fontFamily: '"Open Sans", sans-serif',
    fontSmoothing: 'antialiased',
    '::placeholder': {
      color: '#CFD7DF',
    },
  },
  invalid: {
    color: '#e5424d',
    ':focus': {
      color: '#303238',
    },
  },
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

