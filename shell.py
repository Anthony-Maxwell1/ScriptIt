import basic

print("""                                                                         
 ,---.               ,--.         ,--.  ,--.  ,--.       ,--.     ,--.   
'   .-'  ,---.,--.--.`--' ,---. ,-'  '-.|  |,-'  '-.    /   |    /    \  
`.  `-. | .--'|  .--',--.| .-. |'-.  .-'|  |'-.  .-'    `|  |   |  ()  | 
.-'    |\ `--.|  |   |  || '-' '  |  |  |  |  |  |       |  |.--.\    /  
`-----'  `---'`--'   `--'|  |-'   `--'  `--'  `--'       `--''--' `--'
ScriptIt 1.0 by Anthony Maxwell.
""")

while True:
    text = input('BASIC > ')
    if text.lower() == "exit":
        exit()
    else:
        result, error = basic.run('<stdin>', text)

        if error: print(error.as_string())
        else: print(result)