# Blaise NiFi Receipt

A cloud function to process NiFi receipts and update DDS[https://github.com/ONSdigital/blaise-data-delivery-status].

## Testing

```sh
poetry install
make lint test
```

## Deployment

```sh
poetry export -f requirements.txt > requirements.txt
gcloud functions deploy nifi-receipt-test \
  --trigger-topic <trigger_topic> \
  --runtime python38 \
  --entry-poit=main \
  --set-env-vars=DDS_URL=<DDS_URL> /
  --region=europe-west2
```
