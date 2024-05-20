# Real-Time Bid Adjustment

## Overview
This project automates the adjustment of bids in real-time based on campaign performance and budget utilization using AWS services.

## Architecture
![Architecture Diagram](diagrams/architecture_diagram.png)

## AWS Services Used
- AWS Lambda
- Amazon DynamoDB
- Amazon CloudWatch
- AWS Step Functions

## Features
- Real-time monitoring of campaign performance.
- Automated bid adjustments based on predefined rules.
- Scalable and cost-effective solution.

## Prerequisites
- AWS account
- API access to advertising platforms (e.g., DV360, Amazon DSP, TradeDesk, CM360).

## Setup

### Step 1: Deploy Infrastructure
1. Deploy the CloudFormation stack using `infrastructure/cloudformation_template.yaml`.

### Step 2: Configure Lambda Functions
1. Update `src/bid_adjuster.py` with API credentials and endpoints.
2. Deploy the Lambda functions using the AWS Lambda console or AWS CLI.

## Usage
1. The Lambda function `bid_adjuster.py` runs periodically to fetch campaign performance data.
2. The function adjusts bids based on performance metrics and budget constraints.
