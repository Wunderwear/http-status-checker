import requests
import concurrent.futures

def check_link(link):
    response = requests.get(link)
    if response.status_code == 200:
        print(f"{link} ok")
        create_folder = open("result_ok.txt", "a") #file result
        create_folder.write(f'{link}\n')
    else:
        print(f"{link} bad")
        create_folder = open("result_bad.txt", "a") #file result
        create_folder.write(f'{link}\n')
def check_links(list):
    with open(list, 'r') as file:
        links = file.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor(50) as executor: #thread
        executor.map(check_link, links)

print(("""
 /$$      /$$                           /$$                                                                
| $$  /$ | $$                          | $$                                                                
| $$ /$$$| $$ /$$   /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$  /$$  /$$  /$$  /$$$$$$   /$$$$$$   /$$$$$$ 
| $$/$$ $$ $$| $$  | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$ | $$ | $$ /$$__  $$ |____  $$ /$$__  $$
| $$$$_  $$$$| $$  | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/| $$ | $$ | $$| $$$$$$$$  /$$$$$$$| $$  \__/
| $$$/ \  $$$| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$      | $$ | $$ | $$| $$_____/ /$$__  $$| $$      
| $$/   \  $$|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$      |  $$$$$/$$$$/|  $$$$$$$|  $$$$$$$| $$      
|__/     \__/ \______/ |__/  |__/ \_______/ \_______/|__/       \_____/\___/  \_______/ \_______/|__/      
                                                                                                                                                                                                                                                                                                                         
 GitHub : https://github.com/Wunderwear                                                                                                                                                                                                 
"""))

list = input(f" Input File List : ")
check_links(list)
