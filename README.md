# 🎬 Serverless Movie Ticket Booking System on AWS

A cloud-native **Movie Ticket Booking System** built using **AWS Serverless Services**. The application allows users to book movie tickets, prevents duplicate seat reservations, stores booking details in Amazon DynamoDB, and sends real-time booking confirmation emails using Amazon SNS.

---

## 🚀 Project Overview

This project demonstrates how multiple AWS services work together to build a scalable, secure, and fully serverless web application.

Users can:
- 🎟️ Book movie tickets
- 💺 Prevent duplicate seat bookings
- 📋 View all bookings
- 🗑️ Delete bookings
- 📧 Receive email confirmation after successful booking

---

## ☁️ AWS Services Used

| Service | Purpose |
|----------|---------|
| **Amazon API Gateway** | REST API |
| **AWS Lambda** | Backend Business Logic |
| **Amazon DynamoDB** | NoSQL Database |
| **Amazon SNS** | Email Notification |
| **AWS IAM** | Access Management |
| **Amazon CloudWatch** | Logging & Monitoring |

---

## ✨ Features

- **Serverless Architecture:** Highly scalable and cost-effective.
- **Movie Ticket Booking:** Streamlined booking process.
- **Duplicate Seat Prevention:** Real-time validation using DynamoDB conditional checks.
- **REST API Integration:** Full CRUD operations via API Gateway.
- **Email Notification:** Instant booking confirmation emails using SNS.
- **Responsive Web Interface:** Clean and user-friendly frontend.

---

## 🔄 Project Workflow

1. User enters booking details via the web interface.
2. Frontend sends a `POST` request to API Gateway.
3. API Gateway invokes the AWS Lambda function.
4. Lambda checks DynamoDB for duplicate seat booking.
5. If the seat is available:
   - Stores the booking record in DynamoDB.
   - Publishes a notification to Amazon SNS.
6. SNS sends a booking confirmation email to the user.
7. Users can retrieve all bookings using a `GET` request.
8. Users can delete bookings using a `DELETE` request.

---

## 📚 REST APIs

| Method | Endpoint | Description |
|----------|-----------|-------------|
| `POST` | `/ticket` | Book Ticket |
| `GET` | `/ticket` | Get All Bookings |
| `DELETE` | `/ticket` | Delete Booking |

---

## 📂 Project Structure

```text
Movie Ticket Booking SNS & Dynamo/
│
├── MovieTicketDynamoDB.html           # Frontend UI
├── lambda.py                          # AWS Lambda backend logic
├── README.md                          # Project documentation
├── Architecture of Movie Ticket.jpg   # High-level architecture diagram
├── demo/                              # Demo videos and implementation gifs
└── screenshots/                       # Implementation screenshots
```

---

## 💻 Technology Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Boto3)
- **AWS Cloud:**
  - AWS Lambda
  - Amazon API Gateway
  - Amazon DynamoDB
  - Amazon SNS
  - Amazon CloudWatch
  - AWS IAM

---

## 🎯 Learning Outcomes

- Built REST APIs using **Amazon API Gateway**.
- Developed serverless applications with **AWS Lambda**.
- Integrated **Amazon DynamoDB** for NoSQL data storage.
- Implemented duplicate booking prevention.
- Configured **Amazon SNS** for real-time notifications.
- Managed **IAM** roles and permissions.
- Used **Amazon CloudWatch** for monitoring and logging.
- Connected a responsive frontend with AWS backend services.

