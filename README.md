# BruteforceLOML

**BruteforceLOML** is a Python script that explores astrological compatibility by identifying the most favorable birth dates for a potential partner. Built for astrology enthusiasts, it analyzes a range of dates to find those that align best with your birth chart.

---

## 🔮 Key Features

* Generates detailed compatibility reports (high and low scores)
* Saves results in `.txt` files for quick search and reference
* Visualizes:

  * Score distribution
  * Score progression over time
  * Monthly average scores
* Real-time ASCII score chart in the console
* Estimates processing time (approx. 4 minutes per year of data)
* Automatically fetches geolocation based on your input

---

## 📦 Installation

Ensure you have Python 3 installed. Then install the required libraries:

```bash
pip install requests beautifulsoup4 matplotlib colorama
```

Download or clone the repo and run:

```bash
python BruteforceLOML.py
```

---

## 📝 Usage

You’ll be prompted for:

* Your **birth date, time (hour + minute), and location** (coordinates or city)
* A range of dates to analyze

⚠️ *Birth time is important — it determines your rising sign. If unknown, an estimate will reduce accuracy.*

To **resume** a stopped analysis, run the script again with the exact same inputs.

To clean up generated files, run:

```bash
python cleanup.py
```

---

## ⚙️ How It Works

* Fetches compatibility scores from [Astro-Seek](https://horoscopes.astro-seek.com/)
* Uses:

  * `BeautifulSoup` for HTML parsing
  * `matplotlib` for charts
  * `colorama` for colored terminal output

Best viewed on **Windows Terminal** if using Windows.

---

## 🤝 Contributing

Pull requests and suggestions are welcome! The code was developed quickly and may be rough around the edges.

---

## 📄 License

Use freely with attribution. The author is not liable for any outcomes from use of this tool.
