// ==UserScript==
// @name         Blank WCO Script
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Blank Tampermonkey script for www.wco.tv/*
// @author       MaelPERON
// @match        https://www.wco.tv/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=wco.tv
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function() {
    'use strict';

	var deleted = undefined;

    // Wait for #close-btn to appear
    const waitForCloseBtn = () => {
        const btn = document.querySelector('#close-btn');
        if (btn) {
            console.log(btn);
            btn.removeAttribute('disabled');
            btn.click();
            return true;
        }
        return false;
    };

    // Poll for #close-btn until found
    const intervalId = setInterval(() => {
        const found = waitForCloseBtn();
        console.debug("Check Button...");
        if (found || deleted === true) {
            clearInterval(intervalId);
        }
    }, 100);

    // Your code here...
})();