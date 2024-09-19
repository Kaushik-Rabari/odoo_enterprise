/** @odoo-module */

console.log('Session Started/Loaded...!!!')
window.addEventListener('beforeunload', function (e) {
    e.preventDefault();
    console.log('Session Logouting/Destroying...!!!')

    fetch("/web/session/logout", {})
        .then(function () {
            console.log('Session destroyed on browser close/Refreshing...!!!');
        });
    });