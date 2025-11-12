# Numstore Documentation Site - Setup Guide

This guide explains the new documentation and release management system.

## Overview

The site now uses:
1. **Single HTML file for documentation** - Renders Sphinx-generated docs in an iframe
2. **Auto-detected releases** - Automatically scans and displays releases from the file system

## Documentation System

### Location
- Main documentation HTML: `public/docs/index.html`

### How it Works
1. Place your Sphinx-generated single-page HTML at `public/docs/index.html`
2. The Vue app (`ResourcesDocumentation.vue`) loads and displays it in an iframe
3. No Vue components needed for docs content

### Generating Sphinx Single-Page HTML

To generate a single HTML file from Sphinx documentation:

```bash
cd /path/to/sphinx/docs
sphinx-build -b singlehtml source/ build/singlehtml/
cp build/singlehtml/index.html /path/to/numstore_docs/public/docs/
```

Or use the Makefile:
```bash
make singlehtml
```

### Current Setup
- A placeholder HTML file exists at `public/docs/index.html`
- Replace it with your actual Sphinx-generated documentation

## Release Management System

### Directory Structure

```
public/releases/
├── {version}/
│   ├── library/          # Library files (.so, .a, .h, etc.)
│   ├── docs/             # Version-specific documentation
│   └── artifacts/        # CLI tools, examples, etc.
└── README.md
```

### Example Structure

```
public/releases/
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
│   │   └── libnumstore.so
│   ├── docs/
│   │   └── index.html
│   └── artifacts/
└── 1.1.0/
    ├── library/
    │   └── libnumstore.so
    ├── docs/
    │   └── index.html
    └── artifacts/
```

### Auto-Detection

The system automatically detects releases by:
1. Scanning `public/releases/` for version directories
2. Cataloging all files in `library/`, `docs/`, and `artifacts/` subdirectories
3. Generating `public/releases.json` manifest

### Adding a New Release

1. **Create the release directory:**
   ```bash
   mkdir -p public/releases/x.y.z/{library,docs,artifacts}
   ```

2. **Add your files:**
   ```bash
   # Library files
   cp libnumstore.so public/releases/x.y.z/library/
   cp numstore.h public/releases/x.y.z/library/

   # Documentation
   cp docs/index.html public/releases/x.y.z/docs/

   # Artifacts
   cp numstore-cli public/releases/x.y.z/artifacts/
   ```

3. **Regenerate the manifest:**
   ```bash
   npm run scan-releases
   ```

4. **Rebuild and deploy:**
   ```bash
   npm run build
   ```

### Automatic Scanning

The `scan-releases` script runs automatically:
- Before `npm run dev` (via `predev` hook)
- Before `npm run build` (via `prebuild` hook)

You can also run it manually:
```bash
npm run scan-releases
```

### Release Manifest

The `public/releases.json` file contains:
- List of all releases (sorted newest first)
- All files for each release
- File metadata (size, modification time, path)

Example:
```json
{
  "generated_at": "2025-11-12T21:22:10.504350",
  "total_releases": 3,
  "latest_version": "1.1.0",
  "releases": [
    {
      "version": "1.1.0",
      "library": [...],
      "docs": [...],
      "artifacts": [...]
    }
  ]
}
```

### Vue Components

Two components use the manifest:

1. **Current.vue** (`/downloads/current`)
   - Displays the latest release
   - Shows library, docs, and artifacts sections
   - Links to download each file

2. **Archive.vue** (`/downloads/archive`)
   - Lists all releases (newest first)
   - Expandable sections for each version
   - Full file listings for each release

## Docker Setup

The site includes Docker support for easy deployment:

```bash
# Start with docker-compose
docker-compose up -d

# Access at http://localhost:8080
```

The Docker container:
- Builds the Vue app with Node.js
- Serves static files with nginx
- Includes all releases and documentation

## Development Workflow

### Local Development

```bash
# Install dependencies
npm install

# Start dev server (auto-scans releases)
npm run dev
```

### Adding Documentation

1. Generate Sphinx single-page HTML
2. Copy to `public/docs/index.html`
3. Rebuild: `npm run build`

### Adding Releases

1. Create version directory: `mkdir -p public/releases/x.y.z/{library,docs,artifacts}`
2. Add files to subdirectories
3. Scan releases: `npm run scan-releases`
4. Test locally: `npm run dev`
5. Commit and deploy

### Production Build

```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

## Migration from Old System

### Removed
- `scripts/generate_docs.py` - No longer needed
- `src/views/resources/autogen/` - All Vue doc components removed
- `src/views/resources/docs_outline.txt` - No longer needed
- `package.json` scripts: `gendocs`, `predev:gendocs`, `prebuild:gendocs`

### Added
- `public/docs/index.html` - Single HTML documentation file
- `public/releases/` - Release directory structure
- `public/releases.json` - Auto-generated manifest
- `scripts/scan_releases.py` - Release scanner script
- Updated `Current.vue` and `Archive.vue` components

### Updated
- `ResourcesDocumentation.vue` - Now loads HTML file
- `package.json` - New `scan-releases` script

## File Type Guidelines

### Library Directory
- Shared libraries: `.so` (Linux), `.dll` (Windows), `.dylib` (macOS)
- Static libraries: `.a` (Unix), `.lib` (Windows)
- Header files: `.h`, `.hpp`
- Python packages: `.whl`
- Java archives: `.jar`
- Package files: `.deb`, `.rpm`, `.pkg`

### Docs Directory
- HTML documentation: `index.html` (from Sphinx singlehtml)
- PDF documentation: `manual.pdf`
- Man pages: `.1`, `.3`, etc.
- Plain text: `README.txt`, `CHANGELOG.txt`

### Artifacts Directory
- Command-line tools: `numstore-cli`
- Example code: `examples.tar.gz`, `examples.zip`
- Configuration files: `numstore.conf.example`
- Database schemas: `schema.sql`
- Additional utilities

## Troubleshooting

### Releases not showing up
1. Ensure directory structure is correct: `{version}/{library,docs,artifacts}/`
2. Run `npm run scan-releases` manually
3. Check `public/releases.json` was generated
4. Restart dev server

### Documentation not loading
1. Verify file exists at `public/docs/index.html`
2. Check browser console for errors
3. Ensure HTML is valid and self-contained
4. Check that all resources (CSS, images) are embedded or use relative paths

### Docker build fails
1. Ensure all placeholder files are present
2. Check that `public/releases.json` exists
3. Run `npm run scan-releases` before building
4. Check Docker logs: `docker-compose logs`

## Best Practices

1. **Versioning**: Use semantic versioning (x.y.z)
2. **Complete Releases**: Include library, docs, and relevant artifacts for each release
3. **Documentation**: Keep version-specific docs in `releases/{version}/docs/`
4. **File Sizes**: Keep files reasonably sized; consider compression
5. **Testing**: Test releases locally before deploying
6. **Manifest**: Always run `scan-releases` after adding/modifying releases

## Future Enhancements

Potential improvements:
- Checksums (SHA256) for downloads
- Release notes/changelog integration
- Download statistics
- Multi-platform builds (Linux, macOS, Windows) per release
- API endpoint for release manifest
- Search within releases
