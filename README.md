# Resolution Increaser
### A resolution-increasing program.


## Project Description
This program iterates through EV profiles with a 10-minute sampling rate and converts it to 15 minutes, outputting the new profiles in resampled_data. The output rate doesn't necessarily have to be 15 minutes and can be varied, as long as it remains at a resolution that is lower than that of the input CSVs. The program averages the values in between and ceils any values larger than a 0 and less than 5.76 kW to 5.76 kW. Due to this, this program is specific for EVSEs with a power rating of 5.76 kW and it would need to be accordingly adjusted for different power ratings.

## Requirements
```
pip install pandas numpy
```

### To get the code
```
git clone https://github.com/neighdeen84/Resolution_Increaser.git
```


## Usage
```
cd Resolution_Increaser
python main.py
```


