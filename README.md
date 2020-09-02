# Twitch Chat AI
Why? cause we did  


## Dependencies
* [Twitch Chat Downloader (TCD)](https://github.com/PetterKraabol/Twitch-Chat-Downloader)  
* [Markovify](https://github.com/jsvine/markovify)  (for markov chain based results)  
* [textgenrnn](https://github.com/minimaxir/textgenrnn)  (for NN based results)  
* [demoji](https://pypi.org/project/demoji/)  (to remove emojis from the source material)

## Usage
1. Download the vods with TCD in JSON format into the `training` folder  
    ```sh
        $ cd training
        $ tcd --channel ramee,uhsnow,koil,lord_kebun,thacoop,lagtvmaximusblack --first 5 -f json
    ```
2. Run `conversion.py`, located in the main folder
    ```sh
        $ python conversion.py
    ```
3. CD into the output folder then `cat *.txt > ../processed/output.txt`
4. Then you can run your choice of `markov.py` or `ai.py`
    ```sh
        $ python markov.py
    ```
    or  
    ```sh
        $ python ai.py
    ```