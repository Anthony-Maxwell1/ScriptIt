import basic

print("""                                                                         
 ,---.               ,--.         ,--.  ,--.  ,--.
'   .-'  ,---.,--.--.`--' ,---. ,-'  '-.|  |,-'  '-.
`.  `-. | .--'|  .--',--.| .-. |'-.  .-'|  |'-.  .-'
.-'    |\ `--.|  |   |  || '-' '  |  |  |  |  |  |
`-----'  `---'`--'   `--'|  |-'   `--'  `--'  `--'
ScriptIt 1.2 by Anthony Maxwell.
View changelogs in change-logs.txt
""")

while True:
    text = input('BASIC > ')
    if text.lower() == "exit":
        exit()
    else:
        result, error = basic.run('<stdin>', text)

        if error: print(error.as_string())
        else: print(result)