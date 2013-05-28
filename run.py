from application import app, config
app.run(debug=config.DevelopmentConfig.DEBUG)
