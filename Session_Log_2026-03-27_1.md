# Session Log — March 27, 2026
**Session:** 2 | **Duration:** Full day | **Status:** Complete

---

## Session Goal
Establish a fully operational, portfolio-ready development environment in WSL2 and push first GitHub repository.

---

## Environment at Start of Session
- WSL2 Ubuntu 24.04 existed but was unconfigured
- No pip3 installed
- No Git identity configured
- No SSH key
- No GitHub connection
- No repositories

## Environment at End of Session
- WSL2 Ubuntu 24.04.4 LTS — fully configured
- Python 3.12.3 + pip3 24.0 — ready
- Git 2.43.0 — identity configured
- SSH ed25519 key — generated and authenticated to GitHub
- First repository live at github.com/FvanW/career-transition-prep

---

## Commands Executed & Results

### 1. WSL2 Baseline Check
```bash
lsb_release -a && free -h && df -h && python3 --version && pip3 --version
```
**Result:**
- Ubuntu 24.04.4 LTS confirmed
- 13GB RAM available to WSL2 (of 32GB total — Windows manages split)
- 954GB free storage on Linux partition
- Python 3.12.3 confirmed
- pip3 NOT found — needed installation

**Learning:** WSL2 only sees a portion of total RAM. Normal behavior — configurable later for VM workloads in Phase 2.

---

### 2. Install pip3
```bash
sudo apt install python3-pip -y
pip3 --version
```
**Result:** pip 24.0 installed successfully on Python 3.12

**Learning:** Read the error message — it told you exactly what to install. This is how Linux works. The answer is usually in the error.

---

### 3. Verify Core Tools
```bash
git --version && node --version && code --version
```
**Result:**
- Git 2.43.0 — installed ✅
- Node.js — NOT installed in WSL2 ⚠️
- VS Code CLI — not linked ⚠️

**Decision:** Node.js not needed for Phase 1 courses. Do not install yet — avoid unnecessary complexity.

---

### 4. Configure Git Identity
```bash
git config --global user.name "Frederick Van Wagenen"
git config --global user.email "fred.vanwagenen@gmail.com"
git config --list
```
**Result:** Identity confirmed — name and email set correctly.

**Why this matters:** Git uses this email to link commits to your GitHub profile. Mismatched email = invisible portfolio contributions.

---

### 5. Generate SSH Key
```bash
ssh-keygen -t ed25519 -C "fred.vanwagenen@gmail.com"
```
**Result:** ed25519 key pair generated at `~/.ssh/id_ed25519`

**Learning:** Two files created:
- `id_ed25519` — private key (never share this)
- `id_ed25519.pub` — public key (safe to share — added to GitHub)

---

### 6. Add SSH Key to GitHub
```bash
cat ~/.ssh/id_ed25519.pub
```
**Result:** Public key displayed and copied to GitHub Settings → SSH and GPG keys → New SSH key

**Title used:** `WSL2 Ubuntu - Lenovo`

---

### 7. Test GitHub Connection
```bash
ssh -T git@github.com
```
**Result:** `Hi FvanW! You've successfully authenticated...`

**Learning:** This confirms WSL2 can communicate securely with GitHub. All future git push operations will use this authenticated connection.

---

### 8. Update check_system.py
**Original:** Hardcoded "COHORT 16 WORKSHOP STATUS" — no longer relevant
**Updated to:** Career transition prep script with training environment info and health checks

**Changes made:**
- Added `from datetime import date`
- Updated title to `CAREER TRANSITION PREP - ENV CHECK`
- Added date display
- Added training environment section (target role, phase, courses, lab setup)
- Added environment health checks (Python OK, disk OK)
- Removed broken `hello_world()` call

**Final output:**
```
=========================================
   CAREER TRANSITION PREP - ENV CHECK
=========================================
Date:           2026-03-27
OS:             Linux 6.6.87.2-microsoft-standard-WSL2
Python Version: 3.12.3
Disk Space:     952 GB free of 1006 GB

--- TRAINING ENVIRONMENT ---
Target Role:    Cloud Engineer / Cybersecurity Analyst
Current Phase:  Phase 1 - VSF Scholarship (2026)
Active Courses: AWS Cloud Technical Essentials | CS50P | CS50x
Lab Setup:      WSL2 Ubuntu 24.04 on Windows 11

--- ENVIRONMENT STATUS ---
Python 3:       [OK]
Disk Space:     [OK]

[SUCCESS] Environment fully operational. Stay consistent.
=========================================
```

---

### 9. Create First GitHub Repository
```bash
cd ~
mkdir career-transition-prep
cd career-transition-prep
git config --global init.defaultBranch main
git init
git branch -m main
cp ~/asfw-prep/check_system.py .
nano README.md
git add .
git status
git commit -m "Initial commit - environment check script and README"
git remote add origin git@github.com:FvanW/career-transition-prep.git
git push -u origin main
```
**Result:** Repository live at github.com/FvanW/career-transition-prep

**Learning:** `git push -u origin main` sets upstream tracking — future pushes only need `git push`.

---

## Errors Encountered & How They Were Resolved

| Error | Cause | Fix | Learning |
|-------|-------|-----|----------|
| `check_system.py: command not found` | Script not in PATH, not executable | `python3 check_system.py` | Scripts need to be called through their interpreter |
| `Command 'python' not found` | Linux uses `python3` not `python` | `python3 check_system.py` | Python 2 era legacy naming — modern Linux uses python3 |
| `pip3 not found` | Not installed by default in Ubuntu | `sudo apt install python3-pip` | Read the error — it told you the fix |
| `>` prompt stuck in terminal | Accidentally pasted terminal output into terminal | `Ctrl+C` to cancel | Ctrl+C cancels any stuck command and returns clean prompt |
| nano paste confusion | Content appeared lost after save | File was saved correctly — `cat` confirmed | Always verify with `cat` after nano edits |

---

## Key Decisions Made This Session

| Decision | Reasoning |
|----------|-----------|
| Target role changed to Systems Engineer / DevOps / SRE | Better fit for analytical, command-line oriented working style |
| Cybersecurity removed as primary direction | Not a confirmed interest — Security+ retained as single cert |
| CS50x removed from urgent priority | C programming not directly relevant to target roles — time better spent |
| Added NDG Linux Essentials → LPI → CompTIA Linux+ → RHCSA stack | Logical progression reduces RHCSA failure risk significantly |
| CySA+ removed from roadmap entirely | Not aligned with confirmed target direction |
| Node.js not installed in WSL2 yet | Not needed for Phase 1 — avoid unnecessary complexity |

---

## Career Direction Clarified This Session

**Previous plan:** Cloud Engineer / Cybersecurity Analyst (vague, unfocused)

**Updated direction:** Systems Engineer / DevOps / SRE

**Why this fits:**
- Enjoys command-line work and problem solving
- Analytical and intentional before acting
- Quality and efficiency focused
- Systems thinker
- Strong documentation discipline
- AI-integrated workflow natural

---

## Revised Certification Roadmap

| Phase | Timeframe | Focus |
|-------|-----------|-------|
| Phase 1 | 2026 | AWS Cloud Technical Essentials → CS50P → NDG Linux Essentials |
| Phase 2 | Late 2026 — Mid 2027 | LPI Linux Essentials exam → CompTIA Linux+ |
| Phase 3 | Late 2027 — 2028 | RHCSA → Docker & Kubernetes |
| Phase 4 | 2028 — July 2029 | AWS SAA → Terraform → CKA → Security+ → Portfolio complete |

---

## Concepts Learned This Session

### Linux / WSL2
- WSL2 is a real Linux kernel running inside a lightweight VM on Windows
- WSL2 only sees a portion of total RAM — Windows manages the split
- `/mnt/c` mounts your Windows C drive inside Linux
- `python` vs `python3` — modern Linux uses `python3`
- `sudo apt install` — how to install software in Ubuntu

### Git & GitHub
- Git identity (name + email) must match GitHub account for contributions to appear
- SSH keys: private key stays local, public key goes to GitHub
- `git add .` → `git commit` → `git push` — the core workflow
- `git status` — always check before committing
- `init.defaultBranch main` — industry standard is `main` not `master`
- First push uses `-u origin main` — sets upstream tracking permanently

### Python
- Scripts need to be called through their interpreter: `python3 script.py`
- `pip3` is the package manager for Python 3
- `from datetime import date` — importing modules extends Python's capabilities

### Terminal
- `Ctrl+C` — cancels any stuck command, returns clean prompt
- `cat filename` — always verify file contents after editing
- Right-click or `Ctrl+Shift+V` — paste in WSL2 terminal
- `nano` — terminal text editor: `Ctrl+X` → `Y` → `Enter` to save

---

## Daily Workflow Going Forward

### Every Study Session
```bash
# 1. Run environment check
python3 ~/asfw-prep/check_system.py

# 2. Do coursework

# 3. Save your work
git add .
git commit -m "describe what you did"
git push
```

### Weekly Maintenance
```bash
sudo apt update && sudo apt upgrade
```

---

## Next Session Priorities

1. Open AWS Cloud Technical Essentials and complete first module
2. Pin `career-transition-prep` repository to GitHub profile
3. Add bio to GitHub profile
4. Begin NDG Linux Essentials on Cisco NetAcad (free)
5. Add session log to career-transition-prep repository

---

## Repository Status
**github.com/FvanW/career-transition-prep**

| File | Description |
|------|-------------|
| README.md | Project overview and current phase |
| check_system.py | Daily environment readiness check |
| Session_Log_2026-03-27.md | This file |

---

*Session 2 Complete | Next Review: Session 3 | Stay consistent.*
