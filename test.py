# Documentation and Test Script for GraphQL Queries using cURL

# This Python script provides a documentation file for testing GraphQL endpoints
# with cURL commands. Each cURL command corresponds to a different operation 
# in the GraphQL Geometry Engine API.

import os
import subprocess

# Replace the URL below with the appropriate GraphQL endpoint URL
GRAPHQL_ENDPOINT = "http://localhost:5000/graphql"

# Documentation and cURL Commands for GraphQL Queries
# 1. Bounding Box Query
bounding_box_query = '''
curl -X POST {endpoint} \
  -H "Content-Type: application/json" \
  -d '{{"query": "query {{ boundingBox(points: [{{x: 1, y: 2, z: 0}}, {{x: 1, y: 1, z: 1}}]) {{ minPoint maxPoint }} }}"}}'
'''.format(endpoint=GRAPHQL_ENDPOINT)

# 2. Rotated Mesh Query
rotated_mesh_query = '''
curl -X POST {endpoint} \
  -H "Content-Type: application/json" \
  -d '{{"query": "query {{ rotatedMesh(mesh: [{{x: 1, y: 0, z: 0}}], angle: 90, axis: \"Z\") }}"}}'
'''.format(endpoint=GRAPHQL_ENDPOINT)

# 3. Moved Mesh Query
moved_mesh_query = '''
curl -X POST {endpoint} \
  -H "Content-Type: application/json" \
  -d '{{"query": "query {{ movedMesh(mesh: [{{x: 1, y: 1, z: 1}}], x: 2, y: 2, z: 2) }}"}}'
'''.format(endpoint=GRAPHQL_ENDPOINT)

# 4. Polygon Convexity Check Query
is_convex_query = '''
curl -X POST {endpoint} \
  -H "Content-Type: application/json" \
  -d '{{"query": "query {{ isConvex(points: [{{x: 0, y: 0, z: 0}}, {{x: 1, y: 0, z: 0}}, {{x: 0, y: 1, z: 0}}]) }}"}}'
'''.format(endpoint=GRAPHQL_ENDPOINT)

# Function to print documentation with cURL commands
def print_documentation():
    print("# Documentation for GraphQL Queries using cURL\n")
    print("### 1. Bounding Box Query\n")
    print(bounding_box_query)
    print("\n### 2. Rotated Mesh Query\n")
    print(rotated_mesh_query)
    print("\n### 3. Moved Mesh Query\n")
    print(moved_mesh_query)
    print("\n### 4. Polygon Convexity Check Query\n")
    print(is_convex_query)

# Function to execute cURL commands and print their output
def execute_curl(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}\n{e.stderr.decode('utf-8')}")

# Execute the function to output the documentation and execute each cURL command
if __name__ == "__main__":
    print_documentation()
    
    print("\n### Executing cURL Commands:\n")
    print("\n--- Bounding Box Query ---\n")
    execute_curl(bounding_box_query)
    
    print("\n--- Rotated Mesh Query ---\n")
    execute_curl(rotated_mesh_query)
    
    print("\n--- Moved Mesh Query ---\n")
    execute_curl(moved_mesh_query)
    
    print("\n--- Polygon Convexity Check Query ---\n")
    execute_curl(is_convex_query)
