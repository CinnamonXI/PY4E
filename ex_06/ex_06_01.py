#string manipulation
text = "X-DSPAM-Confidence:    0.8475"
ntext = text.find("0")
print(float(text[ntext :]))