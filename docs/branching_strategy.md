# Branching & Merging Strategy

## Branch Types & Merge Strategies

| Branch Type | Merge Strategy | Reasoning |
|-------------|----------------|-----------|
| **feature/** | Regular merge | Preserve development history |
| **experiment/** | Squash merge | Only final result matters |
| **hotfix/** | Regular merge | Fast merge, preserve context |
| **model/** | Regular merge | Track model evolution |

## When to Use Each Merge Strategy

### Regular Merge
**Use when:**
- Feature took multiple commits to develop
- Want to preserve context
- Multiple people collaborated
- Might need to revert entire feature

**Example:** `feature/api-endpoint` with 10 commits
```bash
git checkout main
git merge feature/api-endpoint
```

---

### Squash Merge
**Use when:**
- Experiment branch with messy commits
- Only care about final result
- Branch has WIP commits ("fix typo", "debugging")
- Want clean main branch

**Example:** `experiment/neural-network` with 50 commits
```bash
git checkout main
git merge --squash experiment/neural-network
git commit -m "Add neural network model option

Experimented with deep learning approach.
Results: No improvement over Random Forest.
Decision: Stick with Random Forest."
```

---

### Rebase
**Use when:**
- Local branch not yet pushed
- Want linear history
- Comfortable with rebase workflow
- No one else is working on branch

**Example:** Local `feature/refactoring` branch
```bash
git checkout feature/refactoring
git rebase main
git checkout main
git merge feature/refactoring  # Fast-forward
```

## ML-Specific Guidelines

### Experiments
- **Always squash merge** experiment branches
- Include metrics in commit message
- Document why experiment succeeded/failed

### Models
- **Regular merge** model branches
- Tag production models: `git tag v1.0-model`
- Keep model branches for audit trail

### Hotfixes
- **Regular merge** for traceability
- Fast-track to production
- No squash (preserve debug commits)

## Branch Lifecycle
```
feature/  → Develop → Review → Merge → Delete
experiment/ → Develop → Evaluate → Merge/Archive → Keep for reference
hotfix/ → Fix → Test → Merge → Deploy → Delete
model/ → Train → Validate → Deploy → Keep (tagged)
```
