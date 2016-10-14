from flask import Flask
from flask_restful import Resource, Api
import MySQLdb
from app import app

if __name__ == '__main__':
    app.run(debug=True)
