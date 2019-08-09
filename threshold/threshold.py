"""Find and print critical values for CPU and memory usage for test."""
import sys

import click
import pandas as pd


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--cpu_limit', default=45, help='CPU usage limit for test')
@click.option('--memory_limit', default=10453370, help='Memory usage limit for test')
def threshold(path, cpu_limit, memory_limit):
    """Find critical CPU and memory usage for test.

    :param str path: Path to log file.
    :param int cpu_limit: CPU usage limit for test.
    :param int memory_limit: Memory usage limit for test.

    :return: Exit code. '0' if test have not crossed limits, '1' otherwise.
    :rtype: int
    """
    df = pd.read_csv(path)
    crit_cpu = df['timestamp'][df['cpu_process %'] > cpu_limit]
    crit_mem = df['timestamp'][df['memory_process'] > memory_limit]
    if crit_cpu.size or crit_mem.size:
        print('Test is crossed of limits')
        print(pd.merge(df[df['timestamp'].isin(crit_cpu)],
                       df[df['timestamp'].isin(crit_mem)],
                       how='outer'))
        sys.exit(1)
    print('Test is success done')
    sys.exit(0)


if __name__ == '__main__':
    threshold()
