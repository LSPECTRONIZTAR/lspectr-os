answer = None
redeemCodes = ["harwm", "bcowc", "nftdw", "baupp", "kkysw", "spdha", "fmfga", "vfcsu", "fgaic", "iiuhf"]
attempts = []
while not answer in redeemCodes:
  answer = input("Enter your redeem code.")
  attempts.append(answer)
  if answer in redeemCodes:
    print("Congratulations! You have received content from the code \"" + answer + "\".")
  else
    print("Redeem code not recognized. Please try again.\nYou have already entered the following redeem codes:)
    for i in attempts
      print(i)
