from config import mysql
from extensions import *

note_show_controller = Blueprint('note_show_controller', __name__)
@note_show_controller.route('/note_show_controller', methods = ["GET", "POST"])
def note_show_page():
	## users should be prompted to login before going to the index page 
	if (not isUserLoggedIn()):
		return redirect(url_for('login.loginpage'))
	cur = mysql.connection.cursor()
	user_id = getUserID(cur, session['username'])
	results_assoc = getExistingNotes(cur, user_id)
	print(results_assoc, file = sys.stderr)
	return render_template('notes.html', notes = results_assoc)


