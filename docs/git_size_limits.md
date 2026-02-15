# Git Size Limits

## GitHub
- **File limit:** 100 MB hard limit
- **Repository limit:** 1 GB recommended, 100 GB hard limit
- **Push limit:** 2 GB per push
- **LFS storage:** 1 GB free, then $5/month per 50GB

## GitLab
- **File limit:** 100 MB default (configurable by admin)
- **Repository limit:** 10 GB recommended
- **LFS storage:** 10 GB free for gitlab.com

## Bitbucket
- **File limit:** 100 MB soft limit
- **Repository limit:** 2 GB recommended, 4 GB hard limit
- **LFS storage:** 1 GB free, then $10/month per 100GB

## What Counts as "Large"?

| File Type | Size | Verdict |
|-----------|------|---------|
| Source code (.py) | 1-100 KB | ✅ Perfect for Git |
| Notebooks (.ipynb) | 100KB-5MB | ⚠️ Clean before commit |
| CSV data | <10MB | ✅ OK for Git |
| CSV data | 10-100MB | ⚠️ Consider DVC |
| CSV data | >100MB | ❌ Use DVC, not Git |
| Models (.pkl) | <10MB | ✅ OK for Git |
| Models (.pkl) | 10-100MB | ⚠️ Use Git LFS |
| Models (.pkl) | >100MB | ❌ Use DVC or model registry |
| Images (training) | Any size | ❌ Use DVC |
| Videos | Any size | ❌ Use DVC |

## Rule of Thumb
- **< 10 MB:** Regular Git ✅
- **10-100 MB:** Git LFS ⚠️
- **> 100 MB:** DVC ❌ (Chunk 4)
