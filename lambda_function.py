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
graphql_endpoint = 'https://tome-backend.fly.dev/graphql'

# Define the headers (if needed)
headers = {
    'Content-Type': 'application/json',
    # Add any other headers as required (e.g., authentication headers)
}

# Create a dictionary for the GraphQL request payload
data = {
    'query': mutation
}

def handler(event, context):
    response = requests.post(graphql_endpoint, json=data, headers=headers)

    message = response.json() if response.status_code == 200 else f"GraphQL request failed."

    result = {
        'status_code': response.status_code,
        'message:': message
    }

    print("Attempted to present daily aphorism:", result)

    return result