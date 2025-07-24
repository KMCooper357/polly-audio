import boto3
import os

# Interpret text from file
with open('speech.txt', 'r') as file:
    text = file.read()

# Polly service
polly_client = boto3.client('polly', region_name='us-east-1')

# Synthesize speech
response = polly_client.synthesize_speech(
    Text=text,
    OutputFormat='mp3',
    VoiceId='Joanna'
)

# Save the audio file to local
with open('output.mp3', 'wb') as file:
    file.write(response['AudioStream'].read())

print("Audio synthesis complete. File saved as output.mp3.")

# Upload to S3 Bucket!
s3_client = boto3.client('s3', region_name='us-east-1')
bucket_name = os.environ['S3_BUCKET']
s3_key = 'polly-audio/output.mp3'

# Adding a comment

s3_client.upload_file('output.mp3', bucket_name, s3_key)
print(f"Uploaded to s3://{bucket_name}/{s3_key}")
