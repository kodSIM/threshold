# Threshold

Find and print critical values for CPU and memory usage for test.

## Install

For installation use `pip`:

    pip install .

## Usage

For run script use format:

    python threshold.py <path to log file> --cpu_limit <percentile for CPU limit> --memory_limit <percentile for memory limit>

or

    threshold <path to log file> --cpu_limit <percentile for CPU limit> --memory_limit <percentile for memory limit>