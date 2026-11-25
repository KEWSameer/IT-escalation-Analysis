# VPN Issue: Slowness After Connecting

| | |
|---|---|
| **Category** | VPN |
| **Escalations (1 Sep to 16 Nov 2026)** | 6 direct VPN reports, plus 5 AWS reports linked to VPN outages or updates |
| **Last updated** | 25 Nov 2026 |

## Symptom

Before agents connect to the VPN, Intercom and other tabs work fine. After they connect, slowness starts.

Agents must connect to the VPN to access Backoffice, so they cannot work without it. They face the slowness every time they connect.

## Quick Checks for Agents

Complete the steps in order. Stop when the problem is gone.

### Step 1: Check your internet connection

Open your web browser and run a speed test on [speedtest.net](https://www.speedtest.net/) by Ookla. Confirm that your internet works properly.

### Step 2: Update Chrome and clear the cache and cookies

If your internet speed is fine, update Chrome, then clear the cache and cookies. This removes unwanted data that slows the browser.

1. Open the three-dot menu in the top-right corner.
2. Go to **Settings**, then **About Chrome**, and install any update.
3. Open **Settings**, then **Privacy and security**, then **Clear browsing data**.
4. Select **Cookies and other site data** and **Cached images and files**.
5. Click **Clear data**.

### Step 3: Reinstall the OpenVPN profile

If the problem continues, delete your OpenVPN profile, install the profile again, and connect.

### Step 4: Change the VPN location

Switch the VPN location to **Chicago** or **Singapore**, then check the speed again.

If the new location fixes the slowness, the cause is the load on the server of the first location.

## Escalate to IT When

The problem continues after you complete all four steps. Contact IT support for further investigation.

## Include in the Escalation

- The VPN locations you tried
- The steps you already tried
- The time the slowness started

IT investigates each case further.
