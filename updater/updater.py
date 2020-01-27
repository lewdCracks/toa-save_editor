import requests
import json
import os
import sys

def load_version_file(target_file):
    try:
        return json.load(open(target_file))
        print(f"[!] Loaded external json: {target_file}")
    except Exception as error:
        print(error)

def update_version_file(dic):
    json.dump(dic, open('data.json', 'w+'), indent=4)

def download(url):
    print("\n[~] Starting download...")
    req = requests.get(url)
    file_name = url.split("/")[-1]
    download_location = os.path.join(os.getcwd(), file_name)

    with open(download_location, 'wb+') as f:
            f.write(req.content)
            f.close()
    
    print(f"[+] Downloaded {file_name}\n")

def get_version_info(url, info):
    req = requests.get(url)
    data = json.loads(req.content.decode('utf-8'))
    return data['version_info'][f'{info}']

def remove_old_version(file):
    try:
        os.remove(file)
    except Exception as error:
        print(error)

def check_url(url):
    req = requests.get(url)
    if req == 200:
        return True
    else:
        return req

def main():
    main_data = load_version_file("data.json")
    info = main_data["version_info"]
    data_url = info['data_link']
    editor_url = info['editor_link']

    current_data_version = info['data_version']
    current_editor_version = info['editor_version']
    current_editor_name = info['editor']

    check = check_url(data_url)
    if check:
        pass
    else:
        print("Data Link is most likely no longer valid.\n\n\n", check)
        sys.exit(1)
    
    latest_data_version = get_version_info(info['data_link'], 'data_version')
    latest_editor_version = get_version_info(info['data_link'], 'editor_version')
    latest_editor_name = get_version_info(info['data_link'], 'editor')

    if latest_data_version != current_data_version:
        try:
            print(f"[!] data.json is not up to date: {current_editor_version}")
            download(data_url)
            print(f"[!] data.json is now up to date: {latest_data_version}")
        except Exception as error:
            print(error)
    else:
        print(f"[!] data.json is up to date: {latest_data_version}\n")

    if latest_editor_version != current_editor_version:
        try:
            print(f"[!] save_editor.exe is not up to date: {current_editor_version}")

            download(editor_url)
            remove_old_version(current_editor_name)
            info['editor_version'] = latest_editor_version
            info['editor'] = latest_editor_name
            update_version_file(main_data)

            print(f"[!] save_editor.exe is now up to date: {latest_editor_version}")

        except Exception as error:
            print(error)
    else:
        print(f"[!] save_editor.exe is up to date: {latest_editor_version}\n")


if __name__ == "__main__":
    main()
    os.system("pause")