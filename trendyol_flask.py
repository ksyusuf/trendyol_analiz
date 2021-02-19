from flask import Flask, render_template, request, redirect, abort, flash, url_for, make_response, jsonify
from flask import Flask, render_template, request, jsonify
import trendyol_analiz
from MARKETLER import app
import os

# port = int(os.environ.get("PORT"), 5000)  # herokuya atma işleminde bu satır gerekiyormuş


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # app.run(debug=True, host='0.0.0.0', port=port)
