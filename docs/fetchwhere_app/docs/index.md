# Fetchwhere App

## Commands

* Python: - python Fetch [payload]
* Command Line: - Fetch.exe [payload]


## Project layout
    
    build/                  # Build folder from build process.
    config/
        config.ini          # The configuration file.
        [ionapifile].ionapi # The ionapi credential file from InforOS. 
                            # Rename to anything you like but must be 
                            # properely referenced in the config.ini file.
    dist/                   # Contains the compiled source.
    docs/
        docs/
            fetchwhere_app/
                index.md    # Main markdown index file
                mkdocs.yml  # Config file
    lib/
        __.init__.py        # Package indicator
        GetTokenClass.py    # Class file to parse config.ini properties and get auth token
    payloads/               # Folder to store fetchwhere payloads (request files)
    Fetch.exe               # The compiled app
    Fetch.py                # The python source
    nsa_icon.ico            # NSA logo



