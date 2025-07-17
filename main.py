from datetime import datetime
from imap_tools import MailBox, MailboxFolderDeleteError
import getpass

# Get credentials from user input
print("Gmail Email Deletion Script")
print("=" * 30)
print("⚠️  WARNING: This will delete ALL emails and folders from your Gmail account!")
print("⚠️  This action is IRREVERSIBLE!")
print()

try:
    # Confirm user wants to proceed
    input("Press \"Enter\" to continue or \"Ctrl+C\" to cancel...")
    print("Starting email deletion process...")
    print()
    EMAIL = input("Enter your Gmail address: ").strip()
    print("Enter your Google App Password (not your regular password):")
    print("Get it from: https://myaccount.google.com/apppasswords")
    APP_PASSWORD = getpass.getpass("Google App Password: ").strip()

    with MailBox("imap.gmail.com").login(EMAIL, APP_PASSWORD) as mailbox:
        print(f"✅ Successfully logged in to: {EMAIL}")
        print("Retrieving folder list...")
        folders = mailbox.folder.list()
        print(f"Found {len(folders)} folders to process")
        total_deleted = 0
        deleted_folders = []

        for folder in folders:
            folder_name = folder.name
            print(f"\nProcessing folder: {folder_name}")

            # Skip "All Mail" folder as it contains copies of all emails
            if folder_name == "[Gmail]/All Mail":
                print(f'→ Skipping "{folder_name}" (contains copies of all emails)')
                continue

            # Try to select the folder - skip if it can't be selected (like [Gmail] which is a namespace/container folder in Google Mail)
            try:
                mailbox.folder.set(folder_name)
            except Exception:
                print(f"→ Could not use folder: {folder_name} (likely a namespace)")
                continue

            # Process emails in batches
            folder_deleted = 0
            batch_size = 100

            while True:
                # Fetch emails in batches
                uids = [msg.uid for msg in mailbox.fetch(limit=batch_size)]
                batch_count = len(uids)

                # No more emails to process
                if batch_count == 0:
                    break

                print(f"→ Processing batch of {batch_count} messages")
                mailbox.delete(uids)
                folder_deleted += batch_count
                total_deleted += batch_count
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"→ Deleted {batch_count} messages from this batch at {timestamp}")
                mailbox.expunge()
                print(f"→ Emptied trash for this batch")

                # If we got fewer messages than the batch size, we're done
                if batch_count < batch_size:
                    break

            if folder_deleted > 0:
                print(f"→ Total messages deleted from folder: {folder_deleted}")
            else:
                print("→ No messages to delete")

            # Try to delete the folder (even Inbox or system folders)
            try:
                mailbox.folder.delete(folder_name)
                deleted_folders.append(folder_name)
                print(f"→ Folder deleted: {folder_name}")
            except MailboxFolderDeleteError:
                print(f"→ Could not delete folder: {folder_name} (likely a system folder)")
            except Exception as e:
                print(f'→ Error deleting folder "{folder_name}": {e}')

        print(f"\n✅ Total messages deleted: {total_deleted}")
        print(f"✅ Folders successfully deleted: {len(deleted_folders)}")
except KeyboardInterrupt:
    print("\n Operation cancelled by user (KeyboardInterrupt). Exiting cleanly.")
