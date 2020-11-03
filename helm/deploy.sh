#!/usr/bin/env bash

set -e
set -x


TAG=$1
DEBUG=$2
REALEASE_NAME="monitoring"
COMMAND="install"

[[ -z "${TAG}" ]] && { echo "Error: value not found in TAG"; exit 1; }
[[ -z "${AWS_ACCESS_KEY_ID}" ]] && { echo "Error: value not found in AWS_ACCESS_KEY_ID"; exit 1; }
[[ -z "${AWS_SECRET_ACCESS_KEY}" ]] && { echo "Error: value not found in AWS_SECRET_ACCESS_KEY"; exit 1; }


if [ $(helm list | awk '{print $1}' | tail -1) == ${REALEASE_NAME} ];then
  COMMAND="upgrade"
fi

helm ${COMMAND} ${REALEASE_NAME} . --version ${TAG} \
                                   --wait \
                                   --set aws_access_key_id="${AWS_ACCESS_KEY_ID}" \
                                   --set aws_secret_access_key="${AWS_SECRET_ACCESS_KEY}" \
                                   "${@: 2}"