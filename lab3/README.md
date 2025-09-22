# Lab 3

## Team Members
- Victor Gutierrez (USC ID: 9841169875)
- Angie Vasquez (USC ID: 5537473368)

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?
RESTful APIs are scalabe since they are stateless and close connections with clients when requests are completed. This allows APIs to perform many requests from thousands of different clients without maintaining a heavy overhead. 

Question 2: According to the definition of "resources" provided in the AWS article above, What are the resources the mail server is providing to clients?
The resources provided by the mail server are messages in text that are formatted as JSON objects. The server can provide a user with a list of received mail including information regarding the sender, subject of the email, the content, and an ID associated with the email.

Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?
One common REST method mentioned in the AWS article is a PUT method that allows for updating existing data. The mail server could use this method by implementing a feature to allow senders to change the content of sent mail (ideally before the receiver has read it). 

Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!
API keys are used to authenticate users and provide unique IDs for each user. This ensures that clients accessing the API are authorized to use it and their usage can be tracked for monetization purposes. They also allow for the ability to limit access to the API, ensuring that there isn't too much traffic going to it. 
Site used for reference: https://cloud.google.com/endpoints/docs/openapi/when-why-api-key

“Why and When to Use API Keys | Cloud Endpoints with OpenAPI.” Google
    Cloud, cloud.google.com/endpoints/docs/openapi/when-why-api-key.  

