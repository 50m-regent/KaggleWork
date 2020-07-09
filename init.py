import os

def url():
    return input("URL: ")

def title_script(url_name):
    title = url_name.split("/")[4]
    print("Dir Name: ", title)

    if os.path.isdir("Competition/" + title):
        print("Already created!")
    else:
        os.mkdir("Competition/" + title)
        os.mkdir("Competition/" + title + "/data")
        os.mkdir("Competition/" + title + "/model")
        os.mkdir("Competition/" + title + "/notebook")
        os.mkdir("Competition/" + title + "/Log")

        with open("Competition/" + title + "/README.md", "w") as f:
            f.write("# " + title)

        print("Done!")

if __name__ == "__main__":
    title_script(url())
