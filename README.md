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

Trigger the Workflow!!
The GitHub Actions workflows are automatically initiated when changes are made to the speech file. To trigger them, follow these steps:
Create a new branch 
Edit the speeech file with your desired content.
Commit and push the changes to your branch.
Open a pull request into the main branch to trigger the "On Pull Request" workflow.
Merge the pull request into main to activate the "On Merge" workflow.
Monitor GitHub Actions to confirm that the workflows run as expected.

Review the Workflow !!!
Go to the "Actions" tab in your GitHub repository.
In the left sidebar, select the workflows named "On Pull Request" and "On Merge".
Click on the most recent run to view detailed logs.
Ensure the speech synthesis and S3 upload steps complete successfully. 

Verify the Uploaded .mp3 
To confirm that the audio files were uploaded correctly to your S3 bucket:
Open up S3 in the AWS Management Console.
Navigate to your specified bucket and select the "Objects" tab.
Look for the MP3 files under the folder.
You can preview or download the files to verify their content.
