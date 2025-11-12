# Downloads Guide

## Overview

The website now has downloadable release files for all versions. These are currently text files simulating real archives for testing purposes.

## Available Downloads

### Version 1.1.0 (Latest)

**Library Files:**
- `numstore-1.1.0-linux-x64.tar.gz` (1.0 KB) - Linux x86_64 distribution
- `numstore-1.1.0-windows-x64.zip` (1.1 KB) - Windows x86_64 distribution
- `numstore-1.1.0-macos-arm64.tar.gz` (1.2 KB) - macOS Apple Silicon distribution
- `libnumstore.so` (77 bytes) - Placeholder shared library

**Artifacts:**
- `numstore-examples.tar.gz` (987 bytes) - Example code with new 1.1.0 features
- `numstore-python-1.1.0-py3-none-any.whl` (825 bytes) - Python bindings package

**Documentation:**
- `index.html` (228 bytes) - Version-specific documentation

### Version 1.0.1

**Library Files:**
- `numstore-1.0.1-linux-x64.tar.gz` (896 bytes) - Linux x86_64 bugfix release
- `numstore-1.0.1-windows-x64.zip` (973 bytes) - Windows x86_64 bugfix release
- `libnumstore.so` (77 bytes) - Placeholder shared library

**Documentation:**
- `index.html` (228 bytes) - Version-specific documentation

### Version 1.0.0

**Library Files:**
- `numstore-1.0.0-linux-x64.tar.gz` (627 bytes) - Linux x86_64 distribution
- `numstore-1.0.0-windows-x64.zip` (703 bytes) - Windows x86_64 distribution
- `numstore-1.0.0-macos-arm64.tar.gz` (745 bytes) - macOS Apple Silicon distribution
- `libnumstore.so` (70 bytes) - Placeholder shared library
- `numstore.h` (360 bytes) - C header file

**Artifacts:**
- `numstore-examples.tar.gz` (647 bytes) - Example code
- `numstore-cli` (110 bytes) - Command-line interface

**Documentation:**
- `index.html` (228 bytes) - Version-specific documentation

## Testing Downloads

### From Development Server

1. Start the dev server:
   ```bash
   npm run dev
   ```

2. Navigate to downloads pages:
   - **Current Release**: http://localhost:5173/downloads/current
   - **All Releases**: http://localhost:5173/downloads/archive

3. Click any download link to download the file

### From Production Build

1. Build the site:
   ```bash
   npm run build
   ```

2. Preview production build:
   ```bash
   npm run preview
   ```

3. Navigate to downloads pages and test

### From Docker

1. Build and run container:
   ```bash
   docker-compose up -d
   ```

2. Access site at http://localhost:8080

3. Navigate to downloads pages:
   - **Current Release**: http://localhost:8080/downloads/current
   - **All Releases**: http://localhost:8080/downloads/archive

4. Test downloads

## File Contents

All files are currently text files with simulated content:

- **Linux tarballs (.tar.gz)**: Installation instructions for Linux
- **Windows zips (.zip)**: Installation instructions for Windows
- **macOS tarballs (.tar.gz)**: Installation instructions for macOS
- **Python wheels (.whl)**: Python package information
- **Examples (.tar.gz)**: Example code descriptions

When you view the downloaded files, you'll see:
- Version information
- Platform details
- Installation instructions
- Release notes (for 1.0.1 and 1.1.0)
- Feature descriptions

## Replacing with Real Files

To replace these test files with real releases:

1. **Build your actual releases** (libraries, binaries, packages)

2. **Place files in the correct directories**:
   ```bash
   # For version x.y.z:
   cp your-real-file.tar.gz public/releases/x.y.z/library/
   cp your-real-examples.tar.gz public/releases/x.y.z/artifacts/
   cp your-real-docs.html public/releases/x.y.z/docs/
   ```

3. **Regenerate the manifest**:
   ```bash
   npm run scan-releases
   ```

4. **Rebuild**:
   ```bash
   npm run build
   ```

The website will automatically detect and serve the new files!

## File Naming Conventions

Follow these naming patterns for consistency:

### Library Files
- Linux: `numstore-{version}-linux-{arch}.tar.gz`
- Windows: `numstore-{version}-windows-{arch}.zip`
- macOS: `numstore-{version}-macos-{arch}.tar.gz`

Examples:
- `numstore-1.1.0-linux-x64.tar.gz`
- `numstore-1.1.0-windows-x64.zip`
- `numstore-1.1.0-macos-arm64.tar.gz`

### Artifacts
- Examples: `numstore-examples.tar.gz` or `numstore-examples-{version}.tar.gz`
- Python wheels: `numstore-python-{version}-py3-none-any.whl`
- CLI tools: `numstore-cli` or `numstore-cli-{version}`

### Documentation
- Usually: `index.html` (single-page documentation)
- Or: `manual-{version}.pdf`, `docs-{version}.tar.gz`

## Download Page Features

### Current Release Page
- Shows only the latest version (1.1.0)
- Organized into sections: Library, Documentation, Artifacts
- File sizes displayed
- Direct download links

### Archive Page
- Shows all releases, newest first
- Latest version marked with green "(Latest)" badge
- Each release has collapsible sections
- File sizes displayed for all files
- Direct download links

## Technical Details

### How Downloads Work

1. Files are stored in `public/releases/{version}/{category}/`
2. `scan_releases.py` generates `public/releases.json` manifest
3. Vue components fetch the manifest on page load
4. Download links point to `/releases/{version}/{category}/{filename}`
5. Browser downloads files directly from the public directory

### MIME Types

The server should serve these files with appropriate MIME types:
- `.tar.gz` → `application/gzip`
- `.zip` → `application/zip`
- `.whl` → `application/zip`
- `.so` → `application/octet-stream`
- `.dll` → `application/octet-stream`
- `.h` → `text/plain`

Vite and nginx handle this automatically.

### Download Verification

For production releases, consider adding:
- SHA256 checksums: `{filename}.sha256`
- GPG signatures: `{filename}.asc`
- Release notes: `RELEASE_NOTES.md`

Add these files to the same directory and they'll be auto-detected!

## Troubleshooting

### Downloads not appearing
1. Check files exist in `public/releases/{version}/`
2. Run `npm run scan-releases` to regenerate manifest
3. Verify `public/releases.json` contains the files
4. Restart dev server

### Download links broken
1. Check file paths in `releases.json` are correct
2. Ensure files are in `public/` directory (not `src/`)
3. Verify no typos in filenames
4. Check browser console for 404 errors

### Files download with wrong name
- Ensure filename matches what's in the directory
- Check no special characters in filenames
- Use kebab-case or snake_case naming

## Summary

✅ **11 downloadable files** across 3 releases
✅ **Automatic detection** via scan script
✅ **Dynamic display** on Current and Archive pages
✅ **Direct downloads** from browser
✅ **Easy to replace** with real release files

Just drop real files in the directories, run `npm run scan-releases`, and rebuild!
