import iotud


app = iotud.create_app()
if __name__ == '__main__':
    #app.run()
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    # PORT: 8080 MUST

    app.run(host='127.0.0.1', port=5000, debug=True)
    
#gcloud builds submit --tag gcr.io/calendapi1/api
#gcloud beta run deploy --image gcr.io/calendapi1/api --platform managed
