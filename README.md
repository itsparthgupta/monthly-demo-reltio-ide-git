# Monthly demo — Reltio IDE Git integration

McDonald’s-style layout: **B2B** and **B2C** business configuration in one Git repo, at the root and in subfolders. Reltio IDE keeps that folder structure in the tree.

| Path | What it is | Demo |
|---|---|---|
| `BusinessConfig.json` | Root — Retail | Auto-discovered |
| `Account360/BusinessConfig.json` | B2B — franchise / restaurant / supplier | Auto-discovered. One-config edit + agent |
| `Consumer360/BusinessConfig.json` | B2C — guest / loyalty | Auto-discovered. Agent |
| `DP/dp_b2b/BusinessConfig.json` | Nested B2B pack | Auto-discovered — structure is preserved |
| `L3.json` | Valid config, different filename | **Add Config** |

Configs are taken from [snehilkamal/reltio-config](https://github.com/snehilkamal/reltio-config).
