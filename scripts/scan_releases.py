#!/usr/bin/env python3
"""
Scan the public/releases/ directory and generate a releases.json manifest.

This script automatically detects all releases and their files, generating
a JSON manifest that the Vue app can use to display downloads.
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime

# Configuration
RELEASES_DIR = Path("public/releases")
OUTPUT_FILE = Path("public/releases.json")

def get_file_info(file_path: Path) -> Dict[str, Any]:
    """Get information about a file."""
    stat = file_path.stat()
    return {
        "name": file_path.name,
        "path": str(file_path.relative_to(Path("public"))),
        "size": stat.st_size,
        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat()
    }

def scan_release_directory(version_dir: Path) -> Dict[str, Any]:
    """Scan a single release directory and return its metadata."""
    version = version_dir.name

    release_data = {
        "version": version,
        "library": [],
        "docs": [],
        "artifacts": []
    }

    # Scan library directory
    library_dir = version_dir / "library"
    if library_dir.exists():
        for file_path in library_dir.iterdir():
            if file_path.is_file():
                release_data["library"].append(get_file_info(file_path))

    # Scan docs directory
    docs_dir = version_dir / "docs"
    if docs_dir.exists():
        for file_path in docs_dir.iterdir():
            if file_path.is_file():
                release_data["docs"].append(get_file_info(file_path))

    # Scan artifacts directory
    artifacts_dir = version_dir / "artifacts"
    if artifacts_dir.exists():
        for file_path in artifacts_dir.iterdir():
            if file_path.is_file():
                release_data["artifacts"].append(get_file_info(file_path))

    return release_data

def parse_version(version: str) -> tuple:
    """Parse a version string into a tuple for sorting."""
    try:
        parts = version.split('.')
        return tuple(int(p) for p in parts)
    except (ValueError, AttributeError):
        return (0, 0, 0)

def scan_all_releases() -> List[Dict[str, Any]]:
    """Scan all release directories and return a list of releases."""
    if not RELEASES_DIR.exists():
        print(f"Error: Releases directory not found: {RELEASES_DIR}")
        return []

    releases = []

    # Iterate through all directories in releases/
    for version_dir in RELEASES_DIR.iterdir():
        if version_dir.is_dir() and version_dir.name != "README.md":
            print(f"Scanning release: {version_dir.name}")
            release_data = scan_release_directory(version_dir)
            releases.append(release_data)

    # Sort releases by version (descending - newest first)
    releases.sort(key=lambda r: parse_version(r["version"]), reverse=True)

    return releases

def generate_manifest():
    """Generate the releases.json manifest file."""
    print(f"Scanning releases in: {RELEASES_DIR}")

    releases = scan_all_releases()

    if not releases:
        print("Warning: No releases found!")
        return

    # Create manifest
    manifest = {
        "generated_at": datetime.now().isoformat(),
        "total_releases": len(releases),
        "latest_version": releases[0]["version"] if releases else None,
        "releases": releases
    }

    # Write manifest
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Generated manifest: {OUTPUT_FILE}")
    print(f"  Total releases: {len(releases)}")
    print(f"  Latest version: {manifest['latest_version']}")

    # Print summary
    print("\nReleases found:")
    for release in releases:
        lib_count = len(release["library"])
        doc_count = len(release["docs"])
        art_count = len(release["artifacts"])
        print(f"  - {release['version']}: {lib_count} libraries, {doc_count} docs, {art_count} artifacts")

def main():
    try:
        generate_manifest()
    except Exception as e:
        print(f"Error generating manifest: {e}")
        import traceback
        traceback.print_exc()
        exit(1)

if __name__ == "__main__":
    main()
