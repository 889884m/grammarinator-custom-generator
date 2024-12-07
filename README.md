# Grammarinator Custom Generator

## Setup

First install dependencies:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


## Running

### IPv6 Generator

Evaluation:

```sh
python3 ipv6/ipv6_eval.py --help
```

A\* Simulation:

1. Install FFmpeg.
2. Install LaTeX.
3. Install dependencies and run:

```sh
git clone https://github.com/3b1b/manim.git
cd manim
pip install -r requirements.txt
cd -
manimgl ipv6/astar_sim.py
```


### URL Generator


### AWS ARN Generator
