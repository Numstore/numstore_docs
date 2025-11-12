# Releases Directory Structure

This directory contains all Numstore releases with their associated files.

## Directory Structure

Each release follows this structure:

```
releases/
├── {version}/
│   ├── library/          # Library files (shared objects, static libs, headers)
│   ├── docs/             # Documentation HTML files
│   └── artifacts/        # Additional artifacts (binaries, tools, examples)
```

## Example Structure

```
releases/
├── 1.0.0/
│   ├── library/
│   │   ├── libnumstore.so
│   │   ├── libnumstore.a
│   │   └── numstore.h
│   ├── docs/
│   │   └── index.html
│   └── artifacts/
│       ├── numstore-cli
│       └── examples.tar.gz
├── 1.0.1/
│   ├── library/
│   ├── docs/
│   └── artifacts/
└── 1.1.0/
    ├── library/
    ├── docs/
    └── artifacts/
```

## Auto-Detection

The Vue application automatically detects all releases by scanning this directory structure.
Run `npm run scan-releases` to generate the `releases.json` manifest file.

## Adding a New Release

1. Create a new directory with the version number: `mkdir -p releases/x.y.z/{library,docs,artifacts}`
2. Add your release files to the appropriate subdirectories
3. Run `npm run scan-releases` to update the manifest
4. Rebuild the application

## File Types

### Library Directory
- Shared libraries (`.so`, `.dll`, `.dylib`)
- Static libraries (`.a`, `.lib`)
- Header files (`.h`, `.hpp`)
- Package files (`.deb`, `.rpm`)

### Docs Directory
- HTML documentation (Sphinx-generated single HTML or multi-page docs)
- PDF documentation
- Man pages

### Artifacts Directory
- Command-line tools
- Example code
- Configuration files
- Additional tools and utilities
