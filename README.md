# ☁️ Automated AWS S3 Security Scanner

An AI-powered security automation tool that detects AWS S3 vulnerabilities and provides automated remediation with approval workflows.

## 🎯 Overview

This project implements an automated security scanner for AWS S3 buckets that identifies public access block misconfigurations and uses AI-assisted remediation through Cursor and AWS MCP (Model Context Protocol) to fix vulnerabilities safely.

## 📊 Project Blueprint
<img src= "https://i.imgur.com/gi79MeO.png" width="100%" alt="Terminial view">

## ✨ Features

- 🔍 **Automated Security Scanning** - Detects S3 Public Access Block misconfigurations across your AWS environment
- 🤖 **AI-Powered Remediation** - Leverages Cursor with AWS MCP for intelligent security fixes
- ✅ **Approval Workflow** - Requires explicit approval before applying any changes to your infrastructure
- 📊 **Risk Assessment** - Identifies and categorizes security vulnerabilities
- 🐍 **Python & Boto3** - Built with robust AWS SDK integration
- 🔧 **Flexible Execution** - Currently on-demand with capability to extend to scheduled or trigger-based runs

## 🛠️ Technologies Used

- **AWS S3** - Object storage service
- **Python** - Core programming language
- **Boto3** - AWS SDK for Python
- **Cursor** - AI-powered code editor with AWS MCP integration
- **AWS MCP** - Model Context Protocol for AWS control through chat

## 📋 Prerequisites

- AWS Account with S3 access
- Python 3.12 installed
- AWS credentials configured on your system
- Appropriate IAM permissions for S3 operations
- Cursor IDE (for AI-assisted remediation)

## 🔐 AWS Configuration

### Before running the scanner, ensure your AWS credentials are properly configured:
### Open your terminal and check to see if AWS CLI is installed:
- Windows: Press Win key and type PowerShell
- macOS: Press Cmd+Space and type Terminal
```bash
aws --version
```
- If already installed, you will see a AWS CLI version number! 
- **IF NOT DO THIS:**
```bash
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
```


## 📦 Installation
- Check if you have AWS credentials configured
```bash
aws sts get-caller-identity
```
- Create a new folder on your Desktop and name it below.
```bash
AWS-Security-Guard
```
- Create a virtual environment and run this command
```bash
python -m venv venv
```
- Activate the virtual environment.
```bash
venv\Scripts\activate
```
- Next, now that your virtual environment is active, install boto3 (AWS SDK for Python) by running this command below:
```bash
pip install boto3
```
### If Installed Correctly It Should Look Like Below:
![Image](http://learn.nextwork.org/overjoyed_amber_trusty_clove/uploads/ai-aws-security-guard_aws2c3d4e)

- Now check if you have uv (Python package manager) installed
- Run this command:
```bash
uv --version
```
- If not installed, do this command:
```bash
iwr https://astral.sh/uv/install.ps1 -UseBasicParsing | iex
```

## 📸 Screenshots

### Building the S3 Scanner through a Python file (Code posted):

![Image](http://learn.nextwork.org/overjoyed_amber_trusty_clove/uploads/ai-aws-security-guard_aws5f6g7h)

# 💡 What does this code do?

### This creates the basic structure of your scanner:

- import boto3 - Loads the AWS SDK library so you can interact with AWS services

- from botocore.exceptions import ClientError - Imports the exception class we'll use to handle AWS API errors properly

- s3 = boto3.client('s3') - Creates a client object that connects to Amazon S3 using your AWS credentials

- s3.list_buckets() - Makes an API call to AWS that returns a list of all S3 buckets in your account

- print(f"Found {len(buckets['Buckets'])} buckets to scan\n") - Shows how many buckets were found

- for bucket in buckets['Buckets']: - Loops through each bucket so you can check it individually

- findings = [] - Creates an empty list to store any security issues found

- if __name__ == "__main__": - This Python pattern means "only run this code if this file is executed directly" (what's a module?)

## Connecting Cursor to AWS with MCP Server

![Image](http://learn.nextwork.org/overjoyed_amber_trusty_clove/uploads/ai-aws-security-guard_aws8i9j0k)

### Add this to your mcp.json and REPLACE your-region with your AWS region (the one you set in aws configure)
```bash
{
  "mcpServers": {
    "aws": {
      "command": "uv",
      "args": ["run", "--with", "awslabs.aws-api-mcp-server", "awslabs.aws-api-mcp-server"],
      "env": {
        "AWS_REGION": "your-region"
      }
    }
  }
}
```
# 💡 What does this configuration do?
### This JSON tells Cursor how to start the AWS MCP server:

- "command": "uv" - Tells Cursor to use the uv package manager to run the server

- "args": [...] - Specifies to install and run the official AWS MCP server package (awslabs.aws-api-mcp-server)

- "env": {"AWS_REGION": "..."} - Sets the AWS region the server should connect to

- When Cursor starts, it reads this file and launches the AWS MCP server automatically

- The server connects to your AWS account using the credentials you configured with aws configure

- This gives Cursor the ability to execute AWS API calls on your behalf through chat

## Create a Test Bucket Using Cursor + AWS MCP
### Before running your scanner, let's use Cursor's AI with AWS MCP to create a deliberately insecure S3 bucket. This will give you a security issue to find and fix!
- Open Cursor's chat panel by pressing Cmd+L (macOS) or Ctrl+L (Windows)
- Send this prompt to Cursor
```bash
Create an S3 bucket named "test-security-demo-12345" without any public access block configuration, so my security scanner will detect it as a CRITICAL issue.
```
- Replace 12345 with 5 random digits (like 67890). S3 bucket names must be globally unique.
- Cursor will propose AWS commands - You'll see it planning to use the AWS CLI to create your bucket

## Security Scan + Results
### Run Your Security Scanner
- Now let's run your scanner to detect the security issue in the bucket you just created.
- Open a terminal in Cursor (Terminal → New Terminal)
- Make sure your virtual environment is activated (you should see (venv) in the prompt). Not activated? in my terminal prompt.) Why does this matter?

- Run your scanner (Windows, but for MAC add 3 after python):
```bash
python scanner.py
 ``` 
### Your Output should look something like this: 
![Image](http://learn.nextwork.org/overjoyed_amber_trusty_clove/uploads/ai-aws-security-guard_aws2m3n4o)

### You'll see:
- Found X buckets to scan - Shows how many buckets exist in your account (including your test-security-demo bucket)
- CRITICAL: [test-security-demo-xxxxx] No public access block configured - Your test bucket has NO protection at all
- Scan complete. Found 1 issues. (or more if you have other insecure buckets)

## Scan Remediated through AI
### Fix Security Issues Using Cursor + AWS MCP
- Now let's use AI to fix these security issues automatically. This is where Cursor + AWS MCP shines - you can fix AWS security issues through natural language!

- Open Cursor's chat panel (Cmd+L on Mac, Ctrl+L on Windows)
= Send this prompt:
```bash
I just ran scanner.py and found security issues with my S3 buckets.
Can you help me fix all CRITICAL findings by enabling public access blocks on those buckets?
```
- Press Enter and watch Cursor work
### Cursor will:
- Use AWS MCP to check your buckets
- Generate the AWS CLI commands to fix them
- Ask for your permission to run the commands
- Execute the fixes

### Final Output
<img src= "https://imgur.com/TyJ70RK.png" width="100%" alt="Terminial view">

## 🔄 Cloud Security Workflow
 
1. **Scan** - The scanner examines all S3 buckets for public access misconfigurations
2. **Detect** - Identifies buckets with Public Access Block disabled or misconfigured
3. **Analyze** - AI assesses the security risk and proposes fixes
4. **Approve** - User reviews and approves recommended changes via Cursor
5. **Remediate** - Automated application of security fixes to vulnerable buckets

## 🎛️ Execution Modes

### Current: On-Demand
Run the scanner manually whenever needed.

### Future Capabilities
- **Scheduled** - Run scans at regular intervals (hourly, daily, weekly)
- **Trigger-Based** - Execute scans based on CloudWatch Events or S3 bucket creation

## ⚠️ Security Considerations

- Always review proposed changes before approval
- Test in a non-production environment first
- Ensure proper IAM roles and permissions
- Monitor AWS CloudTrail for audit logging

## 🙏 Acknowledgments

- AWS for S3 and boto3 SDK
- Cursor for AI-powered development tools
- The AWS MCP community

---

**Note:** This tool modifies AWS infrastructure. Always ensure you have proper backups and test in a development environment before running in production.
