#!/bin/sh -e

file="${1}"
encryption_key="${2}"
gpg --yes --batch --passphrase="${encryption_key}" -o "${file%.gpg}" -d "${file}"
