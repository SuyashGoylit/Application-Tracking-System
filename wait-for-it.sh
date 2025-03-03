#!/usr/bin/env bash
# Wait for PostgreSQL to be ready

set -e

host="$1"
port="$2"
shift 2
cmd="$@"

echo "Waiting for PostgreSQL to be ready..."

until nc -z "$host" "$port"; do
  sleep 1
done

echo "PostgreSQL is up - executing command"
exec $cmd