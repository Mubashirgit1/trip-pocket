# Pocket Trip -  Testing

![Pocket Trip shown on a variety of screen sizes](/docs/mockup/3-devices-white.png)

Visit the deployed site: [POCKET TRIP](https://pocket-trip-0b51f0f8267b.herokuapp.com/)

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [JavaScript Validator](#javascript-validator)
  * [Lighthouse](#lighthouse)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)

Testing was ongoing throughout the entire build. I utilised Chrome developer tools whilst building to pinpoint and troubleshoot any issues as I went along.

During development I made use of google developer tools to ensure everything was working correctly and to assist with troubleshooting when things were not working as expected.

I utilised the console in the developer tools to work through small sections of JavaScript and ensure that the code was working, and also to troubleshoot where issues were.

I have gone through each page using google chrome developer tools & Firefox inspector tool to ensure that each page is responsive on a variety of different screen sizes and devices.

- - -

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. It was also used to validate the CSS.

* [Home](/docs/testing/html-validator/html/home.png) - Passed.
* [About US](/docs/testing/html-validator/html/about.png) - Passed.
* [Search Flights](/docs/testing/html-validator/html/search.png) - Passed.
* [Login](/docs/testing/html-validator/html/login.png) - Passed.
* [Sign up](/docs/testing/html-validator/html/signup.png) - Passed.
* [COntact US](/docs/testing/html-validator/html/contact.png) - Passed.


* [style.css](/docs/testing/html-validator/css/style.png) - Passed, no errors found.

- - -

### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.

* [javascript.js](/docs/testing/js-hint/search-js.png) - Passed.

- - -

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

### Desktop Results

All pages of the site are achieving a score of 100 across the 4 categories.

![Home](/docs/testing/lighthouse/home-desktop.png)

![About](/docs/testing/lighthouse/about-home.png)

![Contact](/docs/testing/lighthouse/contact-desktop.png)

![Search](/docs/testing/lighthouse/desktop-search.png)


### Mobile Results

Each page is achieving a score of 100 for the last three categories. The performance category is achieving a score of 98 for the first three pages and a score of 99 on the 404 & 500 page.

![Home](/docs/testing/lighthouse/home-mobile.png)

![About](/docs/testing/lighthouse/about-mobile.png)

![Contact US](/docs/testing/lighthouse/contact-mobile.png)

![Search](/docs/testing/lighthouse/mobile-search.png)


- - -
## MANUAL TESTING

Manual testing was conducted to ensure the application works as expected based on real-world usage scenarios.

## 🧪 Testing User Stories

This section documents the manual testing performed for the **Flight Search Web Application**.  
Each user story describes a specific feature tested to ensure proper functionality and user experience.

---

### ✅ User Story 1 – Search Flights Between Countries
**As** a traveler  
**I want to** search for flights between different countries  
**So that** I can find available routes, airlines, and ticket prices.

- [x] Entered valid departure and arrival countries → List of available flights displayed  
- [x] Invalid or same origin/destination → Proper error message shown  
- [x] Date selection and passenger count validated correctly  
- [x] Search results show airline, flight number, duration, and fare information  

---

### ✅ User Story 2 – User Registration
**As** a new user  
**I want to** register an account  
**So that** I can log in and save my preferences or bookings.

- [x] Registration form validates required fields (name, email, password)  
- [x] Invalid email/password shows clear error messages  
- [x] Successful registration redirects to login page  
- [x] Duplicate email check handled gracefully  

---

### ✅ User Story 3 – User Login
**As** a returning user  
**I want to** log in securely  
**So that** I can access my flight search history or personalized features.

- [x] Valid credentials → User logged in successfully  
- [x] Invalid credentials → Error message displayed  
- [x] Remember-me / session persistence tested  
- [x] Logout button clears session and redirects to home  

---

### ✅ User Story 4 – Contact Us Form
**As** a visitor  
**I want to** send feedback or inquiries through a contact form  
**So that** I can reach the support team easily.

- [x] All fields (name, email, message) validated  
- [x] Invalid email format → Error message shown  
- [x] Successful submission → Confirmation message displayed  
- [x] Form resets after successful send  

---

### ✅ User Story 5 – About Us Page
**As** a user  
**I want to** learn more about the company and its mission  
**So that** I can trust and understand the platform I’m using.

- [x] Page loads properly with team and mission information  
- [x] All links and media load correctly  
- [x] Responsive layout verified  

---

### ✅ User Story 6 – Home Page
**As** a visitor  
**I want to** view an overview of the platform  
**So that** I can easily navigate to key features like search and login.

- [x] Navigation bar and links function correctly  
- [x] Hero section loads images/text properly  
- [x] Buttons (Search Flights, Login, Register) navigate as expected  
- [x] Responsive layout verified on desktop, tablet, and mobile  

---

## 🧩 Additional Manual Tests
- [x] All forms include proper input validation and error messages  
- [x] Tested across Chrome, Firefox, and Edge browsers  
- [x] Responsive design verified on desktop, tablet, and mobile devices  
- [x] Smooth navigation and consistent layout across pages  

---

### 🧭 Test Environment
- **Browsers:** Chrome v128, Firefox v120, Edge v126  
- **Devices:** Desktop, Laptop, Mobile (Android), Tablet (iPad)  
- **Date:** October 2025  
- **Tested By:** [Your Name]  
- **Project:** Flight Search Web App

---

## 🧰 How to Perform Manual Tests
1. Open the application in your browser.  
2. Navigate to the **Home Page** and test navigation links.  
3. Use the **Search Flights** page to test different country pairs and inputs.  
4. Register a new account and verify email/password validation.  
5. Log in with your credentials and check secure session handling.  
6. Test **Contact Us** form submissions and input validation.  
7. Review **About Us** page content and responsiveness.

---

### Full Testing

Full testing was performed on the following devices:

* Laptop:
  * Macbook Pro 2021 14 inch screen
* Mobile Devices:
  * iPhone 13 pro.
  * iPhone 11 pro.
  * Phone X.

Each device tested the site using the following browsers:

* Google Chrome
* Safari
* Firefox

Additional testing was taken by friends on a variety of devices and screen sizes and Multiple FLights. They reported no issues when searching.

