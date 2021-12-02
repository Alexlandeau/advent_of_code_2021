SHELL:=/bin/bash
.SHELLFLAGS += -e

.ONESHELL:
new_day:
	@set -e
	@echo "Starting to build day $(day)..."
	@mkdir day_$(day)
	@session=$(<session.txt) && curl https://adventofcode.com/2021/day/$(day)/input -o day_$(day)/input.txt --cookie "session=$session"
	@touch day_$(day)/day_$(day).py

	
