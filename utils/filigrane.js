// ==UserScript==
// @name         Filigrane placeholder
// @namespace    http://tampermonkey.net/
// @version      2025-09-30
// @description  Fill the text input with a default placeholder
// @author       MaelPERON
// @match        https://filigrane.beta.gouv.fr/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=gouv.fr
// @grant        none
// @run-at		 document-end
// ==/UserScript==

(function() {
    'use strict';

    // At document-end, DOM is ready
    const inputs = window.document.querySelectorAll('input.fr-input');
    inputs.forEach(input => {
        input.value = "Document exclusivement réservé à ";
    });

})();