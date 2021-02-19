### klasik olarak flaskın config ayarları burada oluyor imiş.

from flask import Flask

app = Flask(__name__)

from MARKETLER import routes
