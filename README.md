# polly-audio

1. AWS Req's
An S3 bucket named: pixel-learning-polly-audio
IAM user with:
polly:SynthesizeSpeech
s3:PutObject permissions

2. GitHub Secrets
Set these in your repo's Settings > Secrets and Variables > Actions:

AWS_ACCESS_KEY_ID – Your AWS access key ID
AWS_SECRET_ACCESS_KEY – Your AWS secret access key
AWS_S3_BUCKET – Your S3 bucket name

3. Modification
Edit the speech.txt file to update the content to be converted.

4. Trigger the Workflow
Open a Pull Request to main branch → triggers beta version (beta.mp3)
Merge into main → triggers production version (prod.mp3)

5. Verify Outcome/Output
Check your S3 bucket under the polly-audio/ prefix:

beta.mp3 – For review
prod.mp3 – Final version
