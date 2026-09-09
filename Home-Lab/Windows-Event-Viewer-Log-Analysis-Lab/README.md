# Windows Event Viewer & Log Analysis Lab

## Project Status

✅ Completed

**Date:** September 2026

**Category:** Home Lab

---

## Overview

This lab was completed in a Windows 11 virtual machine running in UTM on macOS.

The objective was to develop practical experience using Windows Event Viewer to review authentication activity, user account events and security logs commonly analysed in IT Support, Systems Administration and Security Operations environments.

The lab focused on identifying successful logins, failed authentication attempts and user account creation events while practising log filtering, event analysis and basic security monitoring concepts within Windows Security Logs.

---

## Skills Practised

- Windows Event Viewer
- Security Log Analysis
- Authentication Monitoring
- Event Investigation
- Security Event Analysis
- Log Filtering
- Custom View Creation
- Security Monitoring Concepts
- Incident Triage Concepts
- Technical Documentation

---

## Lab Environment

| Item | Details |
|--------|--------|
| Host Device | MacBook |
| Platform | UTM |
| Operating System | Windows 11 |
| Tool Used | Event Viewer |
| Lab Type | Personal Home Lab |

---

## Activities Completed

### 1. Open Event Viewer

01-open-event-viewer.png

#### Learning Outcome

Accessed Windows Event Viewer and explored the available event log categories.

---

### 2. Review Security Logs

02-security-log.png

#### Learning Outcome

Navigated to Windows Security Logs and reviewed audit events recorded by the operating system.

---

### 3. Investigate Successful Login Events (4624)

03-successful-login-event.png

#### Learning Outcome

Reviewed Event ID 4624, which records successful authentication activity and user logins.

---

### 4. Investigate Failed Login Events (4625)

04-failed-login-event.png

#### Learning Outcome

Investigated Event ID 4625, which records failed authentication attempts and login failures.

---

### 5. Investigate User Account Creation Events (4720)

05-account-created-event.png

#### Learning Outcome

Reviewed Event ID 4720, which records the creation of new user accounts within Windows.

---

### 6. Analyse Event Details

06-event-details-analysis.png

#### Learning Outcome

Investigated detailed event information including timestamps, users, account actions and audit activity to better understand event reconstruction and incident investigation workflows.

---

### 7. Filter Security Logs

07-filter-security-log.png

#### Learning Outcome

Applied filtering techniques to isolate key authentication and account management events for analysis.

---

### 7A. Investigate Failed Logon Activity

07a-investigating-failed-logon.png

#### Learning Outcome

Analysed failed authentication attempts to identify affected accounts, authentication failures and event-specific information recorded within the Windows Security Log.

---

### 8. Create Custom Authentication Monitoring View

08-custom-view.png

#### Learning Outcome

Created a custom monitoring view to consolidate authentication and account management events commonly reviewed during security investigations.

---

## Key Event IDs Investigated

| Event ID | Description |
|-----------|-------------|
| 4624 | Successful Login |
| 4625 | Failed Login |
| 4720 | User Account Created |

---

## Security Concepts Practised

- Authentication Monitoring
- Windows Security Auditing
- Security Event Analysis
- Security Log Investigation
- User Account Monitoring
- Identity & Access Management (IAM)
- Incident Triage Concepts
- Event Correlation
- Audit Logging

---

## Key Takeaways

This lab provided practical experience using Windows Event Viewer to review and investigate security-related events recorded within Windows Security Logs.

By analysing successful logins, failed authentication attempts and user account creation events, I developed a stronger understanding of how Windows records security activity and how these events can support troubleshooting, monitoring and incident investigation.

The project also reinforced the importance of reviewing authentication activity, identifying unusual behaviour and maintaining visibility into user account actions through security logging and event analysis.

---

## Relevance to IT Support & Security Operations

This lab reflects foundational activities relevant to IT Support and Security Operations environments, including:

- Reviewing Windows event logs
- Investigating authentication activity
- Analysing security events
- Filtering relevant log entries
- Reviewing event details
- Supporting basic incident triage

---
