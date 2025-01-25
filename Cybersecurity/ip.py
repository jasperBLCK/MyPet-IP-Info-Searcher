import os
import requests
from pystyle import Colors, Colorate, Center
import pyfiglet

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            return data
        else:
            return "Информация по IP не найдена."
    else:
        return "Не удалось подключиться к API."

def print_ip_info(ip_info):
    banner = """
                  ▟█▙
                 ▟███▙
                ▟█████▙
               ▟███████▙
              ▂▔▀▜██████▙
             ▟██▅▂▝▜█████▙
            ▟█████████████▙
           ▟███████████████▙
          ▟█████████████████▙
         ▟███████████████████▙
        ▟█████████▛▀▀▜████████▙
       ▟████████▛      ▜███████▙
      ▟█████████        ████████▙
     ▟██████████        █████▆▅▄▃▂
    ▟██████████▛        ▜█████████▙
   ▟██████▀▀▀              ▀▀██████▙
  ▟███▀▘                       ▝▀███▙
 ▟▛▀                               ▀▜▙
    """

    centered_banner = Center.XCenter(banner)
    print(Colorate.Horizontal(Colors.black_to_white, centered_banner))

    ip = input(Colorate.Horizontal(Colors.black_to_white, "\nВведите IP для поиска: "))
    result = search_ip(ip)

    if isinstance(result, str):
        print(Colorate.Horizontal(Colors.black_to_red, result))
    else:
        formatted_text = f"""
        IP: {result.get('query')}
        Страна: {result.get('country')}
        Регион: {result.get('regionName')}
        Город: {result.get('city')} 
        Провайдер: {result.get('isp')}
        Время: {result.get('timezone')}
        Широта: {result.get('lat')}
        Долгота: {result.get('lon')}

{pyfiglet.figlet_format("jasperBLCK")}
        """

        print(Colorate.Horizontal(Colors.red_to_black, formatted_text))

        if result != "Информация по IP не найдена.":
            save_to_file = input(Colorate.Horizontal(Colors.black_to_white, "Хотите записать информацию в файл? (y/n): "))
            if save_to_file.lower() == 'y':
                with open("ip_info.txt", "w") as file:
                    file.write(formatted_text)
                    
                    print(Colorate.Horizontal(Colors.black_to_green, "Информация успешно записана в файл ip_info.txt!"))

    input(Colorate.Horizontal(Colors.white_to_black, "\nНажмите Enter..."))
    clear_console()

if __name__ == "__main__":
    print_ip_info("")

