from user_exceptions import CustomException

open('logs.txt', 'w', encoding='utf-8').close()

try:
    raise CustomException("TEST ERROR 1")
except CustomException as e:
    assert str(e) == "TEST ERROR 1"

with open('logs.txt', 'r', encoding='utf-8') as f:
    content = f.read()
assert "TEST ERROR 1\n" in content

try:
    raise CustomException("SECOND ERROR")
except CustomException:
    pass

with open('logs.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
assert lines[-2:] == ["TEST ERROR 1\n", "SECOND ERROR\n"]

print("TESTING CustomException IS COMPLETE!")
