import random
def random_task():
    eat = ["Pizza","Burger", "Nachos", "Rice","Tacos"]
    return random.choice(eat)

if __name__ == "__main__":
    print(f"You should eat some {random_task()}")



## Code in Lambda
import json
import random 

def random_task():
    eat = ["Pizza","Burger", "Nachos", "Rice","Tacos"]
    return random.choice(eat)

def lambda_handler(event, context):
    eat = random_task()
    message = (f"You should eat: {eat}")
    return {
        'statusCode': 200,
        'body': json.dumps({"message": message,"eat": eat})
    }



'''
Setup Instructions

Create a Lambda Function:
- Log in to the AWS Management Console.
- Navigate to the Lambda service.
- Click Create function.
- Choose Author from scratch.
- Provide a function name (e.g., RandomFoodSuggestion).
- Choose a runtime (e.g., Python 3.x).
- Click Create function.

Add the Code:
- In the Lambda function console, scroll down to the Function code section.
- Replace the default code with the provided AWS Lambda handler code.
- Click Deploy to save your changes.

Set Up API Gateway Trigger:
- In the Lambda function page, navigate to the Configuration tab.
- Under Triggers, click Add trigger.
- Select API Gateway from the dropdown.
- Choose Create an API.
- Select REST API and configure it with default settings.
- Click Add to create the API Gateway trigger.

Test the API:
- After creating the API Gateway trigger, you will see an API endpoint URL.
- You can test the API using curl from the terminal. Replace <API_ENDPOINT_URL> with your actual API endpoint:

curl <API_ENDPOINT_URL>

You should receive a response in JSON format, for example:

{
    "message": "You should eat: Pizza",
    "eat": "Pizza"
}
    
    ''' 
