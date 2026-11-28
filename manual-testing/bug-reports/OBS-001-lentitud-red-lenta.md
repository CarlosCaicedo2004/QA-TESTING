# OBS-001: The home page is very slow on slow network connections

## Type
Performance observation (no performance requirement was provided)

## Environment
Chrome, https://automationexercise.com (home page), DevTools > Network > throttling

## Steps
1. Open DevTools and go to the Network tab.
2. Select the network profile in the throttling dropdown.
3. Reload the home page and record the load time.

## Results
| Network profile | Load time |
|---|---|
| No throttling | about 2 seconds |
| Slow 4G | 26 seconds |
| 3G [write Fast or Slow] | 3.8 minutes |

## Observation
The page becomes almost unusable on poor connections. Without a defined acceptable load time, this is reported as an observation and not as a defect.

## Suggestion
Check which resources are the heaviest (Network tab, sorted by Size) and reduce them. Define a target load time for slow connections.

## Severity / Priority
Low / Low
