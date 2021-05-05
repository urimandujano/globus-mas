define HELPTEXT
Please use "make <target>" where <target> is one of:
    
    install:
        Install this project and its dependencies into a virtual 
        environment
    docs:
        Update CLI documentation
endef
export HELPTEXT

help:
	@echo "$$HELPTEXT"
	
install:
	poetry install

docs:
	poetry run typer globus_mas/cli/main.py utils docs --name "globus-mas" --output cli_reference.md; 
	pandoc --from markdown --to rst -o cli_reference.rst cli_reference.md; 
	rm cli_reference.md
