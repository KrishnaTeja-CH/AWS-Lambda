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