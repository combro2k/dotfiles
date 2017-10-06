#!/usr/bin/env sh

BASE=$(dirname $(readlink -f ${0}))

cd ${BASE}

git clean -f -d -x
