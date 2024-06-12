# BruteforceLOML

![logo](./logo.png)

#### **BruteforceLOML** is a python3 script that offers a unique approach to exploring astrological compatibility by determining the most auspicious birth dates for a potential partner.
This tool is meticulously crafted for those who place a high value on astrological signs and their influence on relationships.
BruteforceLOML analyzes a range of dates, providing users with a tailored list of potential partners' birth dates that are astrologically aligned for maximum compatibility.
It's a perfect blend of technology and astrology, designed for individuals seeking deeper, star-aligned connections.

## Features

- Generates compatibility reports including high scores and low scores. For each score, there's a file with a list of dates that have that score
- Visualizes the distribution of compatibility scores
- Visualizes how the score changes over time
- Visualizes the a chart of the average score every month within the range of dates
- Automatically fetches user's geolocation data for easier inputs
- Saves the whole data for further analysis. So you can check dates instantly by searching for them in the generated text files
- Real time ascii graph of scores in console
- Estimates time remaining (1 year takes about 4 minute to process, depending on your internet speed)

## Installation

To run BruteforceLOML, **ensure you have the following Python libraries installed**:
- **requests**
- **BeautifulSoup4**
- **matplotlib**
- **colorama**

You can install these using pip:

```bash
pip install requests beautifulsoup4 matplotlib colorama
```

Then you can just download the script and run it (or clone the repo)

## Usage

```bash
python BruteforceLOML.py
```
Input your **birth details, your coordinates, and the range of dates you want to analyze.** The coordinates don't have to be exact, just the city is fine. **YOU ALSO NEED THE HOUR and MINUTE of your birth.** You can find this information on your birth certificate or ask your parents. If you don't know your birth time, you can try to guess it, but the results will be less accurate. The hour and minute are important because they determine your rising sign, which is a crucial part of your astrological profile.

If you interrupt the program, you can resume it by running the same command again **BUT input the same information.**
After the program finishes, you can save the generated .txt files in a separate folder and run the program with other inputs.

You can delete the generated .txt files using [cleanup.py](./cleanup.py)

## How does astrology compatibility work?

Astrological compatibility, often explored in relationships, is based on the belief that the positions of celestial bodies at the time of birth can influence an individual's personality and fate. This compatibility is assessed using birth charts, which represent the positions of the sun, moon, planets, and stars at a specific time and place. By comparing and interpreting these charts, astrologers aim to understand how individuals interact with each other, focusing on aspects like emotional connection, communication styles, and overall relationship harmony. This ancient practice combines astronomical calculations with symbolic interpretation, offering insights into potential strengths and challenges in relationships.

**Is it accurate?** In my perspective, the efficacy of this tool is undeniable, which is why I was motivated to create it in the first place. Initially developed for my personal use, I realized its potential benefits for others and therefore chose to share it publicly. This decision was driven by the hope that it might prove equally useful to others as it has been to me.

## How the script works

The program uses the [Astro-Seek](https://horoscopes.astro-seek.com/) website to fetch compatibility scores. It uses the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to parse the HTML and extract the scores. It just "bruteforces" the dates and saves the date of partners you might be compatible with. It also generates charts using the [matplotlib](https://matplotlib.org/) library. [Colorama](https://pypi.org/project/colorama/) is used to color the output, it might be glitchy on some terminals. If you on Windows, you can use [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab) for the best experience.

## Contributing

Contributions, bug reports, and feature requests are welcome. Please open an issue or submit a pull request. Sorry for the ugly code, the project is made in one hour.

## License

Use it however you want but give me credit. I'm not responsible for any consequences of using this tool.
