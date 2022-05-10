##############
# parameters #
##############
# do you want to check python syntax?
DO_SYNTAX:=0
# do you want to lint python files?
DO_LINT:=0
# do you want to lint python files using flake8?
DO_FLAKE8:=1
# do dependency on the makefile itself?
DO_ALLDEP:=0
# do you want to see the commands given?
DO_MKDBG:=1

########
# code #
########
ALL:=
ifeq (, $(shell which git))
ALL_PY:=$(shell find src -name "*.py")
else
ALL_PY:=$(shell git ls-files 'src/*.py')
endif # shell which git
ALL_SYNTAX:=$(addprefix out/,$(addsuffix .syntax, $(basename $(ALL_PY))))
ALL_LINT:=$(addprefix out/,$(addsuffix .lint, $(basename $(ALL_PY))))
ALL_FLAKE8:=$(addprefix out/,$(addsuffix .flake8, $(basename $(ALL_PY))))

ifeq ($(DO_SYNTAX),1)
ALL+=$(ALL_SYNTAX)
endif # DO_SYNTAX

ifeq ($(DO_LINT),1)
ALL+=$(ALL_LINT)
endif # DO_LINT

ifeq ($(DO_FLAKE8),1)
ALL+=$(ALL_FLAKE8)
endif # DO_FLAKE8

ifeq ($(DO_ALLDEP),1)
.EXTRA_PREREQS+=$(foreach mk, ${MAKEFILE_LIST},$(abspath ${mk}))
endif # DO_ALLDEP

ifeq ($(DO_MKDBG),1)
Q=
# we are not silent in this branch
else # DO_MKDBG
Q=@
#.SILENT:
endif # DO_MKDBG

#########
# rules #
#########
.PHONY: all
all: $(ALL)
	@true

.PHONY: syntax
syntax: $(ALL_SYNTAX)

.PHONY: lint
lint: $(ALL_LINT)

.PHONY: flake8
flake8: $(ALL_FLAKE8)

.PHONY: check_all
check_all: check_ws

.PHONY: check
check: check_ws check_has_key check_no_python2 check_mode

.PHONY: all_lint
all_lint:
	$(info doing [$@])
	$(Q)shopt -s globstar; pymakehelper error_on_print python -m pylint --reports=n --score=n src/**/*.py

.PHONY: all_flake8
all_flake8:
	$(info doing [$@])
	$(Q)pymakehelper error_on_print flake8 src

.PHONY: check_ws
check_ws:
	$(info doing [$@])
	$(Q)git grep -E "\s$$" -- '*.py' || exit 0

# this is a bad check because returning tuples in python is perfectly legit
.PHONY: check_return
check_return:
	$(info doing [$@])
	$(Q)git grep -l -E "return\(.*\)$$" -- '*.py' || exit 0
	$(Q)git grep -l -E "return \(.*\)$$" -- '*.py' || exit 0

# this is a bad check because comparing tuples in python is perfectly legit
.PHONY: check_if
check_if:
	$(info doing [$@])
	$(Q)git grep -l -E "if \(" -- '*.py' || exit 0
	$(Q)git grep -l -E "if\(" -- '*.py' || exit 0

.PHONY: check_has_key
check_has_key:
	$(info doing [$@])
	$(Q)git grep -l "has_key" -- '*.py' || exit 0

.PHONY: check_no_python2
check_no_python2:
	$(info doing [$@])
	$(Q)git grep -E "^#!/usr/bin/python2" || exit 0

.PHONY: check_no_future
check_no_future:
	$(info doing [$@])
	$(Q)git grep "__future__" || exit 0

.PHONY: debug
debug:
	$(info ALL_PY is $(ALL_PY))
	$(info ALL_SYNTAX is $(ALL_SYNTAX))
	$(info ALL_LINT is $(ALL_LINT))
	$(info ALL_FLAKE8 is $(ALL_FLAKE8))
	$(info ALL is $(ALL))

.PHONY: show_shbang
show_shbang:
	$(Q)find src -name "*.py" -exec head -1 {} \; | grep "#!" | sort | uniq

.PHONY: todo
todo:
	$(Q)git grep @TODO -- ':!/Makefile'

.PHONY: remove_stamp
remove_stamp:
	$(Q)find . -type f -and -name "*.stamp" -delete

.PHONY: clean
clean:
	$(Q)rm -f $(ALL)
#	$(Q)find . -not -path "./.venv/*" -and -name "__pycache__" -and -type d -exec rm -r {} \;
#	$(Q)find . -not -path "./.venv/*" -name "*.pyc" -or -name "*.pyo" -delete

.PHONY: clean_hard
clean_hard:
	$(Q)git clean -qffxd

.PHONY: clean_syntax
clean_syntax:
	$(Q)rm -f $(ALL_SYNTAX)

.PHONY: clean_lint
clean_lint:
	$(Q)rm -f $(ALL_LINT)

.PHONY: clean_flake8
clean_flake8:
	$(Q)rm -f $(ALL_FLAKE8)

.PHONY: check_mode
check_mode:
	$(info doing [$@])
	$(Q)find src -name "*.py" -and -type f -and -not -perm 0644

.PHONY: stats
stats:
	$(Q)find out -name "*.syntax" | wc -l
	$(Q)find out -name "*.lint" | wc -l
	$(Q)find out -name "*.flake8" | wc -l

.PHONY: fix_mode
fix_mode:
	$(info doing [$@])
	$(Q)find src -type f -and -not -perm 644 -exec chmod 644 {} \+

.PHONY: check_files
check_files:
	$(info doing [$@])
	$(Q)find src\
		-type f\
		-not -name "*.py"\
		-not -name "*.external_py"\
		-not -name "*.external_py"\
		-not -name "*.pyo"\
		-not -name "*.pyc"\
		-not -name "*.txt"\
		-not -name "Makefile"\
		-not -name "*.cfg"\
		-not -name "*.ini"\
		-not -name "*.py.not"\
		-not -name "*.stamp"

############
# patterns #
############
$(ALL_SYNTAX): out/%.syntax: %.py scripts/syntax_check.py
	$(info doing [$@])
	$(Q)pymakehelper error_on_print scripts/syntax_check.py $<
	$(Q)pymakehelper touch_mkdir $@
$(ALL_LINT): out/%.lint: %.py
	$(info doing [$@])
	$(Q)pymakehelper error_on_print python -m pylint --reports=n --score=n $<
	$(Q)pymakehelper touch_mkdir $@
$(ALL_FLAKE8): out/%.flake8: %.py
	$(info doing [$@])
	$(Q)flake8 --version
	$(Q)which flake8
	$(Q)echo ${PYTHONWARNINGS}
	$(Q)pymakehelper error_on_print flake8 $<
	$(Q)pymakehelper touch_mkdir $@
