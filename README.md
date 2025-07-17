# Gmail Email Deletion

> [!WARNING]  
> This script will permanently delete ALL emails and folders from your Gmail account. Use with extreme caution!

## What This Script Does

This Python script connects to your Gmail account via IMAP and:

- **Deletes ALL emails** from every folder in your Gmail account
- **Deletes ALL folders** (except system folders that can't be deleted)
- **Permanently removes emails** by emptying trash after each batch

## Prerequisites

1. **Gmail App Password**: You need to generate an App Password (not your regular Gmail password)

   - Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
   - Generate a new App Password for "Mail"
   - Use this password in the script

2. **IMAP Access**: Ensure IMAP is available in your Gmail settings
   - Go to Gmail Settings → [Forwarding and POP/IMAP](https://mail.google.com/mail/u/0/#settings/fwdandpop)
   - Contact your workspace administrator if IMAP is not enabled (see [Turn POP & IMAP on or off for users](https://support.google.com/a/answer/105694?hl=en&sjid=12332642361958922417-EU))

## Setup and Usage

### Option 1: GitHub Codespaces

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/bennycode/gmail-email-purger)

1. Click the "Open in GitHub Codespaces" button above
2. Wait for the environment to load
3. Dependencies install automatically
4. Script will run automatically

### Option 2: Local Setup

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Run the script
python main.py
```
