
# Dining Concierge Chatbot

![AWS Logo](https://img.shields.io/badge/AWS-Cloud-yellow?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8-blue?style=flat-square)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

Dining Concierge Chatbot is a personalized restaurant recommendation system built on AWS. It leverages various AWS services to provide a scalable, serverless solution for real-time, customized dining suggestions.

## Features

- **Personalized Recommendations:** Utilizes user preferences and location to provide tailored restaurant suggestions.
- **Real-time Data Processing:** Integrates with AWS services for dynamic data handling and instant responses.
- **Scalable and Serverless:** Built with AWS Lambda, Lex, API Gateway, and DynamoDB, ensuring a scalable and efficient architecture.
- **Secure and Reliable:** Uses AWS SES for secure email communications and ElasticSearch for efficient data retrieval.

## Technologies Used

- **AWS Lex:** Natural language understanding and conversational interface.
- **AWS Lambda:** Serverless compute for handling backend logic.
- **API Gateway:** Secure API management and routing.
- **DynamoDB:** NoSQL database for fast and scalable data storage.
- **ElasticSearch:** Search and analytics engine for efficient data querying.
- **AWS SES:** Email service for sending recommendations.
- **Python:** Core programming language for Lambda functions.

## Project Structure

Here is an overview of the key files in the project and their roles:

- **LF0.py**: Contains specific logic and functions related to handling particular intents or actions by the chatbot.
- **LF2.py**: Similar to LF0.py, this file includes additional logic for managing different functionalities or interactions in the chatbot.
- **utils.py**: Utility functions that support various operations across the project, such as data formatting and common helper methods.
- **validations.py**: Functions for validating user input and other data to ensure proper processing and avoid errors.
- **lambda_function.py**: The main entry point for AWS Lambda, orchestrating the chatbot's responses, interacting with other AWS services, and managing session data.
- **actions.py**: Core actions or behaviors the chatbot performs, such as fetching restaurant data, processing user requests, and generating responses.

## Getting Started

Follow these steps to set up and run the Dining Concierge Chatbot on your local machine.

### Prerequisites

- An AWS account with permissions to use AWS Lex, Lambda, DynamoDB, API Gateway, and SES.
- Python 3.8 or later installed on your local machine.
- `pip` package installer.

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/tanmayr71/Dining-Concierge-Chatbot.git
   cd Dining-Concierge-Chatbot
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up AWS Services:**
   - Create an AWS Lex bot with the provided JSON configuration file.
   - Deploy Lambda functions using the deployment scripts or AWS Management Console.
   - Set up DynamoDB tables as specified in the project’s `dynamodb_setup.py`.
   - Configure API Gateway to connect with your Lambda functions.
   - Set up SES for email functionalities.

### Usage

1. **Start the Bot:**
   - Invoke the AWS Lex bot through the AWS Management Console or integrate it with a web or mobile client.

2. **Test the Chatbot:**
   - Interact with the bot to receive personalized restaurant recommendations based on your inputs.

### Deployment

To deploy this chatbot on AWS, follow these steps:

1. **Create and Deploy Lambda Functions:**
   - Use the `serverless.yml` configuration file or deploy manually through the AWS Console.

2. **API Gateway Setup:**
   - Configure endpoints in API Gateway to handle requests from AWS Lex and return responses from Lambda functions.

3. **DynamoDB and ElasticSearch:**
   - Ensure that your DynamoDB tables are populated with relevant restaurant data.
   - Set up ElasticSearch indices for efficient querying.

### Contributing

Contributions are welcome! Please follow these steps to contribute to the project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

For any queries or issues, please contact [Tanmay Rathi](mailto:tr2452@nyu.edu).
