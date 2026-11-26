# Login and Access Issue

| | |
|---|---|
| **Category** | Login and access |
| **Escalations (1 Sep to 16 Nov 2026)** | 8 direct reports, plus related AWS disconnect reports |
| **Last updated** | 25 Nov 2026 |

## Quick Reference

| # | Scenario | Who fixes it |
|---|---|---|
| 1 | AWS client locked after wrong credentials | IT |
| 2 | Wrong registration code | Agent |
| 3 | Lost or deleted 2FA code | IT |
| 4 | Connection timeout at login | Agent |
| 5 | Correct 2FA code shows as wrong | Agent |
| 6 | AWS client update fails with an error code | IT |
| 7 | WorkSpace disconnects again and again | Agent |

## Scenario 1: AWS client is locked out

**Symptom:** The agent tried to log in several times with wrong credentials. The AWS client is now locked.

**Fix:** Escalate to IT. IT unlocks the account manually in IAM management.

## Scenario 2: Wrong registration code

**Symptom:** The agent cannot log in although everything else is correct. The agent entered a different registration code.

**Fix:** Check the registration code carefully before you sign in.

## Scenario 3: Lost or deleted 2FA code

**Symptom:** The agent deleted or lost the 2FA code by mistake and is stuck on the verification code page.

**Fix:** Escalate to IT. IT resets the 2FA authenticator for the account, sets up a new one, and delivers it to the agent.

## Scenario 4: Connection timeout at login

**Symptom:** The agent gets a connection timeout while logging in.

**Fix:** Follow the steps in order. Stop when the problem is gone.

1. Check your network status. If the round trip time is too long, AWS does not connect. Look at the AWS connection status in the top-right corner and confirm that the round trip time is reasonable.
2. If the round trip time is high, check what uses the internet on your computer. A local VPN causes this problem. Turn off the VPN, then try to log in.
3. If the network problem continues, restart your router and any other network device, then try again.
4. If the problem continues and your internet speed is poor, call your local internet service provider.

## Scenario 5: Correct 2FA code shows as wrong

**Symptom:** The agent enters the correct 2FA code and the system still rejects it.

**Fix:** Check the time and date on your device. A time or date mismatch causes wrong or expired codes. Set the time and date to update automatically, then try again.

## Scenario 6: AWS client update fails

**Symptom:** The AWS client does not update properly and shows an error code during installation.

**Fix:** Escalate to IT with the error code. IT checks the error code first, then configures the temp file on your local machine. This resolves the issue.

## Scenario 7: WorkSpace disconnects again and again

**Symptom:** The WorkSpace disconnects repeatedly.

**Fix:**

1. Close the client.
2. Wait 2 minutes.
3. Sign in again.

If the disconnects continue, check the round trip time and the network, as described in Scenario 4.

## Include in the Escalation

- The scenario number or a short description of the problem
- The error code or message on your screen
- The time the problem started
- The steps you already tried

Never send your password or a 2FA code in an escalation message.
