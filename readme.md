# Data Pipeline with Python and PostgreSQL

This project showcases a straightforward data pipeline that fetches data from an API, inserts the data into a PostgreSQL database, and verifies the data. The pipeline is built using Python, and specifically makes use of the `requests` and `psycopg2` libraries.

## Code Overview

The provided code demonstrates a data pipeline built with Python and PostgreSQL. Here's an overview of the different components and their functionalities:

- **Fetching Data from the API**: The `fetch_data_from_api()` function retrieves data from an API (`https://random-data-api.com/api/v2/users`) using the `requests` library. It specifies the desired size of the data (100 records) through query parameters. If there is an error during the API request, an exception is raised and logged.

- **Creating the Users Table**: The `create_users_table()` function creates a table named `users` in the PostgreSQL database if it doesn't already exist. It uses the `psycopg2` library and executes an SQL query to define the table schema. Any exceptions that occur during the table creation process are logged.

- **Inserting Data into the Users Table**: The `insert_data_into_users_table()` function inserts the fetched data into the `users` table. It iterates over each item in the fetched data, extracts the required fields (country, name, surname, gender), and executes an SQL insert query to add the data to the table. If there are any exceptions during the data insertion, they are logged.

- **Verifying Data**: The `verify_data()` function selects and displays the first 100 rows from the `users` table to verify the data stored in the PostgreSQL database. Any exceptions that occur during the verification process are logged.

- **Main Entry Point**: The `main()` function serves as the main entry point of the script. It establishes a connection to the PostgreSQL database using the provided environment variables (`host`, `port`, `database`, `user`, `password`). The script then fetches data from the API, creates the `users` table (if necessary), inserts the fetched data into the table, and verifies the data. Any exceptions that occur during the process are logged.

The script logs its execution events using the `logging` module, with logs being written to the `script.log` file. Environment variables are loaded from a `.env` file using the `dotenv` library.

To run the script, execute the `main()` function. Adjust the environment variables in the `.env` file to match your PostgreSQL database configuration.

Please ensure that you have the required Python packages (`requests`, `psycopg2`, `dotenv`) installed before running the script.

## Unit Tests

The code includes a set of unit tests implemented using the Python `unittest` framework. These tests ensure the correctness of key functionalities within the data pipeline. Let's take a closer look at the unit tests and their purposes:

- **`test_fetch_data_from_api_success`**: This test validates the `fetch_data_from_api()` function's ability to successfully retrieve data from the API. It uses a mocked HTTP response to simulate a successful API call and compares the returned data with the expected data.

- **`test_create_users_table_success`**: This test verifies the `create_users_table()` function's capability to create the `users` table in the PostgreSQL database. It uses a mocked database cursor and checks if the SQL query for table creation is executed correctly.

- **`test_verify_data_success`**: This test ensures the `verify_data()` function's correctness in verifying the data stored in the PostgreSQL database. It captures the standard output during the function's execution and compares it with the expected output.

## Requirements

Before you begin, please make sure that you have the following installed:

- Python 3.6 or higher
- PostgreSQL server

## Getting Started

1. Clone this repository:

   ```bash
   git clone <repository_url>

2. Initializing a virtual environment:

    ```bash
    python -m venv .venv

3. Activating the virtual environment:

* For Windows
    ```bash
    cd .venv/scripts
    .\activate

* For MacOS
    ```bash
    source .venv/bin/activate

4. Activating the virtual environment:

    ```bash
    cd .venv/scripts
    .\activate

5. Installing requirements:

    ```bash
    pip install -r requirements.txt

6. Running the main pipeline:

    ```bash
    python main.py

7. Running the unit tests:

    ```bash
    python -m unittest discover -s . -p "*tests.py"

8. Running the entire project at once:
* For Windows:
    ```bash
    .\run.bat

* For MacOS:
    ```bash
    chmod +x run.sh
    ./run.sh

## Scaling the Pipeline with Airflow

To handle the data pipeline using Airflow, follow these steps:

1. Install Apache Airflow in your preferred environment.

2. Define a DAG (Directed Acyclic Graph) that represents your data pipeline. This can be done by creating a Python file with the necessary configurations.

3. Set up tasks within the DAG to perform specific actions. For example, create tasks to fetch data from the API, insert data into the PostgreSQL database, and verify the data.

4. Configure the dependencies between tasks using operators such as `BashOperator`, `PythonOperator`, or custom operators. This ensures that tasks are executed in the correct order.

5. Schedule the DAG to run periodically or based on specific events using the Airflow scheduler. Define the schedule interval or use external triggers to start the pipeline.

6. Monitor and manage pipeline execution using the Airflow UI or command-line interface. View logs, track task status, and troubleshoot any issues that may arise.

## Scaling the Pipeline with AWS Lambda

To handle the data pipeline using AWS Lambda, follow these steps:

1. Create an AWS Lambda function using the AWS Management Console or AWS CLI.

2. Write the necessary code within the Lambda function to fetch data from the API, insert it into the PostgreSQL database, and verify the data. This code can be written in Python and should utilise the `requests` and `psycopg2` libraries.

3. Set up appropriate triggers for the Lambda function. This can be achieved using AWS EventBridge, CloudWatch Events, or other event-driven mechanisms. Configure the triggers to execute the Lambda function at the desired interval or based on specific events.

4. Package the Lambda function code along with the required dependencies (e.g. `requests` and `psycopg2`). Create a deployment package that can be uploaded to AWS Lambda.

5. Configure the necessary environment variables for the Lambda function, including the database connection details and API credentials.

6. Monitor the Lambda function execution using AWS CloudWatch logs. View logs, track errors, and analyse the execution duration.

By following these steps, you can handle the data pipeline separately using Airflow and AWS Lambda. Adjust the configurations, code, and triggers based on your specific requirements and environment.

Please make sure to adjust the content and instructions according to your specific project requirements.

## Code References

If you're looking for more examples or references on building data pipelines with Python and working with PostgreSQL, you may find the following resources helpful:

- [Python `requests` Library Documentation](https://docs.python-requests.org/en/latest/) - Official documentation for the `requests` library, which is used for making HTTP requests and fetching data from APIs.

- [Psycopg - PostgreSQL Adapter for Python](https://www.psycopg.org/docs/) - Official documentation for Psycopg, the PostgreSQL adapter for Python. It provides detailed information on how to work with PostgreSQL databases using Python.

- [Apache Airflow Documentation](https://airflow.apache.org/docs/) - Official documentation for Apache Airflow, an open-source platform for programmatically authoring, scheduling, and monitoring workflows. It provides extensive guidance on setting up and managing data pipelines.

- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) - Official developer guide for AWS Lambda, offering in-depth information on creating, configuring, and deploying serverless functions using AWS Lambda.

Feel free to explore these resources to deepen your understanding and find additional examples to enhance your data pipeline implementation.