import argparse
import json


def read_binary_file(filepath):
    with open(filepath, "rb") as f:
        return f.read()


def get_differences(file1, file2):
    differences = []
    min_length = min(len(file1), len(file2))
    i = 0

    while i < min_length:
        if file1[i] != file2[i]:
            hex_address = f"0x{i:X}"
            entry_type = "char"
            length = 1

            if i + 1 < min_length and file1[i:i + 1] != file2[i:i + 1]:
                length = 2
                entry_type = "short"

            if i + 3 < min_length and file1[i:i + 2] != file2[i:i + 2]:
                length = 4
                entry_type = "word"

            if i + length > min_length:
                length = min_length - i
                if length <= 1:
                    length = 1
                    entry_type = "char"
                elif length <= 2:
                    length = 2
                    entry_type = "short"
                else:
                    length = 4
                    entry_type = "word"

            hex_value = "0x" + file2[i:i+length].hex().upper()

            differences.append({
                "type": entry_type,
                "address": hex_address,
                "value": hex_value
            })
            i += length
        else:
            i += 1

    return differences


def main():
    parser = argparse.ArgumentParser(description="Compare hex addresses of two binary files.")
    parser.add_argument("file1", help="Path to the first binary file")
    parser.add_argument("file2", help="Path to the second binary file")
    parser.add_argument("output", help="Path to save the differences JSON file")
    args = parser.parse_args()

    file1_data = read_binary_file(args.file1)
    file2_data = read_binary_file(args.file2)

    differences = get_differences(file1_data, file2_data)

    with open(args.output, "w") as f:
        json.dump(differences, f, indent=4)

    print(f"Differences saved to {args.output}")


if __name__ == "__main__":
    main()
