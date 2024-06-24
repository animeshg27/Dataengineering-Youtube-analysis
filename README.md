# YouTube Video Data Management and Analysis

## Project Overview
With an emphasis on trending metrics and video kinds, this project aims to securely organize, streamline, and analyze structured and semi-structured YouTube video data.

## Project Goals

1. **Data Ingestion**
   - Develop a system to ingest data from various sources.

2. **ETL System**
   - Transform raw data into a suitable format for analysis.

3. **Data Lake**
   - Create a centralized repository to store data from multiple sources.

4. **Scalability**
   - Ensure the system can scale efficiently as data volume increases.

5. **Cloud Integration**
   - Utilize AWS to process large datasets, overcoming local machine limitations.

6. **Reporting**
   - Develop a dashboard to answer key questions and provide insights.

## AWS Services Utilized

- **Amazon S3**
  - Scalable object storage service offering high data availability, security, and performance.
  
- **AWS IAM**
  - Service for managing secure access to AWS resources and services.
  
- **QuickSight**
  - Scalable, serverless BI service powered by machine learning for building dashboards.
  
- **AWS Glue**
  - Serverless data integration service for discovering, preparing, and combining data for analytics.
  
- **AWS Lambda**
  - Computing service that runs code without the need for server management.
  
- **AWS Athena**
  - Interactive query service for analyzing data directly in S3 without loading it into other services.

## Dataset Information

The dataset used in this project is sourced from Kaggle and includes statistics on daily trending YouTube videos over several months. Each day, up to 200 trending videos are recorded for various regions, with data for each region stored in separate files. The dataset includes fields such as:

- Video title
- Channel title
- Publication time
- Tags
- Views
- Likes
- Dislikes
- Description
- Comment count
- `category_id` field (varies by region and linked to a JSON file)

[Dataset Link](https://www.kaggle.com/datasets/datasnaek/youtube-new)

## How to Use This Project

1. **Setup AWS Services**
   - Configure Amazon S3, AWS IAM, QuickSight, AWS Glue, AWS Lambda, and AWS Athena as described in the AWS documentation.

2. **Data Ingestion**
   - Use AWS Lambda or other ingestion mechanisms to collect data from the specified sources.

3. **ETL Processing**
   - Utilize AWS Glue to transform and clean the raw data.

4. **Data Storage**
   - Store the processed data in Amazon S3 as a centralized data lake.

5. **Data Analysis**
   - Use AWS Athena to query the data stored in S3.

6. **Reporting**
   - Build interactive dashboards and reports using QuickSight to visualize the data insights.
