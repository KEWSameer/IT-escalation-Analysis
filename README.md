# IT Escalation Troubleshooting Guides

Step-by-step guides for the technical problems that customer support agents escalate to IT most often.

I work in quality assurance on a customer support team. Over three months I watched the same tool problems come back in our IT escalation group: Intercom running slow, AWS WorkSpaces freezing, Backoffice not loading. Many of these reports had a fix the agent could try alone. So I turned the escalations into data, and the data into guides.

## Goal

- Help agents fix common problems before they escalate.
- Give IT cleaner reports when an escalation is needed, with the right details included.
- Show IT which problems repeat, so the root causes get attention.

## What the data shows

I collected every escalation posted in the IT group between **1 September and 16 November 2026**. The file has **155 escalations**. I sorted each one by the tool it concerns.

| Issue type | Escalations | Share |
|---|---|---|
| Intercom | 64 | 41% |
| AWS WorkSpaces | 46 | 30% |
| Backoffice | 23 | 15% |
| Login and access | 8 | 5% |
| VPN | 6 | 4% |
| Other | 8 | 5% |

A few points stand out:

- Intercom and AWS WorkSpaces make up **71%** of all escalations.
- The volume stays steady at about two escalations a day in September, October, and November.
- Most of the same reports repeat on the same days. For example, 8 agents reported Intercom freezing on 21 October, and 8 reports about Backoffice came in on 3 November.
- VPN reports appear mostly in early September. A few AWS disconnect reports in September and November also link to VPN outages and updates.

The five guides below cover **147 of the 155 escalations (95%)**.

## Guides

| Guide | Problem | Escalations |
|---|---|---|
| [Intercom is slow or freezing](guides/intercom-slow-or-frozen.md) | Chats load slowly, switching between chats lags | 64 |
| [AWS is slow or freezing](guides/aws-workspaces-freezing.md) | WorkSpaces lags when agents switch tabs or scroll | 46 |
| [Backoffice not loading](guides/backoffice-not-loading.md) | Agents cannot log in, get logged out, or lack access after the migration | 23 |
| [Login and access issue](guides/login-and-access.md) | Account lockouts, 2FA problems, timeouts, client update errors | 8 |
| [VPN issue](guides/vpn-slow-after-connecting.md) | Slowness that starts after the VPN connects | 6 |

## How the guides work

Every guide follows the same layout:

1. **Symptom.** What the agent sees.
2. **Quick checks.** Steps an agent completes alone, in order.
3. **Escalate when.** The point where the agent contacts IT.
4. **Include in the escalation.** The details IT needs to start work right away.

Some problems need IT from the first minute, such as an account locked in IAM or a lost 2FA code. The guides say so and tell the agent to escalate without trying other steps.

## Repository structure

```
it-escalation-analysis/
├── README.md
├── data/
│   └── escalations_clean.csv
└── guides/
    ├── aws-workspaces-freezing.md
    ├── backoffice-not-loading.md
    ├── intercom-slow-or-frozen.md
    ├── login-and-access.md
    └── vpn-slow-after-connecting.md
```

## About the data

`data/escalations_clean.csv` has two columns: the issue description and the date. Dates use the day/month/year format. I removed agent names, internal links, and credentials before I added the file. The repository holds no customer or account information.

## Status

These guides are drafts written from the agent side. The quick checks come from the steps agents already use, and the escalation lists are my proposal. I want IT to review them before agents rely on them. Every guide shows a last updated date.

## Next steps

- Review each guide with the IT team and correct any step that does not match how IT works.
- Add guides for the remaining repeat issues, such as the microphone and camera not detected in AWS, and chats that do not snooze in Intercom.
- Add a short monitoring plan for the repeat problems, such as AWS WorkSpaces connection health and VPN uptime.

## Author

**Khalid**, Quality Analyst in customer support. I am studying cloud engineering and want to move into IT. This project shows how I look at a recurring problem: collect the data, find the pattern, and write down the fix.
