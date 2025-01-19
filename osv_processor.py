import json
from pathlib import Path
import csv


def save_osv_cves(cves: list[str], ecosystem: str):
    """
    Save a list of CVEs with a static ecosystem to a CSV file.
    """
    output_file = Path(f"./output/{ecosystem}-cves.csv")
    output_file.parent.mkdir(
        parents=True, exist_ok=True
    )  # Ensure output directory exists

    # Write to CSV
    with output_file.open(mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["cve", "ecosystem"])  # Write the header
        writer.writerows([[cve, ecosystem] for cve in cves])  # Write all rows at once

    print(f"Saved {len(cves)} CVEs to {output_file}")


def fetch_osv_data(ecosystem: str) -> list[str]:
    """
    Fetch CVEs from OSV data for a given ecosystem.
    """
    folder_path = Path(f"./data/{ecosystem}")
    if not folder_path.exists():
        print(f"Folder does not exist: {folder_path}")
        return []

    # List all JSON files in the folder
    osv_files = [file for file in folder_path.glob("*.json")]

    cves = set()  # Use a set for automatic deduplication

    for file_path in osv_files:
        with file_path.open("r") as f:
            data = json.load(f)

            # Check for CVE in `id`
            if data.get("id", "").startswith("CVE-"):
                cves.add(data["id"])

            # Check for CVEs in `aliases` and `related`
            for field in ("aliases", "related"):
                if field in data:
                    cves.update(
                        value for value in data[field] if value.startswith("CVE-")
                    )

    return list(cves)


if __name__ == "__main__":
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

    for ecosystem in ecosystems:
        cves = fetch_osv_data(ecosystem)
        if cves:
            save_osv_cves(cves=cves, ecosystem=ecosystem)
        else:
            print(f"No CVEs found for ecosystem: {ecosystem}")
