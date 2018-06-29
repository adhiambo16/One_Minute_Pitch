from flask_login import login_required

@main.route('/user/<uname>&<id_user>')
@login_required
def profile(id):