# Spotify_DataPipeline_AzureProject

# End-to-End Spotify Data Engineering Pipeline using Azure Data Factory, Databricks Medallion Architecture, ADLS Gen2, and Power BI

## Project Overview

This project demonstrates an end-to-end modern data engineering pipeline built using Microsoft Azure services, Databricks Medallion Architecture, and Power BI.

The goal of the project is to ingest Spotify-style streaming data, process it through Bronze, Silver, and Gold layers, model it into a Star Schema warehouse structure, and create an interactive analytics dashboard for business insights.

The project covers the complete lifecycle of a real-world analytics engineering workflow:

Data ingestion
Data transformation
Data cleaning
Data modeling
Data warehousing
Dashboard analytics
Cloud integration
GitHub version control

## Architecture
Source Files

     ↓
Azure Data Factory

     ↓
ADLS Gen2 Bronze Layer (Raw Data)

     ↓
Databricks Silver Layer (Cleaned & Transformed Data)

     ↓
Databricks Gold Layer (Business-ready Analytical Data)

     ↓
Star Schema Warehouse Model

     ↓
Power BI Dashboard


## Tech Stack
### Cloud & Storage
Microsoft Azure
Azure Data Lake Storage Gen2 (ADLS Gen2)
###Data Engineering
Azure Data Factory (ADF)
Azure Databricks
PySpark
SQL
Databricks Asset Bundles (DAB)
### Analytics & Visualization
Power BI
### Version Control
GitHub

## Project Workflow
### Data Ingestion using Azure Data Factory

Azure Data Factory was used to orchestrate and ingest source data into the Bronze Layer stored in Azure Data Lake Storage Gen2.

Key Tasks:
Created datasets
Configured linked services
Built ingestion pipelines
Connected source to ADLS Gen2
Automated raw data movement

### Medallion Architecture

The project follows the Medallion Architecture pattern:

### Bronze Layer

The Bronze Layer stores raw ingested data exactly as received from the source.

#### Characteristics:
Raw data
No transformations
Historical ingestion storage
Source of truth
Supports incremental data ingestion
Supports backfilling for historical data recovery and reprocessing

#### Pipeline Capabilities:
Incremental loading using Azure Data Factory
Historical backfill support for missed or delayed records
Automated ingestion workflows into ADLS Gen2 Bronze storage
Scalable ingestion architecture for future data growth

### Silver Layer

The Silver Layer contains cleaned and transformed data.

#### Transformations Performed:
Null handling
Column formatting
Standardization
Deduplication
Data quality improvements
Schema refinement

#### Technologies Used:
PySpark
Databricks DataFrames

### Gold Layer

The Gold Layer contains business-ready analytical tables optimized for reporting and dashboarding.

#### Features:
Star schema modeling
Fact and dimension tables
KPI-ready data
Optimized for BI tools

### Data Warehouse Model

The Gold Layer was modeled into a Star Schema warehouse structure.

#### Fact Table
FactStream

Contains streaming activity and transactional metrics.

#### Dimension Tables
DimUser
Contains user information.

DimArtist
Contains artist-related information.

DimTrack
Contains track-level metadata.

DimDate
Contains date and time analytics attributes.

Star Schema Relationship
                DimUser
                    |
                    |
DimDate ---- FactStream ---- DimTrack ---- DimArtist

## Power BI Dashboard

An interactive Power BI dashboard was developed using the Gold Layer analytical tables.

### Dashboard Features

#### Executive KPIs
Total Users
Total Streams
Average Listen Duration
Total Tracks

#### Analytics Visuals
Streaming Trends Over Time
User Subscription Distribution
Streaming Activity by Device Type
Top 10 Countries by Active Users
Top 10 Most Streamed Tracks
Top 10 Most Streamed Artists

#### Interactive Slicers
Country
Subscription Type
Device Type
Date Filters

### Business Insights Generated

The dashboard helps answer business questions such as:

Which subscription type has the highest engagement?
Which countries generate the most streaming activity?
Which artists and tracks are most popular?
What devices are most commonly used?
How does streaming activity change over time?

## Key Features of the Project
Built an end-to-end Azure data engineering pipeline
Implemented Medallion Architecture using Databricks
Created Bronze, Silver, and Gold layers
Performed ETL transformations using PySpark
Modeled warehouse tables using Star Schema
Developed interactive Power BI analytics dashboard
Integrated Azure Data Factory with ADLS Gen2
Used Databricks Asset Bundles for project organization
Maintained project using GitHub version control

### Repository Contents

adf/

├── dataset/

├── linkedService/

├── pipeline/

Databricks notebooks and bundle configurations (in spotify_dab)

Power BI dashboard files

Architecture diagrams

README documentation

## Dashboard Preview
<img width="1337" height="751" alt="image" src="https://github.com/user-attachments/assets/fcc9b281-efd6-4b10-9ca2-61d423376ffc" />

## Architecture or dataflow
<img width="937" height="576" alt="image" src="https://github.com/user-attachments/assets/20d0b868-9a4c-4403-b45f-f2f271951450" />

## Learning Outcomes

This project helped strengthen practical skills in:

Azure cloud services
Data engineering workflows
ETL pipeline development
Data warehousing concepts
Star schema modeling
PySpark transformations
Power BI analytics
GitHub project management
End-to-end analytics architecture

## Conclusion

This project demonstrates a complete modern data engineering and analytics workflow using Azure services, Databricks, and Power BI.

The pipeline transforms raw streaming data into business-ready insights through scalable cloud-based architecture and interactive dashboard reporting.
