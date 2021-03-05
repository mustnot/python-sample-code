import subprocess


def tail(file_path):
    cmd = "tail -f {}".format(file_path)
    with subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:
        while True:
            out = p.stdout.readline().decode("utf-8")
            print(out)


if __name__ == "__main__":
    tail("/var/log/nginx/access.log")