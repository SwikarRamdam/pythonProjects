from contextlib import redirect_stderr
import pywhatkit as pk
intro = "Hi, I am Swikar Ramdam. I love coding. I am an Engineer"
pk.text_to_handwriting(intro,("intro.png"),[245, 66, 66])
print("Succesful")
