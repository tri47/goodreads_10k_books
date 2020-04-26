aws emr create-cluster --name "book-10k-cluster" \
    --release-label emr-5.24.1 \
    --applications Name=Spark \
    --log-uri s3://goodbooks-10k/logs/ \
    --ec2-attributes KeyName="KEY" \
    --instance-type m5.xlarge \
    --instance-count 3 \
    --bootstrap-actions Path=s3://goodbooks-10k/emr_bootstrap.sh \
    --use-default-roles