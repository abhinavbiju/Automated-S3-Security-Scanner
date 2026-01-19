import boto3
from botocore.exceptions import ClientError

def scan_s3_buckets():
    """Scan all S3 buckets for public access misconfigurations"""
    s3 = boto3.client('s3')
    findings = []

    print("Scanning S3 buckets for public access...\n")

    buckets = s3.list_buckets()
    print(f"Found {len(buckets['Buckets'])} buckets to scan\n")

    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']

        try:
            public_block = s3.get_public_access_block(Bucket=bucket_name)
            config = public_block['PublicAccessBlockConfiguration']

            if not all([
                config.get('BlockPublicAcls'),
                config.get('BlockPublicPolicy'),
                config.get('IgnorePublicAcls'),
                config.get('RestrictPublicBuckets')
            ]):
                findings.append({
                    'bucket': bucket_name,
                    'issue': 'Public access not fully blocked',
                    'severity': 'CRITICAL'
                })
                print(f"WARNING: [{bucket_name}] Public access not fully blocked")

        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchPublicAccessBlockConfiguration':
                findings.append({
                    'bucket': bucket_name,
                    'issue': 'No public access block configured',
                    'severity': 'CRITICAL'
                })
                print(f"CRITICAL: [{bucket_name}] No public access block configured")
            else:
                print(f"ERROR: Could not scan {bucket_name}: {str(e)}")

        except Exception as e:
            print(f"ERROR: Could not scan {bucket_name}: {str(e)}")


    print(f"\nScan complete. Found {len(findings)} issues.\n")
    return findings

if __name__ == "__main__":
    scan_s3_buckets()
