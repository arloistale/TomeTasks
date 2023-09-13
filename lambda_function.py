import time
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

graphql_endpoint = 'https://tome-backend.fly.dev/graphql'

def handler(event, context):
    max_retries = 3
    retry_delay = 5

    response = None
    message = None

    for retry_count in range(max_retries):
      try: 
          response = requests.post(graphql_endpoint, json = { 'query': mutation }, headers = { 'Content-Type': 'application/json', })

          if response.status_code == 200:
              message = response.json()
              break
          else:
              message = "GraphQL request failed."
              print(f"{message} Retrying in {retry_delay} seconds...")
      except Exception as e:
          message = f"Exception occurred: {str(e)}."
          print(f"{message} Retrying in {retry_delay} seconds...")

      if retry_count < max_retries - 1:
          time.sleep(retry_delay)

    result = {
        'status_code': response.status_code if response is not None else "?",
        'message:': message
    }

    print("Attempted to present daily aphorism:", result)

    return result