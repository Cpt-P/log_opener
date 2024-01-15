import sys, os, platform
import subprocess

class colors:
    light_magneta = '\033[95m'
    end = '\033[0m'

def logs():
    if not platform.system().lower() == 'windows':
        print(colors.light_magneta + 'This script does not support Linux and macOS.' + colors.end)
        sys.exit(0)

    script_dir = os.path.dirname(os.path.realpath(__file__))
    logfile = os.path.join(script_dir, 'skl_log_opener.log')

    print('')
    
    print(colors.light_magneta + 'Disclaimer: This python script is not affiliated with, endorsed by, or sponsored by SKLauncher or its developers. SKLauncher is a product of skmedix.pl. This python script is a fan-made mod/launcher that uses SKLauncher as a base/dependency. The author of this python script is solely responsible for its content and functionality. Any issues, bugs, or feedback related to this python script should be directed to the author, not to SKLauncher or its developers. Use this python script at your own risk. The author is not liable for any damages or losses that may result from using this python script.' + colors.end)

    print('')

    print(colors.light_magneta + '''
    ---------------------------------------------
            Minecraft Log Opener v0 - Beta
    ---------------------------------------------''' + colors.end)

    print('')

    print(colors.light_magneta + 'Welcome to the Minecraft log opener by еврей(Python port of original by Cpt)...' + colors.end)

    while True:
        print('')

        print(colors.light_magneta + 'Please choose one of the following options: ' + colors.end)
        print(colors.light_magneta + 'Your selection will be copied to your clipboard.' + colors.end)

        print('')

        print(colors.light_magneta + '1. Open the SKlauncher log' + colors.end)
        print(colors.light_magneta + '2. Open the game log' + colors.end)
        print(colors.light_magneta + '3. Open the crash report' + colors.end)
        print(colors.light_magneta + '4. Exit' + colors.end)

        print('')

        choose = input(colors.light_magneta + 'Enter your choice: ' + colors.end)

        print('')

        print(colors.light_magneta + '(ported on python by intosins and еврей)' + colors.end)

        print('')

        with open(logfile, 'a') as file:
            file.write(f'User choice: {choose}\n')
            file.write(f'Date and time: {os.popen("echo %date% %time%").read().strip()}\n')

        if choose == '1':
            print(colors.light_magneta + 'Opening the SKlauncher log' + colors.end)
            with open(f'{os.getenv("APPDATA")}\\.minecraft\\sklauncher\\sklauncher_logs.txt', 'r') as sk_file:
                sk_log_content = sk_file.read()
                subprocess.Popen(['clip'], stdin=subprocess.PIPE).communicate(sk_log_content.encode('utf-8'))
                subprocess.Popen(['start', f'{os.getenv("APPDATA")}\\.minecraft\\sklauncher\\sklauncher_logs.txt'], shell=True)
        elif choose == '2':
            print(colors.light_magneta + 'Opening the game log' + colors.end)
            with open(f'{os.getenv("APPDATA")}\\.minecraft\\logs\\latest.log', 'r') as game_file:
                game_log_content = game_file.read()
                subprocess.Popen(['clip'], stdin=subprocess.PIPE).communicate(game_log_content.encode('utf-8'))
                subprocess.Popen(['start', f'{os.getenv("APPDATA")}\\.minecraft\\logs\\latest.log'], shell=True)
        elif choose == '3':
            crash_reports = sorted([f for f in os.listdir(f'{os.getenv("APPDATA")}\\.minecraft\\crash-reports') if f.endswith('.txt')], key=os.path.getmtime)
            if crash_reports:
                latest_crash_report = crash_reports[-1]
                print(colors.light_magneta + f'Opening the crash report {latest_crash_report}' + colors.end)
                with open(f'{os.getenv("APPDATA")}\\.minecraft\\crash-reports\\{latest_crash_report}', 'r') as crash_file:
                    crash_report_content = crash_file.read()
                    subprocess.Popen(['clip'], stdin=subprocess.PIPE).communicate(crash_report_content.encode('utf-8'))
                    subprocess.Popen(['start', f'{os.getenv("APPDATA")}\\.minecraft\\crash-reports\\{latest_crash_report}'], shell=True)
        elif choose == '4' or choose.lower() == 'exit' or choose.lower() == 'exit()' or choose == 'Exit':
            break
        else:
            print(colors.light_magneta + 'Invalid choice. Please try again.' + colors.end)
            input('Press Enter to continue...')
            continue

        print('')
        print(colors.light_magneta + 'Opening the selected log...' + colors.end)
        input(colors.light_magneta + 'Press Enter to continue...' + colors.end)
        print('')
        print(colors.light_magneta + 'Task complete... Log file can be found in the same directory as this Python script.' + colors.end)
        print('')
        print(colors.light_magneta + 'Feel free to provide your feedback. Thanks for using.' + colors.end)
        sys.exit(0)

if __name__ == '__main__':
    logs()