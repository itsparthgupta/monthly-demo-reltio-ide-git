#!/usr/bin/env python3
"""Apply a local BusinessConfig.json to a Reltio tenant via PUT /configuration."""

from __future__ import annotations

import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

AUTH_URL = os.environ.get("RELTIO_AUTH_URL") or "https://auth-stg.reltio.com/oauth/token"
ENVIRONMENT = os.environ.get("RELTIO_ENVIRONMENT", "").strip()
TENANT = os.environ.get("RELTIO_TENANT", "").strip()
CONFIG_PATH = os.environ.get("RELTIO_CONFIG_PATH", "dev/BusinessConfig.json")
USERNAME = os.environ.get("RELTIO_USERNAME", "").strip()
PASSWORD = os.environ.get("RELTIO_PASSWORD", "").strip()
CLIENT_ID = os.environ.get("RELTIO_CLIENT_ID", "").strip()
CLIENT_SECRET = os.environ.get("RELTIO_CLIENT_SECRET", "").strip()


def fail(message: str, code: int = 1) -> None:
    print(f"::error::{message}", file=sys.stderr)
    raise SystemExit(code)


def request(url: str, *, data: bytes | None = None, headers: dict[str, str], method: str = "GET") -> tuple[int, str]:
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as res:
            body = res.read().decode("utf-8", errors="replace")
            return res.status, body
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return exc.code, body


def access_token() -> str:
    # reltio_ui client_credentials has no tenant. Password grant is required to PUT L3.
    if USERNAME and PASSWORD:
        if not CLIENT_ID or not CLIENT_SECRET:
            fail("Password grant also needs secrets RELTIO_CLIENT_ID and RELTIO_CLIENT_SECRET.")
        payload = urllib.parse.urlencode(
            {
                "grant_type": "password",
                "username": USERNAME,
                "password": PASSWORD,
            }
        ).encode()
        basic = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
        headers = {
            "Authorization": f"Basic {basic}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
    elif CLIENT_ID and CLIENT_SECRET:
        payload = urllib.parse.urlencode(
            {
                "grant_type": "client_credentials",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
            }
        ).encode()
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
    else:
        fail("Set GitHub secrets RELTIO_USERNAME + RELTIO_PASSWORD (and RELTIO_CLIENT_ID + RELTIO_CLIENT_SECRET).")

    status, body = request(AUTH_URL, data=payload, headers=headers, method="POST")
    if status >= 300:
        fail(f"Auth failed HTTP {status}: {body[:500]}")
    try:
        token = json.loads(body).get("access_token")
    except json.JSONDecodeError:
        fail(f"Auth response was not JSON: {body[:300]}")
    if not token:
        fail("Auth response had no access_token")
    return token


def main() -> None:
    if not ENVIRONMENT or not TENANT:
        fail("Set GitHub variables RELTIO_ENVIRONMENT (e.g. tst-01) and RELTIO_TENANT.")
    if not os.path.isfile(CONFIG_PATH):
        fail(f"Config file not found: {CONFIG_PATH}")

    with open(CONFIG_PATH, "rb") as fh:
        config_bytes = fh.read()
    try:
        json.loads(config_bytes)
    except json.JSONDecodeError as exc:
        fail(f"{CONFIG_PATH} is not valid JSON: {exc}")

    url = f"https://{ENVIRONMENT}.reltio.com/reltio/api/{urllib.parse.quote(TENANT)}/configuration"
    print(f"Applying {CONFIG_PATH} -> {url}")
    token = access_token()
    status, body = request(
        url,
        data=config_bytes,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="PUT",
    )
    if status >= 300:
        fail(f"PUT configuration failed HTTP {status}: {body[:1500]}")
    print(f"Tenant {TENANT} updated (HTTP {status}).")


if __name__ == "__main__":
    main()
