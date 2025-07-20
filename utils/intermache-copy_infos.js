// ==UserScript==
// @name         Intermarche Copy Infos
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Script for copying product information on intermarche.com
// @author       MaelPERON
// @match        https://www.intermarche.com/produit/**/*
// @grant        GM_registerMenuCommand
// @grant        GM_setClipboard
// @grant        GM_xmlhttpRequest
// @run-at		 document-end
// ==/UserScript==

(function() {
    'use strict';
	function extract_data() {
		var _document = unsafeWindow.document;
		unsafeWindow._document = _document; // Make _document accessible in the console
		if (!_document) return console.error("Document not found");

		// Define the paths to the elements containing product information
		var product_path = "div:nth-child(1) > h1:nth-child(2)" // marqueproduit
		var name_path = "div:nth-child(1) > h1:nth-child(2) > span" // marque
		var info_path = "div:nth-child(1) > p:nth-child(3)" // commentaire | prix unité
		var price_path = "div.pdpV2-primary-price_e2e:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)" // 1,49 €

		const productElement = _document.querySelector(product_path);
		const nameElement = _document.querySelector(name_path);
		const infoElement = _document.querySelector(info_path);
		const priceElement = _document.querySelector(price_path);

		unsafeWindow.productElement = productElement;
		unsafeWindow.infoElement = infoElement;
		unsafeWindow.priceElement = priceElement;

		var name_marque = nameElement ? nameElement.innerText.trim() : "";
		var name_product = productElement ? productElement.innerText.replace(name_marque, "") : "";
		var comment, price_unit, price;
		[comment, price_unit] = infoElement ? infoElement.innerText.trim().split(' | ') : ["", ""];
		price = priceElement ? priceElement.innerText.trim().replace(/^(\d*)[\.,](\d*).*/, "$1,$2") : "";

		return {
			name_marque: name_marque,
			name_product: name_product,
			comment: comment,
			price_unit: price_unit,
			price: price
		};
	}

	function copyToClipboard(data) {
		unsafeWindow.data = data; // Make data accessible in the console for debugging
		var text = `${data.name_marque}\t${data.name_product}\t${data.comment} (${data.price_unit})\t\t${data.price}`;
		unsafeWindow.text = text; // Make text accessible in the console for debugging
		GM_setClipboard(text);
		alert("Product information copied to clipboard!\n" + text);
	}

	function extractAndCopy() {
		const data = extract_data();
		if (data) {
			copyToClipboard(data);
		} else {
			alert("Failed to extract product information.");
		}
	}

	GM_registerMenuCommand("Copy Product Info", extractAndCopy);

	document.addEventListener('keydown', function(e) {
		if (e.ctrlKey && e.shiftKey && e.code === 'KeyL') {
			extractAndCopy();
		}
	});

})();