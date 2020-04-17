from flask import Blueprint

simple_page = Blueprint("simple_page", __name__)


@simple_page.route("/<page>")
def show(page):
    return page * 3


@simple_page.route("")
def main():
    return "Hit simple main page"
