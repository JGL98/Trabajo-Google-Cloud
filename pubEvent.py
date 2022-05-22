import time
from google.cloud import pubsub_v1


publisher = pubsub_v1.PublisherClient()

f = open("events.csv","r")

project_id="glowing-bird-345011"

while True:
    line = f.readline()
    if not line:
        break


    sleepingTime,topic,message = line.split(",")
    
    topic_path = publisher.topic_path(project_id,topic)

    sleepingTime = int(sleepingTime)
    message = message.replace("\n","")
    message= message.encode("utf-8")
    topic=topic.encode("utf-8")

    print("Publishing a topic: '%s' with message: %s"%(topic,message))

# TODO PUB 
    future = publisher.publish(topic_path,topic + b";" +  message)
    print(future.result())
    print(f"Published messages to {topic}.")

    print("Waiting %i seconds"%sleepingTime)
    time.sleep(sleepingTime)

print("Done")

