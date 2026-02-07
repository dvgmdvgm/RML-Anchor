# 🧹 Cleanup Settings

> **Version**: 1.0.0  
> **Last Updated**: 2026-02-05

---

## ⏳ TTL Settings (Time-to-Live)

Define how long entries should live before being marked for review:

```yaml
TTL_BY_CATEGORY:
  # Context (volatile)
  07_context/current_session.md: 1      # days
  07_context/pending_tasks.md: 7         # days
  07_context/session_history/*: 30       # days
  07_context/walkthroughs/*: 90          # days
  
  # Problems (medium-term)
  06_problems/bugs/*: 60                 # days
  06_problems/workarounds/*: 90          # days - should become fixes!
  
  # Decisions (long-term)
  03_decisions/*: 365                    # days
  
  # Architecture (permanent)
  02_architecture/*: 0                   # 0 = no expiration
  01_project/*: 0                        # 0 = no expiration
  
  # External (medium-term, APIs change)
  09_external/*: 180                     # days
  
  # Default for unspecified
  DEFAULT: 180                           # days
```

---

## ⭐ Importance Score Settings

```yaml
# Base weights by category (0.0 - 1.0)
BASE_WEIGHTS:
  03_decisions: 0.9      # ADRs are critical
  02_architecture: 0.85  # Architecture is important
  01_project: 0.8        # Project info matters
  04_domain: 0.75        # Business rules
  05_code: 0.6           # Code docs
  06_problems: 0.7       # Problems/solutions
  09_external: 0.6       # External deps
  07_context: 0.3        # Session context (volatile)
  08_people: 0.5         # People info
  10_testing: 0.5        # Testing
  11_deployment: 0.7     # Deployment is important
  12_roadmap: 0.4        # Plans change
  13_preferences: 0.6    # User prefs

# Minimum score by category (floor value)
MIN_SCORES:
  03_decisions: 0.5      # Never delete decisions easily
  02_architecture: 0.4   # Protect architecture
  DEFAULT: 0.1

# Score thresholds for actions
THRESHOLDS:
  CRITICAL: 0.7          # Never auto-delete
  IMPORTANT: 0.4         # Summarize before delete
  ARCHIVE: 0.2           # Archive candidate
  DELETE: 0.1            # Delete candidate
```

---

## 🔄 Periodic Cleanup Settings

```yaml
# When to run cleanup checks
CLEANUP_TRIGGERS:
  ON_WAKEUP: true        # Quick check at session start
  ON_SLEEP: true         # Full check at session end
  MANUAL_ONLY: false     # If true, only /anchor_cleanup works

# What to do with files
CLEANUP_ACTIONS:
  # Session history older than TTL
  SESSION_HISTORY:
    action: summarize_and_archive
    keep_summary: true
    
  # Duplicate entries
  DUPLICATES:
    action: merge
    keep_newest: true
    
  # Empty files
  EMPTY_FILES:
    action: delete
    confirm: false
    
  # Low score entries
  LOW_SCORE:
    action: prompt_user
    threshold: 0.2
```

---

## 📝 Summarization Settings

```yaml
# How to summarize old entries
SUMMARIZATION:
  # Session history merge
  SESSION_MERGE:
    enabled: true
    period: monthly           # daily, weekly, monthly
    max_summary_lines: 50
    keep_decisions: true      # Always preserve decisions
    keep_problems: true       # Always preserve problems
    
  # Topic compression
  TOPIC_COMPRESS:
    enabled: true
    min_files_to_trigger: 5   # Compress when 5+ files on same topic
    
  # Archive summary
  ARCHIVE_SUMMARY:
    enabled: true
    format: "metadata + 1 paragraph"
```

---

## 📦 Backup Settings

```yaml
BACKUP:
  # Where to store backups
  BACKUP_DIR: ".agent/backups"
  
  # Backup format
  FORMAT: "zip"
  
  # Naming pattern
  FILENAME_PATTERN: "anchor_backup_{date}_{time}.zip"
  
  # Auto-backup before dangerous operations
  AUTO_BACKUP_BEFORE:
    - anchor_remove
    - anchor_cleanup (delete action)
    
  # Keep last N backups
  MAX_BACKUPS: 5
  
  # Delete old backups automatically
  AUTO_DELETE_OLD: true
```

---

## 🔐 Safe Remove Settings

```yaml
SAFE_REMOVE:
  # Require confirmation code
  REQUIRE_CODE: true
  
  # Code length
  CODE_LENGTH: 8
  
  # Code characters
  CODE_CHARS: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  
  # Create backup before remove
  CREATE_BACKUP: true
  
  # Backup filename
  FINAL_BACKUP_NAME: "anchor_backup_FINAL_{date}.zip"
```

---

## 🔧 Advanced Settings

```yaml
# Performance
MAX_FILES_TO_SCAN: 1000
SCAN_TIMEOUT_SECONDS: 30

# Logging
LOG_CLEANUP_ACTIONS: true
LOG_FILE: ".agent/logs/cleanup.log"

# Dry run mode (show what would happen without doing it)
DRY_RUN_BY_DEFAULT: true
```
