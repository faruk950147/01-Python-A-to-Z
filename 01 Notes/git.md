# 1. ============================================================== What is Git Git Introduction ================================================================
    Git is a version control system that helps track changes in code and collaborate with others.

# 2. ============================================================== Git SSH ==========================================================================
    #!/bin/bash
    # GitHub SSH one time setup script (Windows Git Bash)
    ssh -T git@github.com
    # Email input
    read -p "Enter your GitHub email: " email
    # New SSH key generation
    ssh-keygen -t ed25519 -C "$email"
    # SSH agent start
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
    # Public key display
    echo ""
    echo "==============================================="
    echo "Your public key is below, add it to GitHub:"
    echo "==============================================="
    cat ~/.ssh/id_ed25519.pub
    echo "==============================================="
    echo ""
    # SSH test
    echo "GitHub SSH test is running..."
    ssh -T git@github.com

# 3. ============================================================== Git Useful Commands ==========================================================================

| Category                      | Command                                          | Description                                               |
| ----------------------------- | ------------------------------------------------ | --------------------------------------------------------- |
| **Global Configuration**      | `git config --list`                              | Check Git configuration                                   |
|                               | `git config --global user.name "Your Name"`      | Set your username (only once after installation)          |
|                               | `git config --global user.email "you@email.com"` | Set your email (only once after installation)             |
| **Local Repository**          | `git init`                                       | Initialize Git in the working directory                   |
|                               | `git status`                                     | Check changes in working directory                        |
|                               | `git add <file>`                                 | Add file to staging area                                  |
|                               | `git add .` or `git add -A`                      | Add all files to staging area                             |
|                               | `git commit -m "msg"`                            | Commit changes to local repository                        |
|                               | `git log`                                        | View commit history                                       |
|                               | `git diff`                                       | Show changes in working directory compare to staged area  |
|                               | `git diff --staged`                              | Show staged changes                                       |
|                               | `git diff <file>`                                | Show changes in a specific file                           |
|                               | `git reset --hard HEAD~`                         | Reset to previous commit                                  |
|                               | `git reset`                                      | Reset to previous commit (keep changes)                   |
| **Remote Setup**              | `git remote add origin <url>`                    | Add a remote repository                                   |
|                               | `git remote -v`                                  | View remote repository URLs                               |
|                               | `git remote set-url origin <url>`                | Change remote repository URL                              |
|                               | `git remote remove origin`                       | Remove a remote repository                                |
| **Push & Pull**               | `git push -u origin main`                        | Push local repo → remote (first time)                     |
|                               | `git push`                                       | Push changes to remote                                    |
|                               | `git pull origin main`                           | Pull changes from remote → local                          |
|                               | `git clone <url>`                                | Clone a remote repository                                 |
| **Fetch & Merge**             | `git fetch origin`                               | Fetch changes from remote without merging                 |
|                               | `git merge origin/main`                          | Merge remote changes into local branch                    |
| **Branching & Collaboration** | `git checkout -b <branch>`                       | Create & switch to a new branch                           |
|                               | `git push -u origin <branch>`                    | Push a branch to remote                                   |
|                               | `git checkout -b <branch> origin/<branch>`       | Track a remote branch locally                             |
|                               | `git push origin --delete <branch>`              | Delete a remote branch                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------|

Step 1: Git cache clean এবং remote prune
git gc --prune=now
git remote prune origin

Step 2: origin folder এ কী কী ref আছে দেখো
ls .git/refs/remotes/origin/

Step 3: যদি main ফাইল corrupt হয়, তাহলে ডিলিট করো
rm -f .git/refs/remotes/origin/main

Step 4: নতুন করে remote থেকে রেফারেন্স ফেচ করো
git fetch origin

Step 5: এখন আবার পুল করো
git pull origin main

#Bonus Step (যদি এখনও এরর আসে):
packed-refs ফাইল corrupt হলে রিসেট করো
mv .git/packed-refs .git/packed-refs.backup
git fetch origin
