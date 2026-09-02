# Linux File Permissions & Access Control Lab

## Project Status

✅ Completed

**Date:** September 2026

**Category:** Home Lab

---

## Overview

This lab was completed using Ubuntu running in UTM on macOS.

The objective was to gain practical experience with Linux file permissions, ownership management and access control concepts commonly used in IT Support, System Administration and Cyber Security environments.

The lab focused on understanding how Linux controls access to files through permissions, ownership and group membership.

---

## Skills Demonstrated

- Linux Administration
- File Permission Management
- Access Control
- Least Privilege Principles
- User & Group Management
- Linux Command Line
- Security Awareness
- Technical Documentation

---

## Lab Environment

| Item | Details |
|--------|--------|
| Host Device | MacBook |
| Platform | UTM |
| Operating System | Ubuntu Linux |
| Lab Type | Personal Home Lab |

---

## Activities Completed

### 1. Create Working Directory

**Commands**

```bash
mkdir permissions_lab
cd permissions_lab
pwd
```

**Screenshot:** 01-working-directory.png

### Learning Outcome

Created a dedicated working directory to conduct permission and ownership management activities.

---

### 2. Create Test File and View Permissions

**Commands**

```bash
touch confidential.txt
ls -l
```

**Screenshot:** 02-view-permissions.png

### Learning Outcome

Viewed the default permissions assigned to a new file and learnt how Linux represents permissions using the read, write and execute model.

---

### 3. Restrict Access Using chmod 600

**Commands**

```bash
chmod 600 confidential.txt
ls -l
```

**Screenshot:** Coming Soon

### Learning Outcome

Restricted access so that only the file owner could read and modify the file, applying the principle of least privilege.

---

### 4. Modify Permissions Using chmod 644

**Commands**

```bash
chmod 644 confidential.txt
ls -l
```

**Screenshot:** Coming Soon

### Learning Outcome

Allowed read access to other users while retaining write permissions for the file owner.

---

### 5. View Group Memberships

**Command**

```bash
groups
```

**Screenshot:** Coming Soon

### Learning Outcome

Identified the groups associated with the current user and gained an understanding of group-based access control.

---

### 6. View User and Group Information

**Command**

```bash
id
```

**Screenshot:** Coming Soon

### Learning Outcome

Reviewed user IDs (UID), group IDs (GID) and group memberships used to manage permissions in Linux.

---

### 7. Change File Ownership

**Commands**

```bash
sudo chown labuser confidential.txt
ls -l
```

**Screenshot:** Coming Soon

### Learning Outcome

Changed file ownership to another user account and verified the change, demonstrating ownership management and access control administration.

---

## Security Concepts Practised

- Access Control
- Principle of Least Privilege
- File Ownership
- Permission Management
- User & Group Administration
- Security Administration Concepts

---

## Key Takeaways

This lab provided practical experience managing Linux file permissions and ownership. Through hands-on activities using chmod, chown, groups and id, I developed a stronger understanding of how Linux controls access to files and system resources.

These concepts are relevant to IT Support, Service Desk, System Administration and Cyber Security roles.

---

## Next Steps

Future labs will include:

- Linux Log Analysis
- Basic Network Troubleshooting
- Windows User Administration
- Event Viewer Analysis
- Phishing Investigation Projects
