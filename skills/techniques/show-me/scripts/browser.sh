#!/bin/sh

usage() {
  printf '%s\n' 'Usage: browser.sh [--host HOST] [--port PORT] ABSOLUTE_DIRECTORY

Serve Markdown files in ABSOLUTE_DIRECTORY with mdts in the foreground.

Options:
  --host HOST  Bind address (default: 127.0.0.1)
  --port PORT  TCP port from 1 to 65535 (default: 3000)
  -h, --help   Show this help

Requires a POSIX shell and Nix with flakes and nix-command enabled.
Supported Nix systems: aarch64-darwin, aarch64-linux, x86_64-linux.
The bundled flake supplies mdts without installing packages into a user profile.'
}

fail() {
  printf 'browser.sh: %s\n' "$1" >&2
  exit 2
}

host=127.0.0.1
port=3000
directory=

while [ "$#" -gt 0 ]; do
  case "$1" in
    --host)
      [ "$#" -ge 2 ] || fail "--host requires a value"
      host=$2
      shift 2
      ;;
    --port)
      [ "$#" -ge 2 ] || fail "--port requires a value"
      port=$2
      shift 2
      ;;
    -h|--help)
      [ "$#" -eq 1 ] || fail "--help cannot be combined with other arguments"
      usage
      exit 0
      ;;
    --)
      shift
      [ "$#" -eq 1 ] || fail "provide exactly one directory"
      [ -z "$directory" ] || fail "provide exactly one directory"
      directory=$1
      shift
      ;;
    -*)
      fail "unknown option: $1"
      ;;
    *)
      [ -z "$directory" ] || fail "provide exactly one directory"
      directory=$1
      shift
      ;;
  esac
done

[ -n "$directory" ] || fail "an absolute directory is required; see --help"
case "$directory" in
  /*) ;;
  *) fail "directory must be an absolute path" ;;
esac
[ -d "$directory" ] || fail "directory does not exist or is not a directory: $directory"

case "$host" in
  ''|*[!a-zA-Z0-9:._%-]*|-*) fail "invalid host: $host" ;;
esac
case "$host" in
  0.0.0.0|::|0:0:0:0:0:0:0:0) fail "wildcard bind addresses are not allowed" ;;
esac

case "$port" in
  ''|*[!0-9]*|0|0*) fail "port must be a decimal integer from 1 to 65535" ;;
esac
[ "${#port}" -le 5 ] || fail "port must be a decimal integer from 1 to 65535"
[ "$port" -le 65535 ] || fail "port must be a decimal integer from 1 to 65535"

absolute_directory=$(CDPATH= cd -P -- "$directory" && pwd -P) || fail "cannot resolve directory: $directory"
command -v nix >/dev/null 2>&1 || fail "Nix is required; install or enable it before running this helper"
case "$0" in
  */*) script_directory=${0%/*}; [ -n "$script_directory" ] || script_directory=/ ;;
  *)
    script_path=$(command -v "$0") || fail "cannot locate helper script"
    script_directory=${script_path%/*}
    ;;
esac
script_directory=$(CDPATH= cd -P -- "$script_directory" && pwd -P) || fail "cannot locate bundled flake"
# Encode flake-reference delimiters without requiring a host text processor.
unencoded_path=$script_directory
nix_flake_path=
while [ -n "$unencoded_path" ]; do
  remaining_path=${unencoded_path#?}
  character=${unencoded_path%"$remaining_path"}
  case "$character" in
    '%') character=%25 ;;
    ' ') character=%20 ;;
    '#') character=%23 ;;
    '?') character=%3F ;;
  esac
  nix_flake_path=$nix_flake_path$character
  unencoded_path=$remaining_path
done

printf 'Starting mdts on host %s, port %s for %s\n' "$host" "$port" "$absolute_directory" >&2
exec nix run --no-write-lock-file --no-update-lock-file "path:$nix_flake_path" -- "$absolute_directory" --host "$host" --port "$port" --no-open
