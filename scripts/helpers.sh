#!/usr/bin/env bash
# Manual helper commands migrated from the old Makefile.
# Usage: scripts/helpers.sh <command>

set -euo pipefail

cmd_check_ws() {
	git grep -E "\s$" -- 'src/**.py' || true
}

cmd_check_quotes() {
	git grep "'" -- 'src/**.py' || true
}

cmd_check_mode() {
	find src -name "*.py" -and -type f -and -not -perm 0644
}

cmd_check_has_key() {
	git grep -l "has_key" -- 'src/**.py' || true
}

cmd_check_no_future() {
	git grep "__future__" -- 'src/**.py' || true
}

cmd_check_files() {
	find src \
		-type f \
		-not -name "*.py" \
		-not -name "*.external_py" \
		-not -name "*.pyo" \
		-not -name "*.pyc" \
		-not -name "*.txt" \
		-not -name "Makefile" \
		-not -name "*.cfg" \
		-not -name "*.ini" \
		-not -name "*.py.not" \
		-not -name "*.stamp"
}

cmd_check_all() {
	cmd_check_ws
	cmd_check_quotes
	cmd_check_mode
	cmd_check_has_key
	cmd_check_no_future
}

cmd_fix_mode() {
	find src -type f -and -not -perm 644 -exec chmod 644 {} \+
}

cmd_todo() {
	git grep @TODO -- ':!/Makefile' ':!scripts/helpers.sh'
}

cmd_stats() {
	find out -name "*.syntax" 2>/dev/null | wc -l
	find out -name "*.lint" 2>/dev/null | wc -l
	find out -name "*.mypy" 2>/dev/null | wc -l
}

cmd_show_shbang() {
	find src -name "*.py" -exec head -1 {} \; | grep "#!" | sort | uniq
}

cmd_clean() {
	rsconstruct clean
}

cmd_clean_hard() {
	git clean -qffxd
}

cmd_remove_stamp() {
	find . -type f -and -name "*.stamp" -delete
}

cmd_spell_many() {
	mapfile -t md_src < <(find src -type f -and -name "*.md")
	aspell_many.sh "${md_src[@]}"
}

usage() {
	cat <<EOF
Usage: $0 <command>

Available commands:
  check_ws           Find trailing whitespace in src/**.py
  check_quotes       Find single quotes in src/**.py
  check_mode         Find src/**.py files not mode 0644
  check_has_key      Find files using has_key in src/**.py
  check_no_future    Find files using __future__ in src/**.py
  check_files        Find unexpected non-.py files under src/
  check_all          Run check_ws, check_quotes, check_mode, check_has_key, check_no_future
  fix_mode           chmod 644 on src/** files not at 644
  todo               Find @TODO markers across the tree
  stats              Count .syntax / .lint / .mypy artifacts under out/
  show_shbang        List unique shebangs across src/**.py
  clean              Remove build artifacts (delegates to rsconstruct clean)
  clean_hard         git clean -qffxd
  remove_stamp       Delete all *.stamp files in the tree
  spell_many         Run aspell_many.sh over src/**.md
EOF
}

main() {
	if [[ $# -lt 1 ]]; then
		usage
		exit 1
	fi
	local cmd="$1"
	shift
	if ! declare -F "cmd_$cmd" >/dev/null; then
		echo "unknown command: $cmd" >&2
		usage
		exit 1
	fi
	"cmd_$cmd" "$@"
}

main "$@"
