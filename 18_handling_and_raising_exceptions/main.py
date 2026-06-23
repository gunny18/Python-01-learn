# Trying to read a file. Say I get this file as an input.
# I am anticipating my code to throw an error if that file is not found
# My task -> Say the task is to read a file, take its content and put in db. I will receive file name and db object as input
# If file name as corrupt in it (after opening it), raise error

def read_file_to_db(file_name, db):
    try:
        f = open(file_name, "r")
        if "corrupt" in f.name.lower():
            raise Exception("Corrupt file, not processing it")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        content = f.read()
        print(f"Putting {content} in DB object")
        f.close()
    finally:
        print("Closing and clearing out the db object")
        db = None

db = {
    "name":"postgres",
    "connection_url":"host@1234"
}
read_file_to_db("test_file.txt",db)
read_file_to_db("test.txt",db)
read_file_to_db("corrupt.txt",db)

