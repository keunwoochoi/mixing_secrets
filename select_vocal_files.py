# run this code the project root
import json

with open('zip_contents.txt', 'r') as f:
    lines = f.readlines()

lines = ''.join(lines).split('Filename:')
lines = [l for l in lines if l != '']

fns = {}
for i, line in enumerate(lines):
    song_name = line.split('\n')[0].strip()
    fns[song_name] = [l.strip() for l in line.split('\n') if '__MACOS' not in l]

voc_fns = {}
non_voc_at_all_zips = {}


def vocal_name_detector(filename):
    filename = filename.split('/')[-1]  # remove the folder name

    if 'voc' in filename.lower() or 'vox' in filename.lower():
        return True
    return False


for key, val in fns.items():
    val = [v for v in val if v.lower().endswith('.wav')]
    voc_fns_here = [v for v in val if vocal_name_detector(v)]  # it ignores choir on purpose
    if voc_fns_here == []:
        non_voc_at_all_zips[key] = val
    else:
        voc_fns[key] = voc_fns_here


with open('filenames_vocal.json', 'w') as outfile:
    json.dump(voc_fns, outfile, indent=4)

with open('filenames_non_vocal_songs.json', 'w') as outfile:
    json.dump(non_voc_at_all_zips, outfile, indent=4)

