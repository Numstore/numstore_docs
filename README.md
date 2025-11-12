# Numstore Documentation

A Vue.js documentation website built with Vite and TailwindCSS.

## 🐳 Quick Start with Docker (Recommended)

The easiest way to run this website is using Docker. Just run:

```bash
docker-compose up -d
```

The website will be available at: http://localhost:8080

### Docker Commands

**Start the container:**
```bash
docker-compose up -d
```

**Stop the container:**
```bash
docker-compose down
```

**Rebuild after changes:**
```bash
docker-compose up -d --build
```

**View logs:**
```bash
docker-compose logs -f
```

### Using Docker directly (without docker-compose)

**Build the image:**
```bash
docker build -t numstore-docs .
```

**Run the container:**
```bash
docker run -d -p 8080:80 --name numstore-docs numstore-docs
```

**Stop the container:**
```bash
docker stop numstore-docs
docker rm numstore-docs
```

## 🛠️ Local Development

If you want to develop locally without Docker:

### Prerequisites
- Node.js 20+
- npm

### Setup

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

The dev server will start at http://localhost:5173

### Build for production

```bash
# Build the project
npm run build

# Preview the production build
npm run preview
```

## 📁 Project Structure

```
.
├── src/              # Vue.js source files
├── public/           # Static assets
├── scripts/          # Build scripts
├── Dockerfile        # Docker build configuration
├── docker-compose.yml # Docker compose setup
├── nginx.conf        # Nginx server configuration
└── vite.config.ts    # Vite configuration
```

## 🔧 Configuration

The nginx configuration includes:
- Gzip compression for better performance
- Security headers
- SPA routing support for Vue Router
- Static asset caching
- No-cache policy for index.html

You can modify `nginx.conf` to customize the server behavior.

## 📝 Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run gendocs` - Generate documentation
- `npm run lint` - Lint and fix code
- `npm run format` - Format code with Prettier

## 🚀 Deployment

The Docker container is production-ready and can be deployed to any platform that supports Docker:
- Docker Swarm
- Kubernetes
- AWS ECS
- Google Cloud Run
- Azure Container Instances
- DigitalOcean App Platform
- And more...

Simply push the image to a container registry and deploy!
