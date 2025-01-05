import time
import json
import urllib.request

def fetch_json(url):
  with urllib.request.urlopen(url) as response:
    if response.status == 200:
      return json.loads(response.read().decode())
    else:
      return None

answer = None
redeemCodes = ["harwm", "bcowc", "nftdw", "baupp", "kkysw", "spdha", "fmfga", "vfcsu", "fgaic", "iiuhf"]
redeem_codes_data = fetch_json("https://lspectroniztar.github.io/lspectr-os/system/miscellaneous/tests/python/redeemCodes.json")
if redeem_codes_data:
  redeemCodes.extend(redeem_codes_data)
attempts = []
waitTime = 0

""" Test code for italicized text in tkinter
import tkinter as tk
root = tk.Tk()
label = tk.Label(root, text="This is italicized text", font=("Arial", 12, "italic"))
label.pack()
root.mainloop()
"""

while not answer in redeemCodes:
  answer = input("" if len(attempts) > 0 else "Enter your redeem code.")
  attempts.append(answer)
  if answer in redeemCodes:
    print("Congratulations! You have received content from the code \"" + answer + "\".")
  else:
    print("Redeem code not recognized. Please try again.\nYou have already entered the following redeem codes: " + str(attempts))
  if not answer in redeemCodes and len(attempts) == 10:
    waitTime += 30
    print(f"You have reached the maximum number of attempts. Please try again in {waitTime} seconds.")
    time.sleep(waitTime)
    attempts = []
    print("You may now try again.")
    
print("Thank you for redeeming your code. Enjoy your content!")
