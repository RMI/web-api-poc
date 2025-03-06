FROM python:3.12.6

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN uv sync --frozen --no-install-project

# Sync the project
RUN uv sync --frozen

# Command to run the app when the container starts
CMD ["uv", "run", "src/main.py"]
