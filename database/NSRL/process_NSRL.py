""" NSRL Modern Processing """
import time

NSRLFILE = "E:/modern.nsrl/NSRLFile.txt"

NSRL = {"SHA1": "",
        "MD5": "",
        "CRC32": "",
        "filename": "",
        "filesize": "",
        "productcode": "",
        "opsystemcode": "",
        "specialcode": ""
        }

TOTALLINES = 0

apps = dict()


def parseHashEntry(NSRL, file_content):
    file_data = file_content.split(",")
    file_fields = iter(file_data)
    for keys in NSRL:
        try:
            NSRL[keys] = next(file_fields)
        except StopIteration:
            print(TOTALLINES, NSRL)
    return NSRL


def process_NSRL(target_file):
    global TOTALLINES
    global apps
    with open(target_file, "rt", encoding="utf-8") as file:
        file_content = file.readline()  # remove header
        while file_content:
            file_content = file.readline()
            if not file_content:
                break
            app_info = parseHashEntry(NSRL, file_content)
            SHA1 = app_info["SHA1"]
            if apps.get(SHA1) is None:
                apps[SHA1] = ""
            TOTALLINES += 1
            if not(TOTALLINES % 10000000):
                print(f"Total lines processed: {TOTALLINES:,}")
                print(f"Total unique hashes: {len(apps):,}")
            # print(NSRL)


def main():
    start = time.perf_counter()
    process_NSRL(NSRLFILE)
    end = time.perf_counter()
    run_time = end - start
    print(f'Total time {run_time:.4f}')
    print(f'Total lines {TOTALLINES:,}')
    print(f'Unique hashes {len(apps):,}')


if __name__ == '__main__':
    main()
