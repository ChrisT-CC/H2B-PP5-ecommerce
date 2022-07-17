/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Get stripe keys
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
// Set up stripe
var stripe = Stripe(stripe_public_key);
// Create an instance of stripe elements
var elements = stripe.elements();
var style = {
    base: {
        color: '#343a40',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#6c757d'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
// Create a card element
var card = elements.create('card', {style: style});
// Mount the above card element to the div#card-element from checkout.html
card.mount('#card-element');