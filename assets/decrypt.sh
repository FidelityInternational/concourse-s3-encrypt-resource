#!/bin/sh

file=$1
gpg --yes --no-use-agent --batch --passphrase='${encryption_key}' -d "'${file} -o ${file%.gpg}
