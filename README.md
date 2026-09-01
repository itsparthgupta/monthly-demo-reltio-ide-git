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

**CI/CD (demo):** when a PR is merged to `main`, GitHub Actions PUTs `dev/BusinessConfig.json` to the Reltio tenant.

Repo **Variables:** `RELTIO_ENVIRONMENT` (e.g. `tst-01`), `RELTIO_TENANT`.  
Repo **Secrets:** `RELTIO_USERNAME` + `RELTIO_PASSWORD`, or `RELTIO_CLIENT_ID` + `RELTIO_CLIENT_SECRET`.

Config seed: exact B2B `Account360/BusinessConfig.json` from [snehilkamal/reltio-config](https://github.com/snehilkamal/reltio-config) — copied into `dev/`, `test/`, `prod/`, and root `L3.json`.
