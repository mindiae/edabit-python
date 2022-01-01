# Atbash Cipher
# The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

# Create a function that takes a string and applies the Atbash cipher to it.

# Examples
# atbash("apple") ➞ "zkkov"

# atbash("Hello world!") ➞ "Svool dliow!"

# atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
# Notes
# Capitalisation should be retained.
# Non-alphabetic characters should not be altered.
def atbash(txt):
	return txt.translate(str.maketrans(
	  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
	  "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"))

print(atbash("abcdefghijklmnopqrstuvwxyz") == "zyxwvutsrqponmlkjihgfedcba")
print(atbash("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "ZYXWVUTSRQPONMLKJIHGFEDCBA")
print(atbash("The word 'atbash' derives from the the first and last 2 letters of the Hebrew alphabet.") == "Gsv dliw 'zgyzhs' wvirevh uiln gsv gsv urihg zmw ozhg 2 ovggvih lu gsv Svyivd zokszyvg.")
print(atbash("Vmxibkgrlm zmw wvxibkgrlm ziv rwvmgrxzo uli gsv Zgyzhs xrksvi.") =="Encryption and decryption are identical for the Atbash cipher.")