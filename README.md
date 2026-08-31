# Monthly demo — Reltio IDE Git integration

McDonald’s **DEV**, **TEST**, and **PROD** tenant configuration in one Git repository. Same starting L3 in the three folders. Reltio IDE keeps this structure in the tree.

| Path | What it is |
|---|---|
| `dev/BusinessConfig.json` | DEV tenant L3 — all modeling work happens here first |
| `test/BusinessConfig.json` | TEST tenant L3 — starts identical to DEV; promote after review |
| `prod/BusinessConfig.json` | PROD tenant L3 — same starting file; for structure (promote the same way as TEST) |
| `L3.json` | Copy of the business configuration at repo root (Add Config / other filename) |

**Branches**

| Branch | Role |
|---|---|
| `main` | Integration — PRs merge here |
| `release` | What the data modeler copies into Postman to update a Reltio tenant |
| `feat/user1-delivery-partner` | User 1 (Priya) — `DeliveryPartner` |
| `feat/user2-loyalty-offer` | User 2 (Ankur) — `LoyaltyOffer` |

User 3 creates `feat/user3-menuitem` live during the demo.

Config seed: [snehilkamal/reltio-config](https://github.com/snehilkamal/reltio-config) Consumer360, plus a small `Location` type so three parallel entity inserts merge cleanly.
