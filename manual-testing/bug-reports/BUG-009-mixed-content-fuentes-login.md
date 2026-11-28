# BUG-009: Insecure stylesheets are blocked on the login page (mixed content)

## Environment
Chrome, https://automationexercise.com/login

## Steps to reproduce
1. Open https://automationexercise.com/login
2. Open DevTools and go to the Console tab.
3. Reload the page.
4. Check the Console. Three Mixed Content errors appear.

## Actual result
The page loads over HTTPS, but it requests three Google Fonts stylesheets over HTTP, and Chrome blocks them:
- http://fonts.googleapis.com/css?family=Roboto:400,300,400italic,500,700,100
- http://fonts.googleapis.com/css?family=Open+Sans:400,800,300,600,700
- http://fonts.googleapis.com/css?family=Abel

## Expected result
All resources should load over HTTPS and nothing should be blocked.

## Suggestion
The URLs use http:// instead of https://. Changing them to https:// should fix the issue.

## Severity / Priority
Low / Low

## Evidence
[Screenshot of the Console showing the three errors]
