import argparse
from typing import Optional, Sequence

import yaml


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        with open(filename) as data:
            loaded = yaml.safe_load(data)
            content = yaml.safe_dump(loaded, sort_keys=False)
            sorted_content = yaml.safe_dump(loaded)
            if content != sorted_content:
                with open(filename, 'w') as file:
                    yaml.safe_dump(loaded, file)

                retval = 1

    return retval


if __name__ == '__main__':
    exit(main())
