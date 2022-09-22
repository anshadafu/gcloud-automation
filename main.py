from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import base64
from pprint import pprint

credentials = GoogleCredentials.get_application_default()
service = discovery.build('sqladmin', 'v1beta4', credentials=credentials, cache_discovery=False)
project = '<your-project-id>

def start_stop(event, context):
  print(event)
  pubsub_message = base64.b64decode(event['data']).decode('utf-8')
  print(pubsub_message)
  command, instance_name = pubsub_message.split(' ', 1)

  if command == 'start':
    start(instance_name)
  elif command == 'stop':
    stop(instance_name)
  elif command == 'restart':
    restart(instance_name)    
  else:
    print("unknown command " + command)

def start(instance_name):
  print("starting " + instance_name)
  patch(instance_name, "ALWAYS")

def stop(instance_name):
  print("stopping " + instance_name)
  patch(instance_name, "NEVER")


def patch(instance, activation_policy):
  request = service.instances().get(project=project, instance=instance)
  response = request.execute()

  dbinstancebody = {
    "settings": {
      "settingsVersion": response["settings"]["settingsVersion"],
      "activationPolicy": activation_policy
    }
  }

  request = service.instances().patch(
    project=project,
    instance=instance,
    body=dbinstancebody)
  response = request.execute()
  pprint(response)

def restart(instance_name):
  print("restarting " + instance_name)
  request = service.instances().restart(project=project, instance=instance_name)
  response = request.execute()
  pprint(response)
