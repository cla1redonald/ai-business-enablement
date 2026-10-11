.PHONY: demo test

# Run the whole toolchain against the synthetic Caldergate fixture.
demo:
	./demo.sh

# The checker's own self-test: every rule must fire on its poison and stay silent on
# its clean fixture before anything is graded.
test:
	python3 tools/check.py --self-test
