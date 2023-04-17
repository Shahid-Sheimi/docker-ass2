Created a README.txt file in parallel with the docker-compose.yml file, providing instructions on how to run the docker-compose command and any other relevant information.
To build and run the containers, use the following command in the Assignment2 directory:
docker-compose up
The server will run on http://localhost:5000 and the client will make a GET request to the server and display the response.

Assignment2/
|-- client/
|   |-- Dockerfile
    |-- app/
    |       |-- client.py
|   |-- requirements.txt
|   
|-- server/
|   |-- Dockerfile
    |-- app/
|       |-- server.py
|   |-- requirements.txt
|   

|-- docker-compose.yml
|-- README.txt



