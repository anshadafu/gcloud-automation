# gcloud-automation

Python code for automate Start/Stop/Restart the Cloud SQL at user given time

For this automation we are using following Google Services 
   - Cloud Pub/Sub
   - Cloud Function
   - Cloud scheduler

   A simple workflow would be to create a scheduler that will get triggered at a specified time. This will publish a message to subscribed Pub/Sub topic and that message will be pulled by Cloud Function. Cloud Function will excute and start/stop/restart Cloud SQL as per given pub/sub message

1. Create a pub/sub topic which will be used to trigger the cloud function.
2. Create the cloud function and copy the python code .
3. Make sure to set the correct project ID in line 8.
4. Set the trigger to Pub/Sub and choose the topic created in step 1.
5. Create a cloud scheduler job to trigger the cloud function on a regular basis.
   Choose the frequency when you want the cloud function to be triggered.
   Set the target to Pub/Sub and define the topic created in step 1.
   The payload should be set to start [CloudSQL instance name] or stop [CloudSQL instance name] or restart [CloudSQL instance name] to start, stop or restart the specified instance (e.g. start my_cloudsql_instance will start the CloudSQL instance with the name my_cloudsql_instance)


   Reference : https://cloud.google.com/sql/docs/mysql/start-stop-restart-instance#rest-v1beta4_2
               https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/restart
               https://cloud.google.com/scheduler/docs/tut-pub-sub