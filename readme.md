# SlotCarChampionshipGP

SlotCarChampionshipGP is a race management system for slot car championships. It processes race results from text files, organizes driver statistics, and generates dynamic HTML reports for visualization.

## Features

- **Race Results Processing**: Reads and parses results from the given file
- **Driver Standings**: Sorts drivers based on laps, total time, and best lap
- **Dynamic Leaderboard**: Uses HTML templates to display race data
- **Live Updates**: Watches for file changes and updates results automatically

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/SlotCarChampionshipGP.git
   cd SlotCarChampionshipGP
   ```
2. Install dependencies:
   ```sh
   pip install jinja2
   ```
3. Run the application:
   ```sh
   python main.py "path to file"
   ```

## Usage

1. Place the race results file in the project folder.
2. The system will automatically detect changes and update the leaderboard.
3. View the results in the generated HTML report.

## Contribution

Pull requests are welcome! Feel free to submit issues and suggestions for improvements.

## License

This project is licensed under the GPL-3.0 license.

