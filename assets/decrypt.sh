#!/bin/sh -e

set -x

file="${1}"
encryption_key="${2}"
gpg --yes --no-use-agent --batch --passphrase="${encryption_key}" -o "${file%.gpg}" -d "${file}" 
