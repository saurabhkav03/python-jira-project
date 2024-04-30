# python-jira
## Our Goal
If a user comments `/jira` on an issue, GitHub will send information about the issue to our EC2 instance containing our Python application. The Python application will then communicate with Jira through its API, creating a new ticket on the Jira board.

## Steps
1. **API**:
   - In our project, GitHub posts information to our EC2 instance.
   - The API of the Python application should be of POST type.
   - We perform a POST action twice: once when GitHub posts info to the Python API, and again when the Python app performs a POST action to the Jira API.

2. **Convert the Python script to API**:
   - We use Flask to convert our Python code to a Flask framework to expose an API.
   - To write a Flask API:
     - Install the Flask module using the following command:
       ```
       pip install flask
       ```

3. **Deploy application to the server**:
   - Deploying the application to the server is necessary because GitHub cannot manually run the script on EC2.
   - Flask creates an inbuilt server, eliminating the need to deploy it on servers like Tomcat or any specific application servers.

4. **Configure GitHub webhooks**:
   - GitHub communicates with the Python Application API using webhooks, with the Python application present on the EC2 instance.
   - To set up webhooks:
     - Go to your GitHub repository > Settings > Select Webhooks and provide the API of your Python application.
     - Syntax: `http://public_ip:port/endpoint`
     - Select "Let me select individual events" > Select "Issue comments".

5. **Condition**:
   - Tickets are generated only when `/jira` is commented.
 
