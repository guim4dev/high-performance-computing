## Dependencies
For running this exercise you must have:
- python 3>
- gcc installed
- gfortran installed
- matplotlib and pandas installed

## Running
Simply do, inside the exercise1/ folder
```shell
$ python runner.py
```

Beware that the maximum value is hardcoded at the runner.py file with value = 42000, which means
you might have to change it according to your available memory.


To determine the maximum matrix dimension value (n), simply apply the following formula:

```math
2n + n^2 = available_bytes / 8
```

Edit the file, then Run!
