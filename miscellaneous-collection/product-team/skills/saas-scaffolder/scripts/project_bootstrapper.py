#!/usr/bin/env python3
"""Project Bootstrapper — Generate SaaS project scaffolding from config.

Creates project directory structure with boilerplate files, README,
docker-compose, environment configs, and CI/CD templates.

Usage:
    python project_bootstrapper.py config.json --output-dir ./my-project
    python project_bootstrapper.py config.json --format json --dry-run
"""

import argparse
import json
import os
import sys
from typing import Dict, List, Any, Optional
from datetime import datetime


STACK_TEMPLATES = {
    "nextjs": {
        "package.json": lambda c: json.dumps({
            "name": c["name"],
            "version": "0.1.0",
            "private": True,
            "scripts": {
                "dev": "next dev",
                "build": "next build",
                "start": "next start",
                "lint": "next lint",
                "test": "jest",
                "test:watch": "jest --watch"
            },
            "dependencies": {
                "next": "^14.0.0",
                "react": "^18.0.0",
                "react-dom": "^18.0.0"
            },
            "devDependencies": {
                "typescript": "^5.0.0",
                "@types/react": "^18.0.0",
                "@types/node": "^20.0.0",
                "eslint": "^8.0.0",
                "eslint-config-next": "^14.0.0"
            }
        }, indent=2),
        "tsconfig.json": lambda c: json.dumps({
            "compilerOptions": {
                "target": "es5",
                "lib": ["dom", "dom.iterable", "esnext"],
                "allowJs": True,
                "skipLibCheck": True,
                "strict": True,
                "forceConsistentCasingInFileNames": True,
                "noEmit": True,
                "esModuleInterop": True,
                "module": "esnext",
                "moduleResolution": "bundler",
                "resolveJsonModule": True,
                "isolatedModules": True,
                "jsx": "preserve",
                "incremental": True,
                "paths": {"@/*": ["./src/*"]}
            },
            "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
            "exclude": ["node_modules"]
        }, indent=2),
        "dirs": ["src/app", "src/components", "src/lib", "src/styles", "public", "tests"],
        "files": {
            "src/app/layout.tsx": "export default function RootLayout({ children }: { children: React.ReactNode }) {\n  return <html lang=\"en\"><body>{children}</body></html>;\n}\n",
            "src/app/page.tsx": "export default function Home() {\n  return <main><h1>Welcome</h1></main>;\n}\n",
        }
    },
    "express": {
        "package.json": lambda c: json.dumps({
            "name": c["name"],
            "version": "0.1.0",
            "main": "src/index.ts",
            "scripts": {
                "dev": "tsx watch src/index.ts",
                "build": "tsc",
                "start": "node dist/index.js",
                "test": "jest",
                "lint": "eslint src/"
            },
            "dependencies": {
                "express": "^4.18.0",
                "cors": "^2.8.5",
                "helmet": "^7.0.0",
                "dotenv": "^16.0.0"
            },
            "devDependencies": {
                "typescript": "^5.0.0",
                "@types/express": "^4.17.0",
                "@types/cors": "^2.8.0",
                "@types/node": "^20.0.0",
                "tsx": "^4.0.0",
                "jest": "^29.0.0",
                "@types/jest": "^29.0.0",
                "eslint": "^8.0.0"
            }
        }, indent=2),
        "dirs": ["src/routes", "src/middleware", "src/models", "src/services", "src/utils", "tests"],
        "files": {
            "src/index.ts": "import express from 'express';\nimport cors from 'cors';\nimport helmet from 'helmet';\nimport { config } from 'dotenv';\n\nconfig();\n\nconst app = express();\nconst PORT = process.env.PORT || 3000;\n\napp.use(helmet());\napp.use(cors());\napp.use(express.json());\n\napp.get('/health', (req, res) => res.json({ status: 'ok' }));\n\napp.listen(PORT, () => console.log(`Server running on port ${PORT}`));\n",
        }
    },
    "fastapi": {
        "requirements.txt": lambda c: "fastapi>=0.100.0\nuvicorn[standard]>=0.23.0\npydantic>=2.0.0\npython-dotenv>=1.0.0\nsqlalchemy>=2.0.0\nalembic>=1.12.0\npytest>=7.0.0\nhttpx>=0.24.0\n",
        "dirs": ["app/api", "app/models", "app/services", "app/core", "tests", "alembic"],
        "files": {
            "app/__init__.py": "",
            "app/main.py": "from fastapi import FastAPI\nfrom app.core.config import settings\n\napp = FastAPI(title=settings.PROJECT_NAME)\n\n@app.get('/health')\ndef health(): return {'status': 'ok'}\n",
            "app/core/__init__.py": "",
            "app/core/config.py": "from pydantic_settings import BaseSettings\n\nclass Settings(BaseSettings):\n    PROJECT_NAME: str = 'API'\n    DATABASE_URL: str = 'sqlite:///./app.db'\n    class Config:\n        env_file = '.env'\n\nsettings = Settings()\n",
        }
    }
}


def generate_readme(config: Dict[str, Any]) -> str:
    """Generate README.md content."""
    name = config.get("name", "my-project")
    desc = config.get("description", "A SaaS application")
    stack = config.get("stack", "nextjs")

    return f"""# {name}

{desc}

## Tech Stack

- **Framework**: {stack}
- **Database**: {config.get('database', 'PostgreSQL')}
- **Auth**: {config.get('auth', 'JWT')}

## Getting Started

### Prerequisites

- Node.js 18+ / Python 3.11+
- Docker & Docker Compose

### Development

```bash
# Clone the repo
git clone <repo-url>
cd {name}

# Copy environment variables
cp .env.example .env

# Start with Docker
docker compose up -d

# Or run locally
{'npm install && npm run dev' if stack in ('nextjs', 'express') else 'pip install -r requirements.txt && uvicorn app.main:app --reload'}
```

### Testing

```bash
{'npm test' if stack in ('nextjs', 'express') else 'pytest'}
```

## Project Structure

```
{name}/
├── {'src/' if stack in ('nextjs', 'express') else 'app/'}
├── tests/
├── docker-compose.yml
├── .env.example
└── README.md
```

