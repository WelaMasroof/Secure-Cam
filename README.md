
# AI-Based Person Detection System - Home Security

This project implements an AI-based person detection system designed to enhance home security. The system processes real-time video input using YOLOv8, sends alerts via email and SMS when a person is detected, and integrates with a secure database.

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [Database Setup](#database-setup)
- [Configuration](#configuration)
- [Installing Dependencies](#installing-dependencies)
- [Running the Application](#running-the-application)
- [Contributors](#contributors)
  
## Setup Instructions

### 1. Database Setup (SSMS)

Before running the system, you need to set up the required database in SQL Server Management Studio (SSMS). Use the following SQL scripts to create the necessary tables:

```sql
CREATE TABLE Login (
    Id INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-incrementing ID
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) NOT NULL UNIQUE,
    Password NVARCHAR(255) NOT NULL,
    Type NVARCHAR(20) DEFAULT 'user',
    Approval BIT DEFAULT 0             -- New column for approval with default value false (0)
);

CREATE TABLE Alerts (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Message NVARCHAR(255) NOT NULL,
    ImagePath NVARCHAR(255) NOT NULL,
    Timestamp DATETIME NOT NULL,
    IsRead BIT NOT NULL DEFAULT 0
);

CREATE TABLE ProblemReports (
    Id INT IDENTITY PRIMARY KEY,
    ImageData VARBINARY(MAX),
    Description NVARCHAR(MAX),
    ReportDate DATETIME DEFAULT GETDATE()
);
```

### 2. Configuration

#### Update Database Connection String
- In the Python and C# code, update the database connection string to match your local setup.
- Ensure the connection string points to the SQL Server database you just created.

#### Update Model Path and API URL
- In the code, modify the paths to the YOLOv8 model and API according to your local setup:
  - Path to the model file.
  - The API URL should be updated if it differs from the default address on your machine.

### 3. Installing Dependencies

#### Python Dependencies

1. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

2. **Install the required Python libraries:**
    ```bash
    pip install flask flask-cors opencv-python-headless twilio ultralytics
    ```

#### C# Dependencies

1. **Install the required C# libraries:**
   - You will need to add these libraries to your C# project:
     - `System.Net.Mail` (for sending emails)
     - `Twilio` (for sending SMS)
   
   You can install the Twilio library using NuGet:
   ```bash
   Install-Package Twilio
   ```

2. **Add other required libraries:**
   - Ensure you have all necessary dependencies for integrating the backend and frontend parts.

### 4. Running the Application

1. **Start the Flask backend:**
    - Navigate to the directory where your `app.py` file is located.
    - Run the application:
      ```bash
      python app.py
      ```

2. **Run the C# frontend:**
    - Build and run your C# project in Visual Studio or your preferred C# IDE.
    - Ensure the frontend communicates with the Flask backend correctly.

### 5. Troubleshooting

- **Database connection issues:**
  - Double-check your SQL Server connection string in the code.
  
- **Model not loading:**
  - Verify the path to the YOLOv8 model file is correct.

- **Email/SMS issues:**
  - Ensure that you have configured the Twilio and SMTP settings properly in the C# code.

### 6. Future Enhancements
- Support for multiple video streams.
- Integration of person profiles for better security and access control.

## Contributors
- **User**: Developer and project lead.
- **Umar**: Collaborator and testing.
- **Muaz**: Contributor and testing.
- **Teacher**: Guidance and support.
