List the pre-commit hook file for git.

This pre-commit hook will using pylint to check errors in commited python files.
(If need check docs with Sphinx, Google or Numpy style, please add load-plugins=pylint.extensions.check_docs in MASTER of .pylintr, but I didn't add check doc warning in, please fill free to add your own checking conditions.)

In addition, check the rate of pylint return. If the commit have to finish, the rate has to larger than 5.0/10.

For pylint detail, please check [here](https://docs.pylint.org/index.html)

Need install pylint and glob2

```
pip install pylint glob2
```
