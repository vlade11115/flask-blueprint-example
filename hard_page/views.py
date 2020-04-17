from flask import Blueprint

hard_page = Blueprint("hard_page", __name__)


@hard_page.route("/<page>")
def show(page):
    return page * 300


@hard_page.route("")
def my_main():
    return "<b>Hit rich HTML main page</b>"
