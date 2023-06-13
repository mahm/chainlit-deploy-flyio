# Deploy Chainlit Application to Fly.io Example

## Setup

### Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Python 3.10](https://www.python.org/downloads/)
- [Flyctl](https://fly.io/docs/getting-started/installing-flyctl/)
- [Poetry](https://python-poetry.org/docs/#installation)

### 1. Install Dependencies

```bash
poetry install
```

### 2. Configure Environment

```bash
cp .env.example .env
```

OPENAI_API_KEY is required to run the application. You can get one from [OpenAI](https://beta.openai.com/).

### 3. Run Application (Local)

```bash
docker-compose build
docker-compose up
````

## Deploy to Fly.io

### 1. Create a Fly.io App

```bash
fly apps create [app-name]
```

### 2. Set Fly.io Secrets

```bash
fly secrets set OPENAI_API_KEY=[your-openai-api-key] CHAINLIT_HOST=0.0.0.0 CHAINLIT_PORT=8080
```

### 3. Deploy to Fly.io

```bash
fly deploy
```
