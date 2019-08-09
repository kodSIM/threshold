"""Find and print critical values for CPU and memory usage for test."""
import sys

import click
import pandas as pd


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--cpu_limit', default=0.9, help='Percentile for CPU usage limit for test')
@click.option('--memory_limit', default=0.9, help='Percentile for memory usage limit for test')
def threshold(path, cpu_limit, memory_limit):
    """Find critical CPU and memory usage for test.

    :param str path: Path to log file.
    :param int cpu_limit: Percentile for CPU usage limit for test.
    :param int memory_limit: Percentile for memory usage limit for test.

    :return: Exit code. '0' if test have not crossed limits, '1' otherwise.
    :rtype: int
    """
    df = pd.read_csv(path)
    crit_cpu = df['cpu_process %'].quantile([0, cpu_limit])[cpu_limit]
    crit_mem = df['memory_process'].quantile([0, memory_limit])[memory_limit]
    anomal_cpu = df[df['cpu_process %'] > crit_cpu]
    anomal_mem = df[df['memory_process'] > crit_mem]
    if anomal_cpu.size or anomal_mem.size:
        print('Test is crossed of limits')
        print(pd.merge(anomal_cpu,
                       anomal_mem,
                       how='outer'))
        sys.exit(1)
    print('Test is success done')
    sys.exit(0)


if __name__ == '__main__':
    threshold()
