from flask import render_template


def error_404(error):
    return render_template('errors/404.html'), 404


def error_403(error):
    return render_template('errors/403.html'), 403


def error_500(error):
    return render_template('errors/500.html'), 500
