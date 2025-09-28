// ==UserScript==
// @name         Medium Overflow Visible
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Sets body overflow to visible on Medium articles
// @author       MaelPERON
// @match        https://*.medium.com/*
 // @run-at       document-end
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
	unsafeWindow.document.body.style.overflow = 'visible';
})();
