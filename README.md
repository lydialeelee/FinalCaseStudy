# Tip Calculator API

## 1) Executive Summary 

#### Problem 

Tipping is a common practice in many service industries, but calculating the appropriate tip percentage can sometimes be confusing. Customers often struggle to determine how much to tip based on their total bill amount, especially when paying with cash or splitting the bill among multiple people. Also it is a way for waiters and restaurant owners to ensure fair compensation for their services. 

#### Solution
This project allows you to input a total bill amount and a tip amount, and it will calculate the tip percentage for you. This can help customers quickly determine how much to tip based on their bill, ensuring fair compensation for service staff.

## 2) Project Overview

#### Course Concept(s)

Week 11 — Docker & Containerization
This project implements the concepts from the Week 11 module on containerization. The API is packaged inside a Dockerfile that defines the environment, dependencies, port configuration, and runtime command. Building and running the service inside a Docker container allows for reproducibility across machines because it goes from Dockerfile to Image to Container workflow.

#### Architecture Diagram

![Architecture Diagram](assets/architecture design.png)

#### Data / Models / Services

Data:
This project does not use any external datasets. No data is stored.

Format: JSON
Size: Not applicable (request-time only)
License: None (no external data sources)

Models:
There is no use of machine learning models. The system performs a simple calculation (tip / total_bill) to compute the tip percentage.

Format: Not applicable
Size: Not applicable
License: Not applicable

Services:
* Flask API providing /health and /tip endpoints
* Docker container for reproducible execution environment
* No third-party APIs or cloud services are used

## 3) How to Run (Local)

# build the container
docker build -t tip-calculator:latest .

# run the container
docker run --rm -p 8080:8080 tip-calculator:latest

# health check
curl http://localhost:8080/health
