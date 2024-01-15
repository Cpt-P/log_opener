import sys, os, platform
import subprocess
import colorama 
import loguru 
import datetime 
import webbrowser 

colorama.init() 

def logs():
    if not platform.system().lower() == 'windows':
        print(colorama.Fore.MAGENTA + 'This script does not support Linux and macOS.' + colorama.Style.RESET_ALL)
        sys.exit(0)

    script_dir = os.path.dirname(os.path.realpath(__file__))
    logfile = os.path.join(script_dir, 'skl_log_opener.log')

    print('')

    print(colorama.Fore.MAGENTA + 'Disclaimer: This python script is not affiliated with, endorsed by, or sponsored by SKLauncher or its developers. SKLauncher is a product of skmedix.pl. This python script is a fan-made mod/launcher that uses SKLauncher as a base/dependency. The author of this python script is solely responsible for its content and functionality. Any issues, bugs, or feedback related to this python script should be directed to the author, not to SKLauncher or its developers. Use this python script at your own risk. The author is not liable for any damages or losses that may result from using this python script.' + colorama.Style.RESET_ALL)

    print('')

    print(colorama.Fore.MAGENTA + '''
    ---------------------------------------------
            Minecraft Log Opener v0 - Beta
    ---------------------------------------------''' + colorama.Style.RESET_ALL)

    print('')

    print(colorama.Fore.MAGENTA + 'Welcome to the Minecraft log opener by еврей(Python port of original by Cpt)...' + colorama.Style.RESET_ALL)

    logger = loguru.logger
    logger.add(logfile, format="{time} {message}", level="INFO", rotation="1 MB")

    while True:
        print('')

        print(colorama.Fore.MAGENTA + 'Please choose one of the following options: ' + colorama.Style.RESET_ALL)
        print(colorama.Fore.MAGENTA + 'Your selection will be copied to your clipboard.' + colorama.Style.RESET_ALL)

        print('')

        print(colorama.Fore.MAGENTA + '1. Open the SKlauncher log' + colorama.Style.RESET_ALL)
        print(colorama.Fore.MAGENTA + '2. Open the game log' + colorama.Style.RESET_ALL)
        print(colorama.Fore.MAGENTA + '3. Open the crash report' + colorama.Style.RESET_ALL)
        print(colorama.Fore.MAGENTA + '4. Exit' + colorama.Style.RESET_ALL)

        print('')

        choose = input(colorama.Fore.MAGENTA + 'Enter your choice: ' + colorama.Style.RESET_ALL)

        print('')

        logger.info(f'User choice: {choose}')
        logger.info(f'Date and time: {datetime.datetime.now()}')

        minecraft_path = os.path.join(os.environ.get("APPDATA"), ".minecraft")

        if choose == '1':
            print(colorama.Fore.MAGENTA + 'Opening the SKlauncher log' + colorama.Style.RESET_ALL)
            sk_log_path = os.path.join(minecraft_path, "sklauncher", "sklauncher_logs.txt")
            with open(sk_log_path, 'r') as sk_file:
                sk_log_content = sk_file.read()
                subprocess.Popen(['clip'], stdin=subprocess.PIPE).communicate(sk_log_content.encode('utf-8'))
                webbrowser.open(sk_log_path) # open the log file in the default application
        elif choose == '2':
            print(colorama.Fore.MAGENTA + 'Opening the game log' + colorama.Style.RESET_ALL)
            game_log_path = os.path.join(minecraft_path, "logs", "latest.log")
            with open(game_log_path, 'r') as game_file:
                game_log_content = game_file.read()
                subprocess.Popen(['clip'], stdin=subprocess.PIPE).communicate(game_log_content.encode('utf-8'))
                webbrowser.open(game_log_path) 
        elif choose == '3':
            crash_reports = sorted([f for f in os.listdir(os.path.join(minecraft_path, "crash-reports")) if f.endswith('.txt')], key=os.path.getmtime)
            if crash_reports:
                latest_crash_report = crash_reports[-1]
                print(colorama.Fore.MAGENTA + f'Opening the crash report {latest_crash_report}' + colorama.Style.RESET_ALL)
                crash_report_path = os.path.join(minecraft_path, "crash-reports", latest_crash_report)
                with open(crash_report_path, 'r') as crash_file:
                    crash_report_content = crash_file.read()
                    subprocess.Popen(['clip'], stdin=subprocess.PIPE).communicate(crash_report_content.encode('utf-8'))
                    webbrowser.open(crash_report_path) 
        elif choose == '4' or choose.lower() == 'exit' or choose.lower() == 'exit()' or choose == 'Exit':
            break
        else:
            print(colorama.Fore.MAGENTA + 'Invalid choice. Please try again.' + colorama.Style.RESET_ALL)
            input('Press Enter to continue...')
            continue

        print('')
        print(colorama.Fore.MAGENTA + 'Opening the selected log...' + colorama.Style.RESET_ALL)
        input(colorama.Fore.MAGENTA + 'Press Enter to continue...' + colorama.Style.RESET_ALL)
        print('')
        print(colorama.Fore.MAGENTA + 'Task complete... Log file can be found in the same directory as this Python script.' + colorama.Style.RESET_ALL)
        print('')
        print(colorama.Fore.MAGENTA + 'Feel free to provide your feedback. Thanks for using.' + colorama.Style.RESET_ALL)
        sys.exit(0)

if __name__ == '__main__':
    logs()
