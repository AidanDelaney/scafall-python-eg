# Scafall Example

This project is an example scaffolding project.  It generates a trivial python application and demonstrates how to use `prompts.toml`.  If you would like to try it first install `scafall`:

```bash
$ go install github.com/AidanDelaney/scafall@latest
```

Then use this scaffolding to generate a new project:

```bash
$ scafall http://github.com/AidanDelaney/scafall-python-eg.git
✔ Please input a project name: pyexample
Use the arrow keys to navigate: ↓ ↑ → ←
? Which Python version to use:
  ▸ python3.10
    python3.9
    python3.8
How many digits of Pi to render: 3
$ cd pyexample
$ ./print_pi.py
```

You should be prompted for some values.  Follow the prompts and you will find the example project generated in a `project-pi` directory.