from website import create_app

import os

app = create_app()

if __name__ == '__main__':
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    port = int(os.environ.get("PORT", 5000))
    #context = ('cert.pem', 'key.pem')#certificate and key files
    app.run(debug=True, port=port)#, ssl_context=context)
