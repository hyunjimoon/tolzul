#!/usr/bin/env python3
import subprocess
import os
import re

def get_large_files():
    """Get list of files larger than 2MB in Git history."""
    cmd = 'git rev-list --objects --all | git cat-file --batch-check="%(objectname) %(objecttype) %(objectsize) %(rest)"'
    output = subprocess.check_output(cmd, shell=True).decode('utf-8')
    
    large_files = []
    for line in output.splitlines():
        # Parse the line
        match = re.match(r'^(\w+)\s+(\w+)\s+(\d+)\s*(.*)$', line)
        if match:
            sha, type_, size, path = match.groups()
            # Convert size to MB
            size_mb = int(size) / (1024 * 1024)
            if size_mb > 2 and type_ == 'blob':
                large_files.append((path, sha, size_mb))
    
    return large_files

def remove_files_from_history(files):
    """Remove specified files from Git history."""
    if not files:
        print("No files larger than 2MB found.")
        return
    
    # Create the filter-branch command
    file_paths = [f"'{f[0]}'" for f in files]
    paths_str = ' '.join(file_paths)
    
    commands = [
        f'git filter-branch --force --index-filter \'git rm --cached --ignore-unmatch {paths_str}\' --prune-empty --tag-name-filter cat -- --all',
        'git reflog expire --expire=now --all',
        'git gc --prune=now --aggressive'
    ]
    
    print("\nProcessing the following files:")
    for path, sha, size in files:
        print(f"- {path} ({size:.2f}MB)")
    
    print("\nExecuting cleanup commands...")
    for cmd in commands:
        try:
            subprocess.run(cmd, shell=True, check=True)
            print(f"Successfully executed: {cmd}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {cmd}")
            print(f"Error: {str(e)}")
            return False
    
    print("\nCleanup completed successfully!")
    print("To push changes to remote repository, use:")
    print("git push origin --force --all")
    
    return True

def main():
    print("Scanning repository for large files...")
    large_files = get_large_files()
    
    if not large_files:
        print("No files larger than 2MB found in the repository.")
        return
    
    print("\nFound the following large files:")
    for path, sha, size in large_files:
        print(f"- {path} ({size:.2f}MB)")
    
    response = input("\nDo you want to proceed with removing these files from history? (y/n): ")
    if response.lower() == 'y':
        remove_files_from_history(large_files)
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()