nums = {"one": '"один"', "two": '"два"', "three": '"три"', "four": '"четыре"', "five": '"пять"',
        "six": 'шесть"', "seven": 'семь"', "eight": '"восемь"', "nine": '"девять"', "ten": '"десять"'}


def num_translate(k):
    print(nums.get(k))


num_translate("two")
num_translate("five")
num_translate("eight")
num_translate("twelve")
