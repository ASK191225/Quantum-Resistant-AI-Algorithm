"""
Intentional insecure sinks for CodeQL → Arx ingest proof.
NOT production crypto. Do not call from demo entrypoints.
Each function is a known CodeQL Python security pattern.
"""

import hashlib
import os
import pickle
import subprocess


def run_user_command(user_input: str) -> None:
    # CODEQL: py/command-line-injection
    os.system("ping " + user_input)


def load_untrusted_blob(blob: bytes):
    # CODEQL: py/unsafe-deserialization
    return pickle.loads(blob)


def weak_password_hash(password: str) -> str:
    # CODEQL: py/weak-sensitive-data-hashing (or similar MD5 use)
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def shell_true(cmd: str) -> str:
    # CODEQL: py/command-line-injection via shell=True
    return subprocess.check_output(cmd, shell=True, text=True)
