import csv
from pathlib import Path
from uuid import UUID, uuid4
import pytoml as toml

def uuid_is_valid(uuid):
    """Checks that given string has valid UUID format"""
    try:
        UUID(uuid)
        return True
    except ValueError:
        return False

"""
def main():
    p = Path('.')
    dot_rmotr_files = p.glob('**/.rmotr')
    modified = []
    for dot_rmotr in dot_rmotr_files:
        with dot_rmotr.open('r') as fp:
            obj = toml.load(fp)
        if not uuid_is_valid(obj['uuid']):
            old = obj['uuid']
            new = uuid4()
            obj['uuid'] = str(new)
            modified.append((old, new))
            with dot_rmotr.open('w') as fp:
                fp.write(toml.dumps(obj))

    with open('modified_uuids.csv', 'w') as fp:
        writer = csv.writer(fp)
        for old, new in modified:
            writer.writerow([str(old), str(new)])
"""
def main():
    p = Path('.')
    dot_rmotr_files = p.glob('**/.rmotr')
    modified = []
    for dot_rmotr in dot_rmotr_files:
        with dot_rmotr.open('r') as fp:
            obj = toml.load(fp)
        if not uuid_is_valid(obj['uuid']):
            raise ValueError("{} not valid".format(obj['uuid']))


if __name__ == '__main__':
    main()
