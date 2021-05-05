Building and Installing locally
-------------------------------

[cd into project directory]
``poetry build``

[install using pipx]
``pipx install dist/globus-mas-0.1.0.tar.gz --force``

OR

[cd out of project directory, so you're using your system's pip3]
``pip3 install /root/path/to/project/dist/globus_mas-0.1.0-py3-none-any.whl``


[install your shell's autocomplete]
``globus-mas --install-completion``
