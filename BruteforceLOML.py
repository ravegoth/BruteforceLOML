import datetime
import re
import json
import os

try:
    import requests
except ModuleNotFoundError:
    print("You need to install requests. Run this command: pip install requests")
    exit()
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    print("You need to install BeautifulSoup. Run this command: pip install beautifulsoup4")
    exit()
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("You need to install matplotlib. Run this command: pip install matplotlib")
    exit()
try:
    import colorama
except ModuleNotFoundError:
    print("You need to install colorama. Run this command: pip install colorama")
    exit()

if __name__ != "__main__":
    print('This file is not meant to be imported.')
    exit()

art = """ _             _        __
| |__ _ _ _  _| |_ ___ / _|___ _ _ __ ___
| '_ | '_| || |  _/ -_|  _/ _ | '_/ _/ -_)
|_.__|___ \___|_______|_| ______| \__\___|
| |  / _ \|  \/  | |     / |__ /
| |_| (_) | |\/| | |__  < < |_ \\
|____\___/|_|  |_|____|  \_|___/
""".replace("_", colorama.Fore.RED + "_" + colorama.Fore.RESET) \
.replace("|", colorama.Fore.LIGHTMAGENTA_EX + "|" + colorama.Fore.RESET) \
.replace("/", colorama.Fore.MAGENTA + "/" + colorama.Fore.RESET) \
.replace("\\", colorama.Fore.BLUE + "\\" + colorama.Fore.RESET) \
.replace("(", colorama.Fore.RED + "(" + colorama.Fore.RESET) \
.replace(")", colorama.Fore.RED + ")" + colorama.Fore.RESET) \
.replace(" ", colorama.Fore.RED + " " + colorama.Fore.RESET) \
.replace(")", colorama.Fore.RED + ")" + colorama.Fore.RESET) \
.replace(":", colorama.Fore.RED + ":" + colorama.Fore.RESET) \
.replace("-", colorama.Fore.RED + "-" + colorama.Fore.RESET) \
.replace("=", colorama.Fore.RED + "=" + colorama.Fore.RESET) \
.replace(">", colorama.Fore.RED + ">" + colorama.Fore.RESET) \
.replace("<", colorama.Fore.RED + "<" + colorama.Fore.RESET) \
.replace("!", colorama.Fore.RED + "!" + colorama.Fore.RESET) \
.replace("?", colorama.Fore.RED + "?" + colorama.Fore.RESET) \
.replace(".", colorama.Fore.RED + "." + colorama.Fore.RESET) \
.replace(",", colorama.Fore.RED + "," + colorama.Fore.RESET) \
.replace("'", colorama.Fore.RED + "'" + colorama.Fore.RESET) \
.replace('"', colorama.Fore.RED + '"' + colorama.Fore.RESET) \

print(art)
print("BruteforceLOML - by www.tra1an.com".replace("LOML", colorama.Fore.RED + "LOML" + colorama.Fore.RESET))

my_day = input("Your day of birth: --> ")
my_month = input("Your month of birth: --> ")
my_year = input("Your year of birth: --> ")
print("Your birth date is: " + colorama.Fore.GREEN + "{}/{}/{}".format(my_day, my_month, my_year) + colorama.Fore.RESET)

if os.path.exists("all_dates_for_{}_{}_{}.txt".format(my_day, my_month, my_year)):
    print("You already have a file with this date. Do you want to continue?")
    print("If you continue, the program will continue from where it left off if you give it the same inputs.")
    print("If you want to start from the beginning, type " + colorama.Fore.RED + "delete" + colorama.Fore.RESET + ".")
    print("If you want to continue, press enter.")
    choice = input("Your choice: --> ")
    if choice == "delete":
        for file in os.listdir():
            if file.endswith(".txt"):
                os.remove(file)
        print("All .txt files deleted.")
        for file in os.listdir():
            if file.endswith(".html"):
                os.remove(file)
        print("All .html files deleted.")

print(colorama.Fore.YELLOW + "Now you need to find the hour and minute of birth" + colorama.Fore.RESET)
print("YOU NEED TO CONVERT YOUR TIME TO GMT +0".replace("GMT +0", colorama.Fore.RED + "GMT +0" + colorama.Fore.RESET))
my_hour = input("Your hour of birth (from 0 to 23): (GMT +0) --> ")
my_minute = input("Your minute of birth (from 0 to 59): --> ")
print("What's the minimum year you want the partner to be born in?")
startingYear = input("Minimum year to check: --> ")
print("What's the maximum year you want the partner to be born in?")
endingYear = input("Maximum year to check: --> ")

print("\nChecking coords...")
my_ip = requests.get("https://api.ipify.org").text
api = "https://geolocation-db.com/json/{}&position=true".format(my_ip)
response = requests.get(api)
contents = response.text

geolocation = json.loads(contents)
detected_latitude = str(geolocation["latitude"])
detected_longitude = str(geolocation["longitude"])

detected_latitude_big = int(str(detected_latitude).split(".")[0])
detected_latitude_minutes = int(str(detected_latitude).split(".")[1])
detected_longitude_big = int(str(detected_longitude).split(".")[0])
detected_longitude_minutes = int(str(detected_longitude).split(".")[1])

detected_latitude_minutes = int(str(detected_latitude_minutes)[:2])
detected_longitude_minutes = int(str(detected_longitude_minutes)[:2])

# too precise will break the program
detected_longitude_minutes = 0
detected_latitude_minutes = 0

print("Your detected coords are: {}.{}°N {}.{}°E".format(detected_latitude_big, detected_latitude_minutes, detected_longitude_big, detected_longitude_minutes))

print("What's the latitude of the city you were born in? (example: 12.34)")
latitude_input = input("Your latitude: --> ")
try:
    my_latitude = int(latitude_input.split(".")[0])
    my_latitude_minutes = int(latitude_input.split(".")[1])
except IndexError:
    my_latitude = int(latitude_input)
    my_latitude_minutes = 0
print("What's the longitude of the city you were born in? (example: 23.45)")
longitude_input = input("Your longitude: --> ")
try:
    my_longitude = int(longitude_input.split(".")[0])
    my_longitude_minutes = int(longitude_input.split(".")[1])
except IndexError:
    my_longitude = int(longitude_input)
    my_longitude_minutes = 0
print("What's the latitude you want the partner to be born in? (example: 12.34)")
latitude_input = input("Partner's latitude: --> ")
try:
    her_latitude = int(latitude_input.split(".")[0])
    her_latitude_minutes = int(latitude_input.split(".")[1])
except IndexError:
    her_latitude = int(latitude_input)
    her_latitude_minutes = 0
print("What's the longitude you want the partner to be born in? (example: 23.45)")
longitude_input = input("Partner's longitude: --> ")
try:
    her_longitude = int(longitude_input.split(".")[0])
    her_longitude_minutes = int(longitude_input.split(".")[1])
except IndexError:
    her_longitude = int(longitude_input)
    her_longitude_minutes = 0

print("Your coords are: {}°{}'N {}°{}'E".format(my_latitude, my_latitude_minutes, my_longitude, my_longitude_minutes))
print("Partner's coords are: {}°{}'N {}°{}'E".format(her_latitude, her_latitude_minutes, her_longitude, her_longitude_minutes))

print(colorama.Fore.CYAN + "Program will now start.")
print("It will take a lot of time, so be patient.".replace("a lot of time", colorama.Fore.RED + "a lot of time" + colorama.Fore.RESET))
print("If your internet connection is slow, it will take even more time.".replace("slow", colorama.Fore.RED + "slow" + colorama.Fore.RESET))
print("It will check all the dates between 01/01/{} and 31/12/{} for the best and worst scores.".format(startingYear, endingYear).replace("01/01/{}".format(startingYear), colorama.Fore.GREEN + "01/01/{}".format(startingYear) + colorama.Fore.RESET).replace("31/12/{}".format(endingYear), colorama.Fore.GREEN + "31/12/{}".format(endingYear) + colorama.Fore.RESET))
print("Big scores = good compatibility. Small scores = bad compatibility.".replace("Big scores", colorama.Fore.GREEN + "Big scores" + colorama.Fore.RESET).replace("Small scores", colorama.Fore.RED + "Small scores" + colorama.Fore.RESET))
print("If you want to stop the program, press CTRL + C.".replace("CTRL + C", colorama.Fore.RED + "CTRL + C" + colorama.Fore.RESET))
print("If you run program again it will continue from where it left off, BUT only if")
print("you don't delete the files it generated and the inputs are the same\n\n")

print("Press enter to start the program...")
input()

my_day = int(my_day)
my_month = int(my_month)
my_year = int(my_year)
my_hour = int(my_hour)
my_minute = int(my_minute)
startingYear = int(startingYear)
endingYear = int(endingYear)

def calculate(my_day, my_month, my_year, my_hour, my_minute, her_day, her_month, her_year, her_hour, her_minute, my_latitude, my_latitude_minutes, my_longitude, my_longitude_minutes, her_latitude, her_latitude_minutes, her_longitude, her_longitude_minutes, returnContent=False):
    base_url = 'https://horoscopes.astro-seek.com/calculate-love-compatibility/?send_calculation=1'
    my_details = f'&muz_narozeni_den={my_day}&muz_narozeni_mesic={my_month}&muz_narozeni_rok={my_year}&muz_narozeni_hodina={my_hour:02d}&muz_narozeni_minuta={my_minute:02d}&muz_narozeni_city=Program%2C+Romania&muz_narozeni_mesto_hidden=Program&muz_narozeni_stat_hidden=RO&muz_narozeni_podstat_kratky_hidden=&muz_narozeni_podstat_hidden=Program&muz_narozeni_input_hidden=&muz_narozeni_podstat2_kratky_hidden=&muz_narozeni_podstat3_kratky_hidden=&muz_narozeni_sirka_stupne={my_latitude}&muz_narozeni_sirka_minuty={my_latitude_minutes}&muz_narozeni_sirka_smer=0&muz_narozeni_delka_stupne={my_longitude}&muz_narozeni_delka_minuty={my_longitude_minutes}&muz_narozeni_delka_smer=0'
    her_details = f'&zena_narozeni_den={her_day}&zena_narozeni_mesic={her_month}&zena_narozeni_rok={her_year}&zena_narozeni_hodina={her_hour:02d}&zena_narozeni_minuta={her_minute:02d}&zena_narozeni_no_cas=on&zena_narozeni_city=Program%2C+Romania&zena_narozeni_mesto_hidden=Program&zena_narozeni_stat_hidden=RO&zena_narozeni_podstat_kratky_hidden=&zena_narozeni_podstat_hidden=Program&zena_narozeni_input_hidden=&zena_narozeni_podstat2_kratky_hidden=&zena_narozeni_podstat3_kratky_hidden=&zena_narozeni_sirka_stupne={her_latitude}&zena_narozeni_sirka_minuty={her_latitude_minutes}&zena_narozeni_sirka_smer=0&zena_narozeni_delka_stupne={her_longitude}&zena_narozeni_delka_minuty={her_longitude_minutes}&zena_narozeni_delka_smer=0'
    other_details = '&switch_interpretations=3&house_system=placidus&hid_fortune=1&hid_fortune_check=on&hid_vertex=1&hid_vertex_check=on&hid_chiron=1&hid_chiron_check=on&hid_lilith=1&hid_lilith_check=on&hid_uzel=1&hid_uzel_check=on&uhel_orbis=&hide_aspects=0#tabs_redraw'
    url = f'{base_url}{my_details}{her_details}{other_details}'
    response = requests.get(url)
    contents = response.text
    soup = BeautifulSoup(contents, 'html.parser')
    aspect_divs = soup.find_all('div', class_='cl')
    lines = []
    for div in aspect_divs:
        if "style" in div.attrs and div.attrs["style"] == "overflow: hidden; height: 26px;":
            text_content = div.get_text(strip=True)
            if "(exact)" not in text_content:
                lines.append(text_content)
    loving = re.findall(r"(\d+)xLoving", lines[0])
    key = re.findall(r"(\d+)xKey", lines[1])
    passion = re.findall(r"(\d+)xPassion", lines[2])
    emotional_pain = re.findall(r"(\d+)xEmotional pain", lines[3])
    easy = re.findall(r"(\d+)xEasy", lines[4])
    conflict = re.findall(r"(\d+)xConflict", lines[5])
    combination = re.findall(r"(\d+)x", lines[6])
    score = int(loving[0]) * 3 + int(passion[0]) * 2 + int(easy[0]) * 2 - int(emotional_pain[0]) * 3 - int(conflict[0]) * 2 + int(combination[0]) * 1
    if returnContent:
        return contents
    return score

highscore = -1
lowscore = 1000000

imported_highscore = -1
imported_lowscore = 1000000

dictionary_for_graph = {}

frequency_distribution = {}

if not os.path.exists("all_dates_for_{}_{}_{}.txt".format(my_day, my_month, my_year)):
    with open("all_dates_for_{}_{}_{}.txt".format(my_day, my_month, my_year), "w") as f:
        f.write("")

else:
    with open("all_dates_for_{}_{}_{}.txt".format(my_day, my_month, my_year), "r") as f:
        imported_highscore = -1
        imported_lowscore = 1000000
        
        for line in f.readlines():
            dictionary_for_graph[line.split(" - ")[0]] = int(line.split(" - ")[1])
            if line.split(" - ")[1] in frequency_distribution:
                frequency_distribution[line.split(" - ")[1]] += 1
            else:
                frequency_distribution[line.split(" - ")[1]] = 1
            
            if int(line.split(" - ")[1]) > imported_highscore:
                imported_highscore = int(line.split(" - ")[1])
            if int(line.split(" - ")[1]) < imported_lowscore:
                imported_lowscore = int(line.split(" - ")[1])

if imported_highscore > highscore:
    highscore = imported_highscore
if imported_lowscore < lowscore:
    lowscore = imported_lowscore

for year in range(startingYear, endingYear + 1):
    for month in range(1, 13):
        
        time_now = datetime.datetime.now()
        
        for day in range(1, 32):
            hour = 0
            minute = 0
            her_hour = 0
            her_minute = 0
            
            if os.path.exists("all_dates_for_{}_{}_{}.txt".format(my_day, my_month, my_year)):
                if "{}/{}/{}".format(day, month, year) in open("all_dates_for_{}_{}_{}.txt".format(my_day, my_month, my_year)).read():
                    continue
            
            try:
                score = calculate(my_day, my_month, my_year, my_hour, my_minute, day, month, year, her_hour, her_minute, my_latitude, my_latitude_minutes, my_longitude, my_longitude_minutes, her_latitude, her_latitude_minutes, her_longitude, her_longitude_minutes)            
            except IndexError:
                # print("This date is not valid: {}/{}/{}".format(day, month, year))
                continue
            
            if score > 0: visual = "+" * score
            else: visual = "-" * abs(score)
            print("Checking: {}/{}/{}, score: {}\t[{}]".format(day, month, year, score, visual))
            dictionary_for_graph["{}/{}/{}".format(day, month, year)] = score
            
            if score in frequency_distribution:
                frequency_distribution[score] += 1
            else:
                frequency_distribution[score] = 1
            
            if score > highscore:
                highscore = score
                print("Highscore for partners born in: {}-{}-{}".format(year, month, day))
                if os.path.exists("highscores_{}_{}_{}.txt".format(my_day, my_month, my_year)):
                    with open("highscores_{}_{}_{}.txt".format(my_day, my_month, my_year), "a") as f:
                        f.write("{}/{}/{} - {}\n".format(day, month, year, score))
                else:
                    with open("highscores_{}_{}_{}.txt".format(my_day, my_month, my_year), "w") as f:
                        f.write("{}/{}/{} - {}\n".format(day, month, year, score))
                
                with open("score{}_for{}_{}_{}.html".format(score, my_day, my_month, my_year), "w", encoding="utf-8") as f:
                    f.write(calculate(my_day, my_month, my_year, my_hour, my_minute, day, month, year, her_hour, her_minute, my_latitude, my_latitude_minutes, my_longitude, my_longitude_minutes, her_latitude, her_latitude_minutes, her_longitude, her_longitude_minutes, returnContent=True))
            if score < lowscore:
                lowscore = score
                print("Lowscore for partners born in: {}-{}-{}".format(year, month, day))
                if os.path.exists("lowscores_{}_{}_{}.txt".format(my_day, my_month, my_year)):
                    with open("lowscores_{}_{}_{}.txt".format(my_day, my_month, my_year), "a") as f:
                        f.write("{}/{}/{} - {}\n".format(day, month, year, score))
                else:
                    with open("lowscores_{}_{}_{}.txt".format(my_day, my_month, my_year), "w") as f:
                        f.write("{}/{}/{} - {}\n".format(day, month, year, score))
            
            if os.path.exists("score{}_for{}_{}_{}.txt".format(score, my_day, my_month, my_year)):
                with open("score{}_for{}_{}_{}.txt".format(score, my_day, my_month, my_year), "r") as f:
                    if "{}/{}/{}".format(day, month, year) not in f.read():
                        with open("score{}_for{}_{}_{}.txt".format(score, my_day, my_month, my_year), "a") as f:
                            f.write("{}/{}/{}\n".format(day, month, year))
            else:
                with open("score{}_for{}_{}_{}.txt".format(score, my_day, my_month, my_year), "w") as f:
                    f.write("{}/{}/{}\n".format(day, month, year))
            
            with open("all_dates_for_{}_{}_{}.txt".format(my_day, my_month, my_year), "a") as f:
                f.write("{}/{}/{} - {}\n".format(day, month, year, score))
        
        time_check = datetime.datetime.now()
        print("Month passed in {} seconds".format(time_check - time_now))
        months_left = 12 - month
        months_left += (endingYear - year) * 12
        months_left += 1
        time_left = (time_check - time_now) * months_left
        print("Estimated time left: {}".format(time_left))

print("Printing a plot with all the scores...")
plt.plot(dictionary_for_graph.keys(), dictionary_for_graph.values())
plt.show()

frequency_distribution = {int(k): v for k, v in frequency_distribution.items()}
frequency_distribution = dict(sorted(frequency_distribution.items()))

print("Printing a bar chart with the frequency distribution...")
plt.bar(frequency_distribution.keys(), frequency_distribution.values())
plt.show()

dictionary_for_month_year = {}

with open("all_dates_for_{}_{}_{}.txt".format(my_day, my_month, my_year), "r") as f:
    for line in f.readlines():
        month_year = line.split(" - ")[0].split("/")[1] + "/" + line.split(" - ")[0].split("/")[2]
        
        if month_year in dictionary_for_month_year:
            dictionary_for_month_year[month_year].append(int(line.split(" - ")[1]))
        else:
            dictionary_for_month_year[month_year] = [int(line.split(" - ")[1])]

for key in dictionary_for_month_year:
    dictionary_for_month_year[key] = sum(dictionary_for_month_year[key]) / len(dictionary_for_month_year[key])

print("Printing a line chart with the average score for each month...")
plt.xticks(rotation=90)
plt.plot(dictionary_for_month_year.keys(), dictionary_for_month_year.values())
plt.show()

print("Deleting debug html files...")
for file in os.listdir():
    if file.endswith(".html"):
        os.remove(file)
print("Done")

print("--- STATS ---")
print("Highscore: {}".format(highscore))
print("Dates for highscore: (you need to date someone born in one of these dates)")
for file in os.listdir():
    if file.startswith("score{}_for{}_{}_{}.txt".format(highscore, my_day, my_month, my_year)):
        with open(file, "r") as f:
            print(f.read())
print("Lowscore: {}".format(lowscore))
print("Dates for lowscore: (you MUST NOT date someone born in one of these dates)")
for file in os.listdir():
    if file.startswith("score{}_for{}_{}_{}.txt".format(lowscore, my_day, my_month, my_year)):
        with open(file, "r") as f:
            print(f.read())

print("Total number of dates: {}".format(len(dictionary_for_graph)))
print("Total number of scores: {}".format(len(frequency_distribution)))

print("Best month: {}".format(max(dictionary_for_month_year, key=dictionary_for_month_year.get)))
print("Best month score: {}".format(max(dictionary_for_month_year.values())))

print("Worst month: {}".format(min(dictionary_for_month_year, key=dictionary_for_month_year.get)))
print("Worst month score: {}".format(min(dictionary_for_month_year.values())))

print("Average score: {}".format(sum(dictionary_for_graph.values()) / len(dictionary_for_graph)))

print("\nProgram finished.\nTo check the highscores and lowscores,\ncheck the files highscores_{}_{}_{}.txt and lowscores_{}_{}_{}.txt".format(my_day, my_month, my_year, my_day, my_month, my_year))
print("To check the dates for a specific score X,\ncheck the files scoreX_for{}_{}_{}.txt".format(my_day, my_month, my_year))
print("You should move all the generated files in a folder,\nbecause the program will generate a lot of files if you will run it again.")
print("You can also check the file all_dates_for_{}_{}_{}.txt to see\nall the dates and scores (basically the history of this console)".format(my_day, my_month, my_year))
