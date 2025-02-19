This is a simple Python Script that compares two bin files and outputs the resulting differences in the target file as a json file in the same format as the Preset writes for the Randomizer.

Usage:
```
python diff.py <source_file> <target_file> <output_file>
```
Example:
```
python diff.py source.bin target.bin output.json
```

The resulting file will follow this format:
```json
[
    {
        "type": "word",
        "address": "0x491586E",
        "value": "0x00000000"
    },
    {
        "type": "word",
        "address": "0x4915872",
        "value": "0x00005102"
    },
    {
        "type": "word",
        "address": "0x491592E",
        "value": "0x00000000"
    }
]
```
