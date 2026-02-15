# Git LFS Quota Issues

## Error Message
```
batch response: This repository is over its data quota.
Account responsible for LFS bandwidth should purchase more data packs.
```

## What Happened
- **Storage quota:** 1 GB free on GitHub
- **Bandwidth quota:** 1 GB/month free
- You exceeded limits

## Solutions

### Short-term: Buy More Storage
```bash
# GitHub: Settings → Billing → Git LFS Data
# Cost: $5/month per 50 GB
```

---

### Long-term: Migrate to DVC
```bash
# 1. Stop using LFS for new files
# Remove from .gitattributes

# 2. Migrate existing LFS files to DVC
dvc import-url <lfs-file-url> data/model.pkl
dvc push

# 3. Remove from LFS
git lfs untrack "*.pkl"
git rm models/*.pkl
git commit -m "Migrate models to DVC"

# 4. Save $5-20/month
```

---

### Emergency: Reduce LFS Usage
```bash
# 1. Identify large LFS files
git lfs ls-files -s | sort -k2 -n -r | head -10

# Output:
# models/model_v20.pkl - 500 MB
# models/model_v19.pkl - 480 MB
# ...

# 2. Remove old model versions
git rm models/model_v*.pkl
git commit -m "Remove old model versions"

# 3. Push to free up remote storage
git push

# NOTE: This doesn't free local .git/lfs/ storage
# To clean local LFS cache:
git lfs prune
```

---

## Prevention

1. **Use DVC for large/frequent files**
2. **LFS only for occasional large files**
3. **Monitor quota monthly**
4. **Delete old LFS files when obsolete**
5. **Educate team on LFS costs**
