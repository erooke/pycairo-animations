.PHONY: format
format:
	black .
	isort anim examples
