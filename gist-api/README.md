
# Github Gists API

This project provides a simple API to fetch GitHub user's public gists.  
It includes a Flask app, Dockerfile, and unit tests with mocked GitHub API calls.

## setup

###  Clone the Repository

```bash
git clone https://github.com/EqualExperts-Assignments/equal-experts-respectful-decorous-fierce-occasion-00018d3f967a.git
cd equal-experts-respectful-decorous-fierce-occasion-00018d3f967a
```
Make sure you are on the correct branch:

```bash
git checkout solution
```

Then cd  into the project folder:

```bash
cd gist-api
```

## Project Structure
- `app.py` — Main application code
- `tests/` — Contains unit test cases
- `Dockerfile` — Multi-stage build with non-root user
- `requirements.txt` — Python dependencies

## Build and Run with Docker

### 1. Build the Docker image

```bash
docker build -t gist-api .
```
### 2. Check available images

```bash
docker images
```
**Note:** The Dockerfile uses a multi-stage build and runs as a non-root user.

### 3. Run the container

```bash
docker run -d -p 8080:8080 gist-api
```

**If you see a port conflict error:**

```
docker: Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:8080
```

It means port 8080 is already in use on your host. Run the container on a different port:

```bash
docker run -d -p 8081:8080 gist-api
```
### 4. Verify running containers

```bash
docker ps
```
## Test the API

```bash
curl http://localhost:8080/octocat
```

You can also test in your browser: `http://localhost:8080/octocat`

## Run Unit Tests Locally

### 1. Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Run tests:

```bash
python -m pytest -v
```

The tests use mocked GitHub API responses for reliability.


## Notes
Dockerfile uses multi-stage build and runs as a non-root user.

Unit tests are located under the tests/ folder.

If port 8080 is busy, use another port mapping (e.g., 8081:8080).

