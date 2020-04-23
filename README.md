# CompilerLocalJudge

A simple judge script for correctness check.

Please make sure that `python3` and `ravel` are available in PATH.

### Usage

The first step is to edit the testing directory and the shell commands for compiling, runing with `llc`, and running with `ravel`.

Then execute:

```shell
python3 batch.py args...
```

This will test all `.mx` files under the directory set in the script except for the ones in `args`.

For example, `python3 batch.py t2 t65` will ignore `t2.mx` and `t65.mx`.

Further customizing can be made by simply editing the script.

