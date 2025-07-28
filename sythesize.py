import boto3
import os
import sys

# Read text from file
with open('speech.txt', 'r') as file:
    text = file.read()

# Initialize Polly client
polly_client = boto3.client('polly', region_name='us-east-1')

# Synthesize speech
response = polly_client.synthesize_speech(
    Text=text,
    OutputFormat='mp3',
    VoiceId='Joanna'
)

# Save the audio stream locally
output_filename = 'output.mp3'
with open(output_filename, 'wb') as file:
    file.write(response['AudioStream'].read())

print(f"Audio synthesis complete. File saved as {output_filename}.")

# Upload to S3
s3_client = boto3.client('s3', region_name='us-east-1')
bucket_name = os.environ.get('S3_BUCKET')

if not bucket_name:
    print("❌ Environment variable 'S3_BUCKET' is not set.")
    sys.exit(1)

# Use override key if provided
s3_key = os.environ.get('S3_KEY', 'polly-audio/output.mp3')

s3_client.upload_file(output_filename, bucket_name, s3_key)
print(f"✅ Uploaded to s3://{bucket_name}/{s3_key}")

