import sshtunnel
import appJar
from appJar import gui

app = gui()

'''Language Translations'''

app.setTitle("Port Borer")

defaultserver = "67328286-288b-4d7d-b637-3fe2ae63abf2.pub.cloud.scaleway.com"
defaultpass = "pass"


serverlangentry = "Server"
passwordlangentry = "Password"
remembermelangentry = "Remember Me"
loginbuttlangentry = "Log In"

changeservbuttlangentry = "Change Server"
customportbuttlangentry = "Custom"
localportbuttlangentry = "Local"
serveravailportbuttlangentry = "UnReserved"


def press(button):
	if button == customportbuttlangentry:
		app.stop()
	if button == localportbuttlangentry:
		app.stop()
	if button == serveravailportbuttlangentry:
		app.stop()


def loginpress(button):
	app.hide()

	server = app.getEntry(serverlangentry)
	password = app.getEntry(passwordlangentry)
	remember = app.getCheckBox(remembermelangentry)
	print("Server:", server, "Pass:", password, "Remember:", remember)

	app.removeAllWidgets()
	app.disableEnter()
	app.setResizable(canResize=True)
	app.show()





app.addLabelEntry(serverlangentry, 1, 1, 2)
app.setEntryDefault(serverlangentry, defaultserver)
app.addLabelSecretEntry(passwordlangentry, 2, 1, 2)
app.addCheckBox(remembermelangentry, 3, 1)
app.addButtons([loginbuttlangentry], loginpress, 3, 2)
app.enableEnter(loginpress)
app.setResizable(canResize=False)

app.go()













