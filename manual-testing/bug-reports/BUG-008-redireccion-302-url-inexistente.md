# BUG-008: Non-existent URL redirects (302) to the home page instead of returning a 404 error

## Environment
Chrome, https://automationexercise.com

## Steps to reproduce
1. Open DevTools, go to the Network tab and check "Preserve log".
2. Type https://automationexercise.com/this-page-does-not-exist in the address bar.
3. Sort the request list by Status (ascending).
4. Find the request named "this-page-does-not-exist" with status 302.

## Actual result
The request returns status 302 (type: document / redirect) and the Location header points to the home page [replace with the exact Location value]. The final page loads with status 200 and the URL in the address bar is replaced.

## Expected result
The server should return a 404 status code and display an error page.

## Impact
The user gets no clear error message, so broken links go unnoticed. Automated checks that expect a 404 would not detect them.

## Severity / Priority
Low / Low

## Evidence
[Screenshot of the 302 request with the Headers tab open, showing the Location header]
