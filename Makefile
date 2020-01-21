include .makefile.inc

.PHONY: help
help: ##  List all available commands.
	${SHOW_IDENTITY}
	@echo 'Usage:'
	@echo '${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@perl -ne "$${HELP_SCRIPT}" $(MAKEFILE_LIST)

.PHONY: tests
tests: ##  Run the unit tests against the project.
	python -m unittest discover -s tests/
