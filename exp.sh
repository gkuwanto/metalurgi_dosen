#!/bin/bash
while IFS="=" read -r key value; do
    declare $key=$value
    export "$key"
done < .env