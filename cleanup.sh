#!/usr/bin/env sh

BASE=$(dirname $(dirname $(readlink -f ${0})))

cd ${BASE}

git clean -f -d -x
