"""This script loads file names of vocal stems from `filenames_vocal.json`.
It unzips and moves them into a single directory.
"""
import os
import json
import tqdm
import shutil
import zipfile
import argparse
import tempfile

json_path = 'filenames_vocal.json'


def main(source_path, target_path):
    with open(json_path, 'r') as f:
        data = json.load(f)  # zip filename: list of member paths

    # validate if there's no same file name because we'll flatten it
    # filepaths = []
    # for _, members in data.items():
    #     filepaths.extend([f.split('/')[-1] for f in members])
    #
    # assert len(set(filepaths)) == len(filepaths)
    # ..ok there are overlapping names, so..  i'll need to be more careful as below.

    os.makedirs(target_path, exist_ok=True)

    temp_dir = tempfile.TemporaryDirectory()

    for zip_fn, subpaths in tqdm.tqdm(data.items(), total=len(data)):
        with zipfile.ZipFile(os.path.join(source_path, zip_fn)) as zip_ref:
            for subpath in subpaths:
                zip_ref.extract(subpath, temp_dir.name)
                new_filename = subpath.replace('/', '-')
                shutil.move(os.path.join(temp_dir.name, subpath), os.path.join(target_path, new_filename))

    temp_dir.cleanup()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_path', type=str, required=True, help='path that has all the zip files.')
    parser.add_argument('--target_path', type=str, required=True, help='path to decompress the vocal stem wavs.')

    args = parser.parse_args()

    main(args.source_path, args.target_path)
