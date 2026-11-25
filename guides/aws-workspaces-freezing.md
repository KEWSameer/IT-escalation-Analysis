# AWS Is Slow or Freezing

| | |
|---|---|
| **Category** | AWS WorkSpaces |
| **Escalations (1 Sep to 16 Nov 2026)** | 46 |
| **Last updated** | 25 Nov 2026 |

## Symptom

Agents who are working face serious slowness inside AWS. They report these signs:

- Switching between tabs takes a very long time.
- After a mouse scroll, the page waits 5 to 10 seconds before it starts to scroll, and then it scrolls with heavy lag.

## Quick Checks for Agents

Complete the steps in order. Stop when the problem is gone.

### Step 1: Check your internet connection

AWS WorkSpaces is a cloud-based service, so a weak or unstable connection causes freezing.

1. Test your speed on [speedtest.net](https://www.speedtest.net/).
2. If you use Wi-Fi, switch to a wired connection when possible.
3. Restart your router or try a different network.

### Step 2: Restart the AWS WorkSpaces client

1. Find the **Amazon WorkSpaces** menu at the top of the client.
2. Click **WorkSpaces Client**.
3. Click **Restart WorkSpace**.

### Step 3: Keep Chrome updated inside AWS WorkSpaces

1. Open the Google Chrome browser.
2. Click the three-dot menu in the top-right corner.
3. Go to **Settings**, then **About Chrome**.
4. Chrome checks for updates automatically.
5. If an update is available, click **Update**, then **Restart**.

### Step 4: Check the AWS WorkSpaces status

AWS sometimes has service issues. Open the [AWS WorkSpaces Health Dashboard](https://clients.amazonworkspaces.com/Health.html) and look for an ongoing outage in your region.

### Step 5: Restart your local machine

If the WorkSpace still freezes, restart your local computer. Make sure no background application uses excessive resources.

## Escalate to IT When

The slowness continues after you complete all five steps.

## Include in the Escalation

- A screenshot of the AWS connection health
- A screenshot with the VPN page open
- The time the slowness started
- The steps you already tried

IT investigates each case further.
