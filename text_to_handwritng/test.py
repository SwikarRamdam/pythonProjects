import pywhatkit as wk

text = """Text messaging, or texting, is the act of composing and sending electronic messages, typically consisting of alphabetic and numeric characters, between two or more users of mobile devices, desktops/laptops, or another type of compatible computer. Text messages may be sent over a cellular network, or may also be sent via an Internet connection."""

wk.text_to_handwriting(text,"text.png",[255, 0, 0])
wk.text_to_handwriting(text)
print("Successful")