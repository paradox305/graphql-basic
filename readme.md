# GraphQL Geometry Engine Service

## Overview

This project is a **GraphQL Geometry Engine Service** implemented using **Flask** and **GraphQL**. The service provides various geometric operations on 3D geometry data, such as calculating bounding boxes, rotating meshes, translating meshes, and checking polygon convexity. This document provides information on how to set up, run, and test the service.

## Features

- **Bounding Box Calculation**: Calculate the smallest bounding box that contains a set of 3D points.
- **Mesh Rotation**: Rotate a 3D mesh around a specified axis by a given angle.
- **Mesh Translation**: Translate a 3D mesh by specified units along each axis.
- **Polygon Convexity Check**: Check whether a polygon in 3D space is convex.

## Prerequisites

- **Python 3.8+**
- **Flask**
- **Graphene** (GraphQL implementation for Python)
- **cURL** (for testing the GraphQL API)
- **Docker** (Optional for containerization)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd graphql-geometry-engine
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install Flask graphene
   ```

## Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. The GraphQL endpoint will be available at:
   ```
   http://localhost:5000/graphql
   ```

## GraphQL Queries

Below are the GraphQL queries that can be executed against the `/graphql` endpoint.

### 1. Bounding Box Calculation
**Description**: Calculate the smallest bounding box for a given set of 3D points.

**Example Query**:
```graphql
query {
  boundingBox(points: [{x: 1, y: 2, z: 0}, {x: 1, y: 1, z: 1}]) {
    minPoint
    maxPoint
  }
}
```

### 2. Mesh Rotation
**Description**: Rotate a 3D mesh around a specified axis by a given angle.

**Example Query**:
```graphql
query {
  rotatedMesh(mesh: [{x: 1, y: 0, z: 0}], angle: 90, axis: "Z")
}
```

### 3. Mesh Translation
**Description**: Translate a 3D mesh by specified units along each axis.

**Example Query**:
```graphql
query {
  movedMesh(mesh: [{x: 1, y: 1, z: 1}], x: 2, y: 2, z: 2)
}
```

### 4. Polygon Convexity Check
**Description**: Check whether a given 3D polygon is convex.

**Example Query**:
```graphql
query {
  isConvex(points: [{x: 0, y: 0, z: 0}, {x: 1, y: 0, z: 0}, {x: 0, y: 1, z: 0}])
}
```

## Testing with cURL

Below are the cURL commands that can be used to test the GraphQL queries.

### 1. Bounding Box Query
```bash
curl -X POST http://localhost:5000/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { boundingBox(points: [{x: 1, y: 2, z: 0}, {x: 1, y: 1, z: 1}]) { minPoint maxPoint } }"}'
```

### 2. Rotated Mesh Query
```bash
curl -X POST http://localhost:5000/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { rotatedMesh(mesh: [{x: 1, y: 0, z: 0}], angle: 90, axis: \"Z\") }"}'
```

### 3. Moved Mesh Query
```bash
curl -X POST http://localhost:5000/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { movedMesh(mesh: [{x: 1, y: 1, z: 1}], x: 2, y: 2, z: 2) }"}'
```

### 4. Polygon Convexity Check Query
```bash
curl -X POST http://localhost:5000/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { isConvex(points: [{x: 0, y: 0, z: 0}, {x: 1, y: 0, z: 0}, {x: 0, y: 1, z: 0}]) }"}'
```

## Dockerization (Optional)

To run the service using Docker:

1. Build the Docker image:
   ```bash
   docker build -t geometry-engine .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 geometry-engine
   ```

3. Pull a prebuilt image from Docker Hub:
   ```bash
    docker pull codecraftme/graphql-basic:latest
   ```

## Running Tests

This project includes a set of unit tests to validate the geometric calculations.

1. Run the tests:
   ```bash
   python test.py
   ```

## Project Structure

- **app.py**: The main Flask application.
- **schema.py**: Contains GraphQL schema and resolver functions.
- **geometry.py**: Contains the geometric calculation functions.
- **test_geometry.py**: Unit tests for the geometric functions.

## Contribution

Feel free to open issues and submit pull requests if you want to improve or contribute to the project.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

