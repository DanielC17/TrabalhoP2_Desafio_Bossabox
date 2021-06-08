from flask import Flask, render_template, request, url_for
import os

template_folder = os.path.abspath('application/view/templates')
static_folder = os.path.abspath("application/view/static")

app = Flask(__name__, template_folder = template_folder, static_folder = static_folder)

'''from application.controller import home_controller'''