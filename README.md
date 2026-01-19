# ☁️ Automated AWS S3 Security Scanner

An AI-powered security automation tool that detects AWS S3 vulnerabilities and provides automated remediation with approval workflows.

## 🎯 Overview

This project implements an automated security scanner for AWS S3 buckets that identifies public access block misconfigurations and uses AI-assisted remediation through Cursor and AWS MCP (Model Context Protocol) to fix vulnerabilities safely.

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
- Python 3.x installed
- AWS credentials configured on your system
- Appropriate IAM permissions for S3 operations
- Cursor IDE (for AI-assisted remediation)

## 🔐 AWS Configuration

Before running the scanner, ensure your AWS credentials are properly configured:

```bash
aws configure
```

**Required permissions:**
- `s3:GetBucketPublicAccessBlock`
- `s3:PutBucketPublicAccessBlock`
- `s3:ListAllMyBuckets`

## 📦 Installation

![Image](http://learn.nextwork.org/overjoyed_amber_trusty_clove/uploads/ai-aws-security-guard_aws2c3d4e)

## 🚀 Usage

<!-- Add usage instructions here -->

## 📸 Screenshots

### Building the S3 Scanner

![Image](http://learn.nextwork.org/overjoyed_amber_trusty_clove/uploads/ai-aws-security-guard_aws5f6g7h)

### Security Scan Results

![Image](http://learn.nextwork.org/overjoyed_amber_trusty_clove/uploads/ai-aws-security-guard_aws2m3n4o)

### Connecting Cursor to AWS with MCP

![Image](http://learn.nextwork.org/overjoyed_amber_trusty_clove/uploads/ai-aws-security-guard_aws8i9j0k)

### Testing the Scanner

![Image](http://learn.nextwork.org/overjoyed_amber_trusty_clove/uploads/ai-aws-security-guard_aws2m3n4o)

## 🔄 Workflow

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

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 👤 Author

Abhinav Biju

## 🙏 Acknowledgments

- AWS for S3 and boto3 SDK
- Cursor for AI-powered development tools
- The AWS MCP community

---

**Note:** This tool modifies AWS infrastructure. Always ensure you have proper backups and test in a development environment before running in production.
