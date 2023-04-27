"""Download samples and eval data"""
import argparse
import os
import yaml
import gdown
import zipfile
from tqdm import tqdm


def download_file(url, folder_path, file_name):
    """Download file from Google Drive"""
    output_path = os.path.join(folder_path, file_name)
    gdown.download(url, output_path, quiet=False, fuzzy=True)


def main():
    """Main function that perform the download"""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--parameters_file",
        type=str,
        required=True,
        help="File containing parameters for the download",
    )
    parser.add_argument(
        "--output_path", type=str, required=True, help="Path where data will be stored",
    )
    args = parser.parse_args()

    with open(args.parameters_file, "r") as f:
        params = yaml.full_load(f)

    output_path = args.output_path
    dataset_url = params["dataset_url"]
    file_name = "dataperf-vision-selection-resources.zip"

    download_file(dataset_url, output_path, file_name)
    FILEID=1vcahjqKEosjnHzxAgr5fDUf7RTWKGU39
    FILENAME=file.zip
    download_cmd = "wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://docs.google.com/uc?export=download&id=${FILEID}" -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=${FILEID}" -O $FILENAME && rm -rf /tmp/cookies.txt"
    print("filename being downloaded is", file_name)

    with zipfile.ZipFile(os.path.join(output_path, file_name)) as zf:
        for member in tqdm(zf.infolist(), desc="Extracting "):
            try:
                zf.extract(member, output_path)
            except zipfile.error as e:
                print(e)


if __name__ == "__main__":
    main()
