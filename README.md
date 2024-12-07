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
#### Running the test generators:
Running the grammarinator generator, must be done from in the same folder that the grammar and generator class are in
```bash
grammarinator-generate urlGenerator.urlGenerator --sys-path /Users/brooke_s/grammarinator-custom-generator/URL/url_grammarinator_files -r url -d 10 -n 5
```

Running the custom generator, must be done from the folder that myUrlGenerator is in.

Just running the below command as is will generate 10 tests of depth 10 due to the driver code at the bottom of the file:
```bash
python3 myUrlGenerator.py
```

##### TO GENERATE MORE TESTS/PASS IN DIFFERENT PARAMETERS:
Make an instance of the myURL() class, and call the generate generateURL() method:

```python
URL = myURL()
URL.generateURL(
    #number of tests,
    #depth,
    #other params...
    )
```

#### Testing:

To check the coverage, you must go to the file and choose which generator's tests to run the coverage tests on:
```python
#for custom generator:
custom_tests = testsToList("/Users/brooke_s/grammarinator-custom-generator/url/custom_url_files/tests")
#for grammarinator:
custom_tests = testsToList("/Users/brooke_s/grammarinator-custom-generator/url/url_grammarinator_files/tests")
```
Leave the line of the test suite you want uncommented, and comment out the other.

```bash
coverage run url_coverage_script.py
```

To test timing, each generator has its own file inside the associated folder. 

To time the custom generator, you can call time_function from a different file or you can run custom_timer.py:

```bash
python3 custom_timer.py
```
As is, this will test and plot how long it takes to generate 10,000 tests with depth 20.

To run timing for Grammarinator, you can call timing_grammarinator
```bash
python3 timing_grammarinator.py
```

Right now it runs the same test as for custom, with depth 20. You can change depth and the range of number of tests by altering lines 21 and 19 respectively.

#### Validity
Finally, to check the validity of the tests that are currently generated, run urlValidator. This will evaluate any tests currently in the tests folders for both generators and print the invalid URLs. 

##### Note that this requires django since it relies on a django validator

```bash
python3 urlValidator.py
```
### AWS ARN Generator
