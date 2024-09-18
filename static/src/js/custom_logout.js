/** @odoo-module */

import { Session } from '@web/session';
// import { useService } from '@web/core/utils/hooks';
// import { rpcService } from "@web/core/network/rpc_service";


// window.addEventListener('beforeunload', function (e) {
//     // Prevent the default action of the event
//     e.preventDefault();
    
//     // Retrieve the CSRF token from a meta tag
//     const csrfToken = document.querySelector('input[name="csrf-token"]').getAttribute('t-att-value');
    
//     // Make a fetch request to destroy the session
//     fetch('/web/session/logout', {
//         method: 'GET',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRF-Token': csrfToken // Include CSRF token in the request headers
//         },
//         credentials: 'same-origin'
//     })
//     .then(response => response.ok ? console.log('Session destroyed on browser close') : console.error('Failed to destroy session'))
//     .catch(error => console.error('Error destroying session:', error));
// });





















// window.addEventListener('beforeunload', function (e) {
//     // Prevent the default action of the event
//     e.preventDefault();
    
//     // Using a simple fetch API to destroy the session
//     fetch('/web/session/logout', {
//         method: 'POST',
//         credentials: 'same-origin'
//     })
//     .then(response => response.ok ? console.log('Session destroyed on browser close') : console.error('Failed to destroy session...'))
//     .catch(error => console.error('Error destroying session:', error));
// });








// $(window).on('load', function () {
//     // alert("destroying soon.......!!!!!!")
//     console.log('Session Started/Loaded...!!!')
// });

// $(window).on('beforeunload', function (e) {
//     e.preventDefault();
//     e.returnValue = 'are you want to destroy this session'
//     alert("Destroying Soon.......!!!!!!")
//     rpc = useService('rpc');  // Access RPC service
//     Session.rpc('/web/session/destroy', {})
// });



window.addEventListener('load', function (e) {
    e.preventDefault();
    fetch("/web/login", {})
        .then(function () {
            console.log('Session Started/Loaded...!!!')
        });
    });

// $(window).on('beforeunload', function (e) {
//     e.preventDefault();
//     console.log('Session Logouting/Destroying...!!!')
//     fetch("/web/session/logout", {})
//         .then(function () {
//             console.log('Session destroyed on browser close/Refreshing...!!!');
//         });
//     });
