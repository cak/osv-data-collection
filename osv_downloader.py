import requests
import zipfile
import os
from pathlib import Path


def create_directory(path: str) -> None:
    """
    Create a directory if it doesn't exist.
    """
    Path(path).mkdir(parents=True, exist_ok=True)
    print(f"Directory ensured: {path}")


def download_file(url: str, local_path: str) -> None:
    """
    Download a file from the specified URL to a local path.
    """
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(local_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Downloaded: {local_path}")


def extract_zip(zip_path: str, extract_to: str) -> None:
    """
    Extract a ZIP file to the specified directory and remove the ZIP file.
    """
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(zip_path)
    print(f"Extracted to: {extract_to} and removed temporary ZIP file.")


def download_and_extract_osv(ecosystem: str, base_dir: str = "./data") -> None:
    """
    Download and extract OSV data for a given ecosystem.
    """
    output_dir = Path(base_dir) / ecosystem
    create_directory(output_dir)

    url = f"https://osv-vulnerabilities.storage.googleapis.com/{ecosystem}/all.zip"
    local_zip = output_dir / "all.zip"

    download_file(url, local_zip)
    extract_zip(local_zip, output_dir)


if __name__ == "__main__":
    base_data_dir = "./data"

    ecosystems = [
        "PyPI",  # Python packages
        "npm",  # JavaScript/Node.js packages
        "crates.io",  # Rust packages
        "Go",  # Go modules
        "RubyGems",  # Ruby packages
        "Maven",  # Java packages
        "NuGet",  # .NET packages
        "Packagist",  # PHP packages
        "Hex",  # Elixir/Erlang packages
        "Pub",  # Dart packages
        "CRAN",  # R packages (CRAN)
    ]

    create_directory(base_data_dir)

    for ecosystem in ecosystems:
        try:
            download_and_extract_osv(ecosystem, base_data_dir)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {ecosystem}: {e}")
        except zipfile.BadZipFile as e:
            print(f"Error extracting {ecosystem}: {e}")
        except Exception as e:
            print(f"Unexpected error for {ecosystem}: {e}")
