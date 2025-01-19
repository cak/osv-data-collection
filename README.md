# Open Source Vulnerability (OSV) Data Processor

This project provides tools to download and process vulnerability data from the [OSV database](https://osv.dev/). It supports multiple ecosystems to collect and save CVEs for open-source libraries and packages.

## Features

- Download and extract OSV vulnerability data for selected ecosystems.
- Process JSON files to extract CVE identifiers.
- Save CVEs to a CSV file with ecosystem metadata.
- Modular design for easy addition of new ecosystems.

## Requirements

- Python 3.11+
- The only required package is `requests`.

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies using `pip`:
   ```bash
   pip install requests
   ```
   
---

## Scripts Overview

### `osv_downloader.py`

**Purpose**: Download and extract OSV data for specified ecosystems.

#### Key Functions:
- **`create_directory`**: Ensures a directory exists.
- **`download_file`**: Downloads a ZIP file from a URL.
- **`extract_zip`**: Extracts a ZIP file and removes it after extraction.
- **`download_and_extract_osv`**: Combines the above steps to handle ecosystem-specific OSV data.

#### Usage:
```bash
python osv_downloader.py
```

#### Output:
- Data for each ecosystem is extracted into the `./data/{ecosystem}/` directory.

---

### `osv_processor.py`

**Purpose**: Process downloaded OSV JSON files to extract CVEs and save them to CSV files.

#### Key Functions:
- **`fetch_osv_data`**: Reads JSON files for a specific ecosystem and extracts CVE identifiers from `id`, `aliases`, and `related` fields.
- **`save_osv_cves`**: Saves the extracted CVEs and ecosystem information into a CSV file.

#### Usage:
```bash
python osv_processor.py
```

#### Output:
- A CSV file for each ecosystem is saved in the `./output/` directory. Example: `./output/PyPI-cves.csv`

---

## Supported Ecosystems

The following ecosystems are covered:
- PyPI (Python)
- npm (JavaScript/Node.js)
- crates.io (Rust)
- Go (Go modules)
- RubyGems (Ruby)
- Maven (Java)
- NuGet (.NET)
- Packagist (PHP)
- Hex (Elixir/Erlang)
- Pub (Dart)
- R (CRAN and Bioconductor)

### Adding New Ecosystems
To add a new ecosystem, include its name in the `ecosystems` list in both `osv_downloader.py` and `osv_processor.py`. The scripts will handle the rest automatically.

---

## Example Workflow

1. **Download OSV Data**:
   Run `osv_downloader.py` to fetch and extract data for all supported ecosystems.
   ```bash
   python osv_downloader.py
   ```

2. **Process Data**:
   Run `osv_processor.py` to extract CVEs and save them to CSV files.
   ```bash
   python osv_processor.py
   ```

3. **Check Output**:
   Extracted CVEs for each ecosystem will be saved in the `./output/` directory.

---

## Contributing

Feel free to submit issues or pull requests to improve this project. Contributions are welcome!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
