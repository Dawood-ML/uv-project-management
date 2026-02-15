# Pull Request Workflow

## Step-by-Step Process
```
┌─────────────────────────────────────────────────────────────┐
│ 1. CREATE BRANCH                                            │
│    git checkout -b feature/add-api                          │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. DEVELOP FEATURE                                          │
│    - Write code                                             │
│    - Write tests                                            │
│    - Commit changes (multiple commits OK)                   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. PUSH BRANCH                                              │
│    git push -u origin feature/add-api                       │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. OPEN PULL REQUEST (GitHub)                               │
│    - Navigate to repo on GitHub                             │
│    - Click "Compare & pull request"                         │
│    - Fill out PR template                                   │
│    - Assign reviewers                                       │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. AUTOMATED CHECKS RUN                                     │
│    ✓ Tests pass                                             │
│    ✓ Linting passes                                         │
│    ✓ Code coverage meets threshold                          │
│    ✓ No merge conflicts                                     │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 6. CODE REVIEW                                              │
│    Reviewer checks:                                         │
│    - Code quality                                           │
│    - Tests coverage                                         │
│    - Documentation                                          │
│    - ML-specific: metrics, data handling, reproducibility   │
└─────────────────────────────────────────────────────────────┘
                          ↓
                    Changes needed?
                    ↙           ↘
                  Yes            No
                   ↓              ↓
┌──────────────────────┐   ┌─────────────────┐
│ 7. ADDRESS FEEDBACK  │   │ 8. APPROVE PR   │
│    - Fix issues      │   │    ✓ Approved   │
│    - Push updates    │   └─────────────────┘
│    - Re-request      │            ↓
│      review          │            │
└──────────────────────┘            │
         ↓                          │
         └──────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────────────────┐
│ 9. MERGE TO MAIN                                            │
│    Options:                                                 │
│    - Merge commit (preserves history)                       │
│    - Squash merge (clean history)                           │
│    - Rebase merge (linear history)                          │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 10. DELETE BRANCH                                           │
│     git branch -d feature/add-api                           │
│     git push origin --delete feature/add-api                │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Points

### For Solo Developers
- **Still use PRs** (GitHub lets you merge your own)
- **Write PR descriptions** (document decisions)
- **Use PR templates** (checklist for quality)
- **Run checks** (automated tests)

**Why?**
- Future employers see your process
- Future you understands past decisions
- Practice for team work
- Forces quality standards

---

### For Teams
- **Require reviews** (at least 1 approval)
- **Automate checks** (tests must pass)
- **Use templates** (consistency)
- **Respond quickly** (don't block teammates)
