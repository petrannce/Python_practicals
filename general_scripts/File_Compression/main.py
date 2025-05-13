import gzip
import shutil

def compress_file(input_file, output_file):
    """
    Compress a file using gzip compression.

    :param input_file_path: Path to the input file to be compressed.
    :param output_file_path: Path where the compressed file will be saved.
    """
    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

# Example usage
if __name__ == "__main__":
    input_file = 'example.txt'  # Replace with your input file path
    output_file = 'example.txt.gz'  # Replace with your desired output file path

    compress_file(input_file, output_file)
    print(f"Compressed {input_file} to {output_file}")