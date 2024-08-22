# xbox-trial-code-checker
A request based Python tool to check if XGPC (Xbox Gamepass invite-friend Trial codes) is valid, or not.

# How to use?

Download the script, install the requirements. (pip install requests colorama)

On this part of the code, remove the dummy text and replace it with your auth headers

![image](https://github.com/user-attachments/assets/dd71adea-cc6a-448a-844b-a15eb781eb88)

Put your codes in "codes.txt" at same folder, one code each line, and run by "python main.py".

After done, it will save the valid codes in valid_codes.txt

# How to get your headers

You don't need to do this every time. Only when your XBL authorization token expires.

Login to XBOX with a testing / dummy microsoft account. 

Go to https://www.xbox.com/en-US/xbox-game-pass/invite-your-friends/redeem?offerId=ccccccccc

Find this GET request on your Networks tab

![image](https://github.com/user-attachments/assets/45f635e1-9c2d-4ef9-879e-84c28a91a4ec)

Right click it and Copy as fetch

![image](https://github.com/user-attachments/assets/03f74c92-a26c-4812-980a-fabef2c404f2)

Paste it to a notepad. In the pasted text, there should be your headers

Copy your headers from User-Agent to Priority

![image](https://github.com/user-attachments/assets/f8e2cebb-befc-4bb6-a5b3-3a6b28a163bd)

and directly paste it into the headers part of your code

![image](https://github.com/user-attachments/assets/0992aa99-ece9-4f3f-acad-a9fbd4ca737c)

# Why? Can't you put a email pass or something

Yes you can, but i'm too lazy to add the code that does mail:pass > xbl token

# Bugs?

I dont know all of the responses, so some codes show as "Invalid" while they're "Used", but it shouldn't be a problem

# Threading? Proxy?

No.

