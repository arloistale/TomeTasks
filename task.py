import requests

# Define the GraphQL mutation
mutation = '''
mutation MyMutation {
  presentRandomAphorism {
    ... on PresentRandomAphorismSuccess {
      __typename
      aphorism {
        title
      }
    }
    ... on AphorismAlreadyPresentedError {
      __typename
      message
    }
  }
}
'''

# Define the GraphQL endpoint URL
graphql_endpoint = 'https://jtome-backend.onrender.com/graphql'

# Define the headers (if needed)
headers = {
    'Content-Type': 'application/json',
    # Add any other headers as required (e.g., authentication headers)
}

# Create a dictionary for the GraphQL request payload
data = {
    'query': mutation
}

print("Sending request to", graphql_endpoint,"...")

# Send the GraphQL request
response = requests.post(graphql_endpoint, json=data, headers=headers)

# Check for a successful response
if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"GraphQL request failed with status code {response.status_code}:")
    print(response.text)

