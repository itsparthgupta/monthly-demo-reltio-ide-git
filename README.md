# Monthly demo — Reltio IDE Git integration

Layout matches a real config repo ([snehilkamal/reltio-config](https://github.com/snehilkamal/reltio-config)): `BusinessConfig.json` at the **root** and in **subfolders**, including a nested `DP/` path. Reltio IDE keeps that folder layout in the tree.

`L3.json` is valid business configuration with a different filename — use **Add Config** from Explorer.

| Path | Level | Demo use |
|---|---|---|
| `BusinessConfig.json` | Root | Auto-discovered (Retail) |
| `Insurance/BusinessConfig.json` | Subfolder | Auto-discovered (small — use for the one-prompt / two-config edit) |
| `Consumer360/BusinessConfig.json` | Subfolder | Auto-discovered |
| `DP/dp_lif/BusinessConfig.json` | Nested | Auto-discovered — shows structure is preserved |
| `L3.json` | Root | **Add Config** |

Files (except a missing `entityTypes` array on Insurance, added so the file is a valid business configuration) come from that repo.
