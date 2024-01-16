#include <iostream>
#include <fstream>
#include <string>
#include <ctime>
#include <windows.h> 
#include <shlobj.h> 
#include <shlwapi.h> 
#include <filesystem> 

using namespace std;

string get_current_datetime()
{
    time_t now = time(0);
    tm *ltm = localtime(&now);
    char buffer[80];
    strftime(buffer, 80, "%Y-%m-%d %H-%M-%S", ltm);
    return string(buffer);
}

string get_appdata_path()
{
    char buffer[MAX_PATH];
    SHGetFolderPathA(NULL, CSIDL_APPDATA, NULL, 0, buffer);
    return string(buffer);
}

string get_file_name(string file_path)
{
    size_t pos = file_path.find_last_of("\\/");
    if (pos == string::npos)
        return file_path;
    else
        return file_path.substr(pos + 1);
}

// Thx ChatGPT
void display_file(string file_path)
{

    ifstream file(file_path);
    if (!file.is_open())
    {
        cout << "Error: Cannot open file " << file_path << endl;
        return;
    }

    string file_name = get_file_name(file_path);

    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);

    SetConsoleTitleA(file_name.c_str());

    SMALL_RECT windowSize = {0, 0, 79, 24};
    SetConsoleWindowInfo(hConsole, TRUE, &windowSize);

    COORD bufferSize = {80, 25};
    SetConsoleScreenBufferSize(hConsole, bufferSize);

    system("cls");

    for (int i = 0; i < file_name.length(); i++)
    {
        cout << file_name[i];
        Sleep(50); 
    }
    cout << endl;

    string file_content((istreambuf_iterator<char>(file)), istreambuf_iterator<char>()); // It has an issue here. No fix for now.

    cout << file_content << "\n";

    file.close();

    if (OpenClipboard(NULL))
    {
        EmptyClipboard();

        HGLOBAL hglbCopy = GlobalAlloc(GMEM_MOVEABLE, (file_content.length() + 1) * sizeof(TCHAR));
        if (hglbCopy != NULL)
        {
            LPTSTR lptstrCopy = (LPTSTR)GlobalLock(hglbCopy);
            memcpy(lptstrCopy, file_content.c_str(), file_content.length() * sizeof(TCHAR));
            lptstrCopy[file_content.length()] = (TCHAR)0; 
            GlobalUnlock(hglbCopy);

            SetClipboardData(CF_TEXT, hglbCopy);
        }

        CloseClipboard();
    }

    cout << "The file content has been copied to the clipboard." << endl;
}

// Thx ChatGPT
void create_log_file(string log_path, string action, string file_path)
{
    ofstream log(log_path, ios::app);
    if (!log.is_open())
    {
        cout << "Error: Cannot open log file " << log_path << endl;
        return;
    }

    string datetime = get_current_datetime();

    log << datetime << " - " << action << " - " << file_path << endl;

    log.close();
}

int main()
{
    string appdata = get_appdata_path();

    string launcher_log = appdata + "\\.minecraft\\sklauncher\\sklauncher_logs.txt";
    string game_log = appdata + "\\.minecraft\\logs\\latest.log";

    string crash_report;

    for (const auto &entry : std::filesystem::directory_iterator(appdata + "\\.minecraft\\crash-reports"))
    {
        if (entry.is_regular_file() && entry.path().extension() == ".txt")
        {
            if (entry.path().filename().string() > crash_report)
            {
                crash_report = entry.path().filename().string();
            }
        }
    }

    crash_report = appdata + "\\.minecraft\\crash-reports\\" + crash_report;

    string log_file = "log-" + get_current_datetime() + ".txt";

    cout << "Disclaimer: This batch script is not affiliated with, endorsed by, or sponsored by SKLauncher or its developers. SKLauncher is a product of skmedix.pl. This batch script is a fan-made mod/launcher that uses SKLauncher as a base/dependency. The author of this batch script is solely responsible for its content and functionality. Any issues, bugs, or feedback related to this batch script should be directed to the author, not to SKLauncher or its developers. Use this batch script at your own risk. The author is not liable for any damages or losses that may result from using this batch script." << endl;
    cout << "\n";
    cout << "---------------------------------------------" << endl;
    cout << "Minecraft Log Opener v0 - Beta - C++ Port" << endl;
    cout << "---------------------------------------------" << endl;
    cout << "Welcome to the Minecraft Log Opener by Cpt..." << endl;
    cout << "\n";
    cout << "Please choose one of the following options:" << endl;
    cout << "Your selection will be copied to your clipboard." << endl;
    cout << "\n";
    cout << "1. View the launcher log" << endl;
    cout << "2. View the game log" << endl;
    cout << "3. View the crash report" << endl;
    cout << "4. Exit the program" << endl;

    int choice;

    while (true)
    {
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice < 1 || choice > 4)
        {
            cout << "Invalid choice. Please try again." << endl;
            continue;
        }

        switch (choice)
        {
        case 1:
            display_file(launcher_log);
            create_log_file(log_file, "Viewed", launcher_log);
            break;
        case 2:
            display_file(game_log);
            create_log_file(log_file, "Viewed", game_log);
            break;
        case 3:
            display_file(crash_report);
            create_log_file(log_file, "Viewed", crash_report);
            break;
        case 4:
            create_log_file(log_file, "Exited", "N/A");
            cout << "Thank you for using the Minecraft Log Viewer. Goodbye!" << endl;
            return 0;
        }

        cout << "Press any key to continue..." << endl;
        cin.ignore();
        cin.get();
    }

    return 0;
}
